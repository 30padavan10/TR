shpd_access = '''{num}. Организация услуги ШПД в интернет access'ом.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{mask}, в порт подключения выдать vlan access.
'''


shpd_trunk = '''{num}. Организация услуги ШПД в интернет trunk'ом.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{mask}, согласовать с клиентом tag vlan, в порт подключения выдать vlan тегом.'''


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

gate_yes = '''3. Организация услуги телефония.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
Организовать {tel_lin} {kol_lin1} от тел. шлюза {mod} (установлен на АВ) до телефонного оборудования клиента. {kol_lin2} Р{nu} тел. шлюза.
 
ОЭППО проведение работ:
1. Настроить {tel_lin}-канальный тел. номер. '''

hot_spot = '''{num}. Организация услуги Хот-спот {hot_name}.
------------------------------------------------------------------------------------------

Подготовка ОИПМ/ОИПД.
Заблаговременно создать заявку на ОНИТС СПД для создания Хот-спот.

Проведение работ ОИПМ/ОИПД.
- Подключить беспроводн{hot_st1} станц{hot_st2} {hot_mod} к СПД по решению ОАТТР.

Подготовка ОНИТС СПД.
По заявке в Cordis подготовиться к организации услуги Хот-спот:
- проектируемое количество клиентов Хот-Спот: {hot_client};
- проектируемое количество беспроводных станций: {hot_kol};

Проведение работ ОНИТС СПД.
1. Запустить беспроводн{hot_st1} станц{hot_st2}, организовать управление станци{hot_st3}.
2. Передать информацию в ОСИС заявкой в Cordis.

Проведение работ ОСИС.
Настроить беспроводн{hot_st1} станц{hot_st2} под услугу Хот-спот, запустить услугу Хот-спот для клиента.'''

var_lin = ('телефонную линию от АВ до телефонного оборудования клиента. Включить линию через кросс в порт', 'телефонные линии от АВ до телефонного оборудования клиента. Включить линии через кросс в порты', 'телефонных линий от АВ до телефонного оборудования клиента. Включить линии через кросс в порты')
var_lin2 = ('ю', 'и')
var_lin_gate_yes_1 = ('телефонную линию', 'телефонные линии', 'телефонных линий')
var_lin_gate_yes_2 = ('Включить линию через кросс в порт', 'Включить линии через кросс в порты')
hotspot_name = ('Стандарт', 'Премиум')
hotspot_st1 = ('ую', 'ые')
hotspot_st2 = ('ию', 'ии')
hotspot_st3 = ('ей', 'ями')
hotspot_model = ('D-Link DIR-300', 'Ubiquiti UniFi')

def service():
    service = input('Услуга(ШПД-1, телефония-2, Хот-спот-3):  ')

    if service == '1':
        access = input('access/trunk(a,t): ')
        if access == 'a':
            mask = input('Input mask: ')
            result = shpd_access.format(mask)
            title = shpd_access[:shpd_access.index('---')]
        elif access == 't':
            mask = input('Input mask: ')
            result = shpd_trunk.format(mask=mask)
            title = shpd_access[:shpd_trunk.index('---')]
    elif service == '2':
        gate = input('Требуется установка шлюза? ')
        if gate == 'y':
            model = input('Модель: ')
            linii = input('Количество линий ')
            number_port = input('Порты на шлюзе ')
            if int(linii) == 1:
                result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[0], nu=number_port, chis=var_lin2[0])
            elif 2 <= int(linii) <=4:
                result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[1], nu=number_port, chis=var_lin2[1])
            else:
                result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[2], nu=number_port, chis=var_lin2[1])
            title = gate_no[:gate_no.index('---')]
        elif gate == 'n':
            model = input('Модель: ')
            linii = input('Количество линий ')
            number_port = input('Порты на шлюзе ')
            if int(linii) == 1:
                result = gate_yes.format(mod=model, tel_lin=linii, kol_lin1=var_lin_gate_yes_1[0], nu=number_port, kol_lin2=var_lin_gate_yes_2[0])
            elif 2 <= int(linii) <=4:
                result = gate_yes.format(mod=model, tel_lin=linii, kol_lin1=var_lin_gate_yes_1[1], nu=number_port, kol_lin2=var_lin_gate_yes_2[1])
            else:
                result = gate_yes.format(mod=model, tel_lin=linii, kol_lin1=var_lin_gate_yes_1[2], nu=number_port, kol_lin2=var_lin_gate_yes_2[1])
            title = gate_yes[:gate_yes.index('---')]
    elif service == '3':
        hotspot = input('Cтандарт-1/Премиум-2: ')
        hotspot_client = input('Количество клиентов: ')
        hotspot_kol = input('Количество точек: ')
        if hotspot == '1' and hotspot_kol == '1':
            result = hot_spot.format(hot_name=hotspot_name[0], hot_mod=hotspot_model[0], hot_st1=hotspot_st1[0], hot_st2=hotspot_st2[0], hot_st3=hotspot_st3[0], hot_client=hotspot_client, hot_kol=hotspot_kol)
        elif hotspot == '1' and int(hotspot_kol) > 1:
            result = hot_spot.format(hot_name=hotspot_name[0], hot_mod=hotspot_model[0], hot_st1=hotspot_st1[1], hot_st2=hotspot_st2[1], hot_st3=hotspot_st3[1], hot_client=hotspot_client, hot_kol=hotspot_kol)
        elif hotspot == '2' and hotspot_kol == '1':
            result = hot_spot.format(hot_name=hotspot_name[1], hot_mod=hotspot_model[1], hot_st1=hotspot_st1[0], hot_st2=hotspot_st2[0], hot_st3=hotspot_st3[0], hot_client=hotspot_client, hot_kol=hotspot_kol)
        elif hotspot == '2' and int(hotspot_kol) > 1:
            result = hot_spot.format(hot_name=hotspot_name[1], hot_mod=hotspot_model[1], hot_st1=hotspot_st1[1], hot_st2=hotspot_st2[1], hot_st3=hotspot_st3[1], hot_client=hotspot_client, hot_kol=hotspot_kol)
        title = result[:result.index('---')]
    return result, title


if __name__ == '__main__':
    res = []
    kol = int(input('Количество услуг '))
    for i in range(kol):
        usl, usl_tit = service()
        res.append(usl)
        res.append(usl_tit)
    res.sort()
    for i in res:
        print(i)
