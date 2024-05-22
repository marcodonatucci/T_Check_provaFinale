from Connection import device_DAO, connector


class Model:
    def __init__(self, telefono):
        self.device = None
        self.connection = None
        self.telefono = telefono

    def setDevice(self, imei, selected_type):
        self.device = device_DAO.getDevice(imei, selected_type, self.connection)

    def setConnection(self):
        self.connection = connector.Connection()

    def setToken(self, username, password):
        self.connection.getTokenRequest(username, password)

    def doBlocco(self):
        msg = {
            '1': 'relay,1#',
            '2': 'relay,1#',
            '3': 'relay,1#',
            '4': 'relay,1#',
            '5': 'relay,1#',
            '7': 'setdigout 1',
            '8': 'setdigout 11',
            '12': 'AT+GTDOS=gv58ceu,0,1,1,1,0,0,0,,1,0,5,,,,FFFF$',
        }
        name = 'Blocco Motore'
        itemId = self.device.itemId
        var_msg = msg.get(self.device.selected_type)
        result = self.connection.executeCommand(name, var_msg, itemId)
        return result

    def doTacho(self):
        msg = {
            '9': 'tachocheck',
            '11': 'tachocheck',
            '13': 'AT+GTTTR=gv355ceu,10,,,,,,,,FFFF$',
        }
        name = {
            '9': 'check',
            '11': 'tacho',
            '13': 'tacho check'
        }
        itemId = self.device.itemId
        var_name = name.get(self.device.selected_type)
        var_msg = msg.get(self.device.selected_type)
        result = self.connection.executeCommand(var_name, var_msg, itemId)
        if result:
            try:
                output = self.connection.getConnection(self.device.uid)['prms']['text']['v']
            except KeyError as e:
                output = True
            return output
        else:
            return False

    def doSblocco(self):
        msg = {
            '1': 'relay,0#',
            '2': 'relay,0#',
            '3': 'relay,0#',
            '4': 'relay,0#',
            '5': 'relay,0#',
            '7': 'setdigout 0',
            '8': 'setdigout 00',
            '12': 'AT+GTDOS=gv58ceu,0,1,1,0,0,0,0,,1,0,5,,,,FFFF$',
        }
        name = 'Sblocco Motore'
        itemId = self.device.itemId
        var_msg = msg.get(self.device.selected_type)
        result = self.connection.executeCommand(name, var_msg, itemId)
        if result:
            try:
                output = self.connection.getConnection(self.device.uid)['prms']['text']['v']
            except KeyError as e:
                try:
                    output = self.connection.getConnection(self.device.uid)['prms']['msg']['v']
                except KeyError as e:
                    output = True
            return output
        else:
            return False

    def doName(self, nome):
        itemId = self.device.itemId
        result = self.connection.update_name(itemId, nome)
        return result

    def doCall(self, numero):
        self.telefono(numero)

    def defineType(self):
        types = {
            '1': 'Topflytech T8806+R',
            '2': 'Topflytech T8803',
            '3': 'Topflytech T8803+',
            '4': 'Topflytech T8803+E',
            '5': 'Topflytech TLW2-12BL',
            '6': 'Topflytech PioneerX100',
            '7': 'Teltonika FMB920',
            '8': 'Teltonika FMB140',
            '9': 'Teltonika FMB640',
            '10': 'Teltonika FMC150',
            '11': 'Teltonika FMC640',
            '12': 'Queclink GV58CEU',
            '13': 'Queclink GV355CEU'
        }
        return types[self.device.selected_type]

    def doEmail(self, username, note, cliente):
        message = (f"Nome account: {username}\n"
                   f"Nome cliente: {cliente}\n"
                   f"Tipo dispositivo: {self.defineType()}\n\n"
                   f"{self.device.__str__()}\n\n"
                   f"Note: {note}")
        self.connection.send_email(message)
