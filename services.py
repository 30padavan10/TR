shpd_access = '''2. Организация услуги ШПД в интернет access'ом.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{}, в порт подключения выдать vlan access.
'''


shpd_trunk = '''2. Организация услуги ШПД в интернет trunk'ом.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{}, согласовать с клиентом tag vlan, в порт подключения выдать vlan тегом.'''


gate_no = '''3. Организация услуги телефония.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
1. Заблаговременно создать заявку на ОНИТС СПД для настройки шлюза. 
2. Установить в АВ тел. шлюз {mod}. Установить в АВ телефонный кросс. 
3. Организовать {tel_lin} {kol_lin} Р{nu} тел. шлюза. В кроссе на лини{chis} установить штекер защиты.

ОНИТС СПД проведение работ:
1. Совместно с ОИПМ установить телефонный шлюз на АВ.
2. Передать информацию в ОЭППО.

ОЭППО проведение работ:
1. Настроить тел. шлюз в качестве шлюза под ВАТС. 
2. Организовать ВАТС с базовым набором сервисов на 3 внутренних порта для 3-канального тел. номера.'''

var_lin = ('телефонную линию от АВ до телефонного оборудования клиента. Включить линию через кросс в порт', 'телефонные линии от АВ до телефонного оборудования клиента. Включить линии через кросс в порты', 'телефонных линий от АВ до телефонного оборудования клиента. Включить линии через кросс в порты')
var_lin2 = ('ю', 'и')

def service():
    service = input('Услуга(ШПД-1, телефония-2):  ')

    if service == '1':
        access = input('access/trunk(a,t): ')
        if access == 'a':
            mask = input('Input mask: ')
            result = shpd_access.format(mask)
            title = shpd_access[:shpd_access.index('---')]
        elif access == 't':
            mask = input('Input mask: ')
            result = shpd_trunk.format(mask)
            title = shpd_access[:shpd_trunk.index('---')]
    elif service == '2':
        gate = input('Требуется установка шлюза? ')
        if gate == 'y' or 'н':
            model = input('Модель: ')
            linii = input('Количество линий ')
            number_port = input('Порт на шлюзе ')
            if int(linii) == 1:
                result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[0], nu=number_port, chis=var_lin2[0])
            elif 2 <= int(linii) <=4:
                result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[1], nu=number_port, chis=var_lin2[1])
            else:
                result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[2], nu=number_port, chis=var_lin2[1])
            title = gate_no[:gate_no.index('---')]
        elif gate == 'n' or 'т':
            pass
    return result, title


if __name__ == '__main__':
    res = []
    kol = int(input('Количество услуг '))
    for i in range(kol):
        usl, usl_tit = service()
        res.append(usl)
        res.append(usl_tit)
    for i in res:
        print(i)
