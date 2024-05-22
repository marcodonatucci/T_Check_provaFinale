import time
import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDdType(self):
        self._view.ddType.options.append(ft.dropdown.Option(key='1', text="Topflytech T8806+R"))
        self._view.ddType.options.append(ft.dropdown.Option(key='2', text="Topflytech T8803"))
        self._view.ddType.options.append(ft.dropdown.Option(key='3', text="Topflytech T8803+"))
        self._view.ddType.options.append(ft.dropdown.Option(key='4', text="Topflytech T8803+E"))
        self._view.ddType.options.append(ft.dropdown.Option(key='5', text="Topflytech TLW2-12BL"))
        self._view.ddType.options.append(ft.dropdown.Option(key='6', text="Topflytech PioneerX100"))
        self._view.ddType.options.append(ft.dropdown.Option(key='7', text="Teltonika FMB920"))
        self._view.ddType.options.append(ft.dropdown.Option(key='8', text="Teltonika FMB140"))
        self._view.ddType.options.append(ft.dropdown.Option(key='9', text="Teltonika FMB640"))
        self._view.ddType.options.append(ft.dropdown.Option(key='10', text="Teltonika FMC150"))
        self._view.ddType.options.append(ft.dropdown.Option(key='11', text="Teltonika FMC640"))
        self._view.ddType.options.append(ft.dropdown.Option(key='12', text="Queclink GV58CEU"))
        self._view.ddType.options.append(ft.dropdown.Option(key='13', text="Queclink GV355CEU"))

    def handle_search(self, e):
        self._view.txt_result.clean()
        self._view.pr.visible = True
        self._view.update_page()
        imei = self._view.txt_imei.value
        imei = str(imei).replace(" ", "")
        if not imei.isdigit():
            self._view.create_alert("IMEI errato! Riprova")
            self._view.txt_imei.value = ''
            self._view.pr.visible = False
            self._view.update_page()
            return
        if self._model.connection is None:
            self._view.create_alert("Accedi con username e password")
            self._view.txt_imei.value = ''
            self._view.pr.visible = False
            self._view.update_page()
            return
        if self._view.ddType.value is None or self._view.ddType.value == '':
            self._view.create_alert("Seleziona il tipo di dispositivo")
            self._view.txt_imei.value = ''
            self._view.pr.visible = False
            self._view.update_page()
            return
        self._model.setDevice(imei, self._view.ddType.value)
        tempo_di_attesa = 10
        start_time = time.time()
        while self._model.device is None:
            if time.time() - start_time >= tempo_di_attesa:
                break
            else:
                pass
        if self._model.device is None:
            self._view.txt_result.controls.append(
                ft.Text("Dispositivo non trovato! controlla l'IMEI e il tipo di dispositivo e riprova", color='red'))
            self._view.pr.visible = False
            self._view.update_page()
            return
        drop = self._view.ddType.value
        self._view.pr.visible = False
        self._view._page.controls.clear()
        self._view.load_results_interface()
        self._view.update_page()
        blocco = ['1', '2', '3', '4', '5', '7', '8', '12']
        tacho = ['9', '11', '13']
        if blocco.__contains__(drop):
            self._view.btn_blocco.disabled = False
            self._view.btn_sblocco.disabled = False
        if tacho.__contains__(drop):
            self._view.btn_tacho.disabled = False
        for row in self._model.device.displayData():
            self._view.table.rows.append(row)
        # self._view.txt_result.controls.append(ft.Text(self._model.device.__str__()))
        self._view.update_page()

    def handle_login(self, e):
        self._view.pr.visible = True
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._model.connection is None:
            self._model.setConnection()
        if self._view.txt_username.value is None or self._view.txt_username.value == '':
            self._view.create_alert("Inserisci username e password!")
            self._view.pr.visible = False
            self._view.update_page()
            return
        if self._view.txt_password.value is None or self._view.txt_password.value == '':
            self._view.create_alert("Inserisci username e password!")
            self._view.pr.visible = False
            self._view.update_page()
            return
        username = self._view.txt_username.value.replace(" ", "")
        password = self._view.txt_password.value.replace(" ", "")
        self._model.setToken(username, password)
        tempo_di_attesa = 10
        start_time = time.time()
        while self._model.connection.token is None:
            if time.time() - start_time >= tempo_di_attesa:
                break
            else:
                pass
        if self._model.connection.token is None:
            self._view.txt_result.controls.append(
                ft.Text("Accesso non riuscito! controlla username e password e riprova", color='red'))
            self._view.pr.visible = False
            self._view.update_page()
            return
        self._view.pr.visible = False
        self._view.username = self._view.txt_username.value
        self._view.txt_username.value = ''
        self._view.txt_password.value = ''
        self._view._page.controls.clear()
        self._view.load_search_interface()
        self._view.update_page()

    def back(self, e):
        self._view._page.controls.clear()
        self._view.load_search_interface()
        self._view.update_page()

    def refresh(self, e):
        self._view._page.controls.clear()
        self._view.update_page()
        self._model.setDevice(self._model.device.uid, self._model.device.selected_type)
        self._view.load_results_interface()
        self._view.update_page()
        blocco = ['1', '2', '3', '4', '5', '7', '8', '12']
        tacho = ['9', '11', '13']
        if blocco.__contains__(self._model.device.selected_type):
            self._view.btn_blocco.disabled = False
            self._view.btn_sblocco.disabled = False
        if tacho.__contains__(self._model.device.selected_type):
            self._view.btn_tacho.disabled = False
        for row in self._model.device.displayData():
            self._view.table.rows.append(row)
        # self._view.txt_result.controls.append(ft.Text(self._model.device.__str__()))
        self._view.update_page()

    def handle_blocco(self, e):
        self._view.txt_result.clean()
        self._view.pr.visible = True
        self._view.update_page()
        var = self._model.doBlocco()
        tempo_di_attesa = 10
        start_time = time.time()
        while not var:
            if time.time() - start_time >= tempo_di_attesa:
                break
            else:
                pass
        if var:
            self._view.pr.visible = False
            self._view.txt_result.controls.append(ft.Text(f"Risposta comando: {var}", color='green'))
            self._view.update_page()
            return
        else:
            self._view.pr.visible = False
            self._view.txt_result.controls.append(ft.Text("Blocco non riuscito! Riprova!", color='red'))
            self._view.update_page()
            return

    def handle_tacho(self, e):
        self._view.txt_result.clean()
        self._view.pr.visible = True
        self._view.update_page()
        var = self._model.doTacho()
        tempo_di_attesa = 10
        start_time = time.time()
        while not var:
            if time.time() - start_time >= tempo_di_attesa:
                break
            else:
                pass
        if var:
            self._view.pr.visible = False
            self._view.txt_result.controls.append(ft.Text(f"Risposta comando: {var}"))
            self._view.update_page()
            return
        else:
            self._view.pr.visible = False
            self._view.txt_result.controls.append(ft.Text("Invio comando non riuscito! Riprova!", color='red'))
            self._view.update_page()
            return

    def handle_sblocco(self, e):
        self._view.txt_result.clean()
        self._view.pr.visible = True
        self._view.update_page()
        var = self._model.doSblocco()
        tempo_di_attesa = 10
        start_time = time.time()
        while not var:
            if time.time() - start_time >= tempo_di_attesa:
                break
            else:
                pass
        if var:
            self._view.pr.visible = False
            self._view.txt_result.controls.append(ft.Text(f"Risposta comando: {var}", color='green'))
            self._view.update_page()
            return
        else:
            self._view.pr.visible = False
            self._view.txt_result.controls.append(ft.Text("Sblocco non riuscito! Riprova!", color='red'))
            self._view.update_page()
            return

    def handle_nome(self, e):
        self._view.create_model_alert_nome()
        self._view.update_page()

    def handle_termina_float(self, e):
        self._view._page.controls.clear()
        self._view.load_final_interface()
        self._view.update_page()

    def handle_termina(self, e):
        if self._view.txt_cliente.value is None or self._view.txt_cliente.value == '':
            self._view.create_alert("Inserisci il nome del cliente per continuare!")
            self._view.update_page()
            return
        self._view.create_model_alert_collaudo()
        self._view.update_page()

    def handle_yes_collaudo(self, e):
        self._view._page.dialog.open = False
        self._view.update_page()
        self._view._page.controls.clear()
        if self._model.device is None:
            self._view.create_alert("Nessun dispositivo collaudato, cerca il dispositivo!")
            self._view.load_search_interface()
            self._view.update_page()
            return
        try:
            self._model.doEmail(self._view.username, self._view.txt_final.value, self._view.txt_cliente.value)
        except:
            self._view.create_alert("Problemi riscontrati nel termine collaudo, contatta il tecnico!")
            self._view.load_search_interface()
            self._view.update_page()
            return
        self._view.create_alert("Collaudo terminato")
        self._model.device = None
        self._view.load_search_interface()
        self._view.update_page()

    def handle_no_collaudo(self, e):
        self._view._page.dialog.open = False
        self._view.update_page()

    def handle_send_name(self, e):
        self._view._page.dialog.open = False
        self._view.update_page()
        nome = self._view._page.dialog.actions[0].value
        result = self._model.doName(nome)
        if result:
            self._view.create_alert("Nome dispositivo cambiato")
        else:
            self._view.create_alert("Cambio nome non andato a buon fine, riprova!")
        self._view.update_page()

    def handle_call(self, e):
        self._view.create_model_alert_call()

    def handle_call_Marco(self, e):
        self._model.doCall('+393519297869')

    def handle_call_Marisa(self, e):
        self._model.doCall('+393386083090')
