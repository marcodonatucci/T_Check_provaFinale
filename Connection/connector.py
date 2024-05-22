import smtplib
import webbrowser
from urllib.parse import urlparse, parse_qs
from wialon import Wialon, WialonError
import libs.requests as requests


class Connection:
    def __init__(self):
        self.token = None
        self.wialon_api = None

    def getConnection(self, imei):
        '''Stabilisce una connessione al server ed effettua il login'''
        try:
            self.wialon_api = Wialon()
            result = self.wialon_api.token_login(
                token=self.token)
            self.wialon_api.sid = result['eid']

            search_spec = {
                'itemsType': 'avl_unit',
                'propName': 'sys_unique_id',
                'propValueMask': imei,
                'sortType': 'sys_name'
            }

            search_result = self.wialon_api.search_items(spec=search_spec)
            if len(search_result['items']) == 0:
                return None
            item_data = search_result['items'][0]
            #  ATTIVAZIONE UNITA!
            if item_data['act'] == 0:
                activation = self.wialon_api.active_unit(item_data['id'])
                item_data['act'] = activation['active']
            self.wialon_api.core_logout()
            return item_data
        except WialonError as e:
            print(e)

    def setToken(self, new_url):
        '''Apre la pagina web di login, l'utente incolla l'url dopo aver effettuato l'accesso e il metodo estrae il token'''
        parsed_url = urlparse(new_url)
        query_params = parse_qs(parsed_url.query)
        access_token = query_params.get('access_token', [None])[0]
        self.token = access_token

    def getTokenRequest(self, username, password):
        url = 'https://hst-api.wialon.com/oauth/authorize.html?lang=en'
        data = {
            'response_type': 'token',
            'wialon_sdk_url': 'https://hst-api.wialon.com',
            'success_uri': '',
            'login_uri': 'https://tracking.topflyiot.com/login.html',
            'client_id': 'wialon',
            'redirect_uri': 'https://tracking.topflyiot.com/login.html',
            'access_type': '-1',
            'activation_time': '0',
            'duration': '0',
            'flags': '7',
            'login': username,
            'passw': password
        }
        headers = {
            'origin': 'https://tracking.topflyiot.com',
            'content-type': 'application/x-www-form-urlencoded',
            'refer': 'https://tracking.topflyiot.com/'
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            get_url = response.request.url
            self.setToken(get_url)
        else:
            return None

    def executeCommand(self, command, param, itemId):
        params = {
            "itemId": itemId,
            "commandName": command,
            "linkType": "tcp",
            "param": param,
            "timeout": 10,
            "flags": 0
        }
        try:
            result = self.wialon_api.token_login(
                token=self.token)
            self.wialon_api.sid = result['eid']
            command_result = self.wialon_api.execute_cmd(params=params)
            if len(command_result) == 0:
                return True
            else:
                return None
        except WialonError as e:
            print(e)

    def update_name(self, itemId, name):
        try:
            result = self.wialon_api.token_login(
                token=self.token)
            self.wialon_api.sid = result['eid']
            # NUOVO NOME, DA TESTARE!
            command_result = self.wialon_api.update_name(itemId, name)
            if command_result['nm'] == name:
                return True
            else:
                return False
        except WialonError as e:
            print(e)

    # def make_phone_call(self, numero):
    # CAMBIA NUMERO
    # Costruisci l'URL con il numero di telefono precompilato
    #    tel_url = f'tel:{numero}'
    # Apri l'URL nel browser
    #    webbrowser.open(tel_url)

    def send_email(self, message):
        subject = "Conferma collaudo dispositivo"
        encoded_subject = f"Subject: {subject}\n\n"

        # Concatena il soggetto e il messaggio decodificato
        full_message = encoded_subject + message

        # Codifica il messaggio completo in UTF-8
        encoded_message = full_message.encode('utf-8')
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('collaudotopfly@gmail.com', 'mkut jets fifq fehz')
        server.sendmail('collaudotopfly@gmail.com', 'collaudotopfly@gmail.com', encoded_message)
        server.quit()
