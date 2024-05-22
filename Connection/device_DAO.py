from Model import device1234, device6, device7, device8, device9, device5, device10, device11, device12, device13, \
    device


def getDevice(imei, selected_type, connection):
    '''Crea gli oggetti Device e li include nel model'''
    imei = str(imei)
    connessione = connection.getConnection(imei)
    if connessione is not None:
        if selected_type == '1' or selected_type == '2' or selected_type == '3' or selected_type == '4':
            try:
                result_device = device1234.Device1234(uid=connessione['uid'],
                                                      itemId=connessione['id'],
                                                      name=connessione['nm'],
                                                      position=(connessione['pos']['x'], connessione['pos']['y']),
                                                      device_status=connessione['act'],
                                                      object_status=connessione['prms']['in']['v'],
                                                      selected_type=selected_type,
                                                      battery=connessione['prms']['pwr_ext']['v'],
                                                      total_km=connessione['prms']['mileage']['v'],
                                                      blocco=connessione['prms']['relay']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '5':
            try:
                result_device = device5.Device5(uid=connessione['uid'],
                                                itemId=connessione['id'],
                                                name=connessione['nm'],
                                                position=(connessione['pos']['x'], connessione['pos']['y']),
                                                device_status=connessione['act'],
                                                object_status=connessione['prms']['ign']['v'],
                                                selected_type=selected_type,
                                                battery=connessione['prms']['pwr_ext']['v'],
                                                total_km=float(connessione['prms']['odometer']['v']) / 1000,
                                                blocco=connessione['prms']['digital_out']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '6':
            try:
                result_device = device6.Device6(uid=connessione['uid'],
                                                itemId=connessione['id'],
                                                name=connessione['nm'],
                                                position=(connessione['pos']['x'], connessione['pos']['y']),
                                                device_status=connessione['act'],
                                                object_status=connessione['prms']['ign']['v'],
                                                selected_type=selected_type,
                                                battery=connessione['prms']['pwr_ext']['v'],
                                                total_km=float(connessione['prms']['odometer']['v']) / 1000)
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '7':
            try:
                result_device = device7.Device7(uid=connessione['uid'],
                                                itemId=connessione['id'],
                                                name=connessione['nm'],
                                                position=(connessione['pos']['x'], connessione['pos']['y']),
                                                device_status=connessione['act'],
                                                object_status=connessione['prms']['io_239']['v'],
                                                selected_type=selected_type,
                                                battery=connessione['prms']['pwr_ext']['v'],
                                                total_km=float(connessione['prms']['io_16']['v']) / 1000,
                                                blocco=connessione['prms']['io_179']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '8':
            try:
                result_device = device8.Device8(uid=connessione['uid'],
                                                itemId=connessione['id'],
                                                name=connessione['nm'],
                                                position=(connessione['pos']['x'], connessione['pos']['y']),
                                                device_status=connessione['act'],
                                                object_status=connessione['prms']['io_239']['v'],
                                                selected_type=selected_type,
                                                battery=connessione['prms']['pwr_ext']['v'],
                                                total_km=float(connessione['prms']['io_87']['v']) / 1000,
                                                blocco=connessione['prms']['io_179']['v'],
                                                fuel_percentage=connessione['prms']['io_89']['v'],
                                                rpm=connessione['prms']['io_85']['v'],
                                                water_temp=float(connessione['prms']['io_115']['v']) / 10)
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '9':
            try:
                result_device = device9.Device9(uid=connessione['uid'],
                                                itemId=connessione['id'],
                                                name=connessione['nm'],
                                                position=(connessione['pos']['x'], connessione['pos']['y']),
                                                device_status=connessione['act'],
                                                object_status=connessione['prms']['io_239']['v'],
                                                selected_type=selected_type,
                                                battery=connessione['prms']['pwr_ext']['v'],
                                                total_km=connessione['prms']['tco_distance']['v'],
                                                fuel_percentage=connessione['prms']['io_87']['v'],
                                                rpm=connessione['prms']['io_88']['v'],
                                                water_temp=connessione['prms']['io_127']['v'],
                                                driver_id=connessione['prms']['tco_driver1_id']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '10':
            try:
                result_device = device10.Device10(uid=connessione['uid'],
                                                  itemId=connessione['id'],
                                                  name=connessione['nm'],
                                                  position=(connessione['pos']['x'], connessione['pos']['y']),
                                                  device_status=connessione['act'],
                                                  object_status=connessione['prms']['io_239']['v'],
                                                  selected_type=selected_type,
                                                  battery=connessione['prms']['pwr_ext']['v'],
                                                  total_km=float(connessione['prms']['io_87']['v']) / 1000,
                                                  fuel_percentage=connessione['prms']['io_89']['v'],
                                                  rpm=connessione['prms']['io_85']['v'],
                                                  water_temp=float(connessione['prms']['io_115']['v']) / 10,
                                                  blocco=connessione['prms']['io_179']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '11':
            try:
                result_device = device11.Device11(uid=connessione['uid'],
                                                  itemId=connessione['id'],
                                                  name=connessione['nm'],
                                                  position=(connessione['pos']['x'], connessione['pos']['y']),
                                                  device_status=connessione['act'],
                                                  object_status=connessione['prms']['io_239']['v'],
                                                  selected_type=selected_type,
                                                  battery=connessione['prms']['pwr_ext']['v'],
                                                  total_km=connessione['prms']['tco_distance']['v'],
                                                  fuel_percentage=connessione['prms']['io_87']['v'],
                                                  rpm=connessione['prms']['io_88']['v'],
                                                  water_temp=connessione['prms']['io_127']['v'],
                                                  driver_id=connessione['prms']['tco_driver1_id']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '12':
            try:
                result_device = device12.Device12(uid=connessione['uid'],
                                                  itemId=connessione['id'],
                                                  name=connessione['nm'],
                                                  position=(connessione['pos']['x'], connessione['pos']['y']),
                                                  device_status=connessione['act'],
                                                  object_status=connessione['prms']['ign']['v'],
                                                  selected_type=selected_type,
                                                  battery=connessione['prms']['pwr_ext']['v'],
                                                  total_km=float(connessione['prms']['can_total_dist_hect']['v']) / 10,
                                                  fuel_percentage=connessione['prms']['can_fuel_level_p']['v'],
                                                  rpm=connessione['prms']['can_eng_rpm']['v'],
                                                  water_temp=connessione['prms']['can_eng_cool_temp']['v'],
                                                  blocco=connessione['prms']['dout_status']['v'])
                return result_device
            except KeyError as e:
                return None
        elif selected_type == '13':
            try:
                result_device = device13.Device13(uid=connessione['uid'],
                                                  itemId=connessione['id'],
                                                  name=connessione['nm'],
                                                  position=(connessione['pos']['x'], connessione['pos']['y']),
                                                  device_status=connessione['act'],
                                                  object_status=connessione['prms']['ign']['v'],
                                                  selected_type=selected_type,
                                                  battery=connessione['prms']['pwr_ext']['v'],
                                                  total_km=float(connessione['prms']['can_total_distance']['v'])/10,
                                                  fuel_percentage=connessione['prms']['can_fuel_level_p']['v'],
                                                  rpm=connessione['prms']['can_eng_rpm']['v'],
                                                  water_temp=connessione['prms']['can_eng_cool_temp']['v'],
                                                  driver_id=connessione['prms']['tco_driver1_id']['v'])
                return result_device
            except KeyError as e:
                return None
    else:
        return None
