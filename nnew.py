med = '''{num}. Присоединение к СПД по медной линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать медную линию связи от {pps_l} до клиента.
- Подключить организованную линию для клиента в коммутатор {kad_l}, задействовать свободный порт.'''

med_two = '''{num}. Присоединение к СПД по медной линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать 2 медных линии связи от {pps_l} до клиента.
- Подключить организованные линии для клиента в коммутатор {kad_l}, задействовать свободные порты.'''



vols = '''{num}. Присоединение к СПД по оптической линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {kad_l}, порт задействовать свободный.
- Установить на стороне клиента конвертер 1550 нм, выставить на конвертере режим работы 100 FD Force.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''

vols_two = '''{num}. Присоединение к СПД по оптической линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ 2 конвертера 1310 нм, выставить на конвертерах режим работы 100 FD Force.
- Подключить организованные линии для клиента в коммутатор {kad_l}, порты задействовать свободные.
- Установить на стороне клиента 2 конвертера 1550 нм, выставить на конвертерах режим работы 100 FD Force.

ОНИТС СПД проведение работ:
- На портах подключения клиента выставить скоростной режим Auto.'''


vols_idle = '''{num}. Присоединение к СПД по оптической линии связи с простоем связи услуг
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Требуется отключение согласно ППР {ppr_idle} согласовать проведение работ.

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_idle} до клиента по решению ОАТТР.
- Совместно с ОНИТС СПД убедиться в восстановлении связи согласно ППР {ppr_idle}.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {kad_idle}, порт задействовать свободный.
- Установить на стороне клиента конвертер 1550 нм, выставить на конвертере режим работы 100 FD Force.


ОНИТС СПД проведение работ:
- После проведения монтажных работ убедиться в восстановлении услуг согласно ППР {ppr_idle}.
- На порту подключения клиента выставить скоростной режим Auto.'''


vols_csw100 = '''{num}. Присоединение к СПД по оптической линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {kad_l}, порт задействовать свободный.
- Установить на стороне клиента передатчик SFP WDM, дальность до 20 км (14dB), 1550 нм.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''


vols_csw1g = '''{num}. Присоединение к СПД по оптической линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ передатчик SFP WDM, дальность до 20 км (12dB), 1310 нм.
- Подключить организованную линию для клиента в коммутатор {kad_l}, порт задействовать свободный.
- Установить на стороне клиента передатчик SFP WDM, дальность до 20 км (14dB), 1550 нм.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''


CSW_100M_M = '''{num}. Установка клиентского коммутатора
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для настройки клиентского коммутатора.
- Логическое подключение для клиентского коммутатора - {pps_l}, {kad_l}.

ОИПМ проведение работ:
- Установить в помещении клиента коммутатор D-Link DGS-1100-06/ME. Включить линию для клиента в Port 5 коммутатора D-Link DGS-1100-06/ME.
- Совместно с ОНИТС СПД запустить клиентский коммутатор.


ОНИТС СПД подготовиться к работам:
- В рамках заявки в Cordis подготовиться к установке клиентского коммутатора D-Link DGS-1100-06/ME.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ установить клиентский коммутатор.
- Передать информацию в ОУИ СПД.'''


CSW_100M_O = '''{num}. Установка клиентского коммутатора
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для настройки клиентского коммутатора.
- Логическое подключение для клиентского коммутатора - {pps_l}, {kad_l}.

ОИПМ проведение работ:
- Установить в помещении клиента коммутатор D-Link DGS-1100-06/ME. Включить линию для клиента в Port 6 коммутатора D-Link DGS-1100-06/ME.
- Совместно с ОНИТС СПД запустить клиентский коммутатор.


ОНИТС СПД подготовиться к работам:
- В рамках заявки в Cordis подготовиться к установке клиентского коммутатора D-Link DGS-1100-06/ME.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ установить клиентский коммутатор.
- Передать информацию в ОУИ СПД.'''


CSW_1G = '''{num}. Установка клиентского коммутатора
------------------------------------------------------------------------------------------

ВНИМАНИЕ!!!!!!!!!!!!!!!! ТРЕБУЕТСЯ УДАЛЕННАЯ НАСТРОЙКА КОММУТАТОРА D-Link DGS-1100-06/ME С ОНИТС СПД НА ЭТАПЕ ПОДГОТОВКИ К РАБОТАМ.

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для настройки клиентского коммутатора.
- Логическое подключение для клиентского коммутатора - {pps_l}, {kad_l}.
- Совместно с ОНИТС СПД удаленно настроить коммутатор D-Link DGS-1100-06/ME.

ОИПМ проведение работ:
- Установить в помещении клиента коммутатор D-Link DGS-1100-06/ME. Включить линию для клиента в Port 6 коммутатора D-Link DGS-1100-06/ME.
- Совместно с ОНИТС СПД запустить клиентский коммутатор на магистрали 1G.


ОНИТС СПД подготовиться к работам:
- В рамках заявки в Cordis подготовиться к установке клиентского коммутатора D-Link DGS-1100-06/ME.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ установить клиентский коммутатор.
- Передать информацию в ОУИ СПД.'''

csw_port_4 = '''{num}. Присоединение к клиентскому коммутатору по медной линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать {csw_po} медных линии от клиентского коммутатора до оборудования, установленного у клиента. Включить линии в порты:
Port 1 - ШПД в интернет.
Port 2 - телефония.'''


infinet = '''{num}. Присоединение к СПД по беспроводной среде передачи данных
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для выделения реквизитов беспроводных точек доступа WDS/WDA.
- Доставить в офис ОНИТС СПД беспроводные точки Infinet H11 для их настройки.


ОИПМ проведение работ:
После выполнения подготовительных работ в рамках заявки в Cordis и настройки точек в офисе ОНИТС СПД:
- Установить на стороне {pps_l} и на стороне клиента беспроводные точки доступа по решению ОАТТР. На АВ использовать для подключения беспроводной точки коммутатор {kad_l}, свободные порты есть.

ОНИТС СПД подготовиться к работам:
- По заявке в Cordis выделить реквизиты для управления беспроводными точками.
- Настроить беспроводные точки Infinet H11 в офисе.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ подключить к СПД и запустить беспроводные станции (WDS/WDA).'''


ubi = '''{num}. Присоединение к СПД по беспроводной среде передачи данных
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для выделения реквизитов беспроводных точек доступа WDS/WDA.

ОИПМ проведение работ:
После выполнения подготовительных работ в рамках заявки в Cordis на ОНИТС СПД:
- Установить на стороне {pps_l} и на стороне клиента беспроводные точки доступа по решению ОАТТР. На АВ использовать для подключения беспроводной точки коммутатор {kad_l}, свободные порты есть.

ОНИТС СПД подготовиться к работам:
- По заявке в Cordis выделить реквизиты для управления беспроводными точками.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ подключить к СПД и запустить беспроводные станции WDS/WDA.'''

shpd_access = '''{num}. Организация услуги ШПД в интернет access'ом
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{mask}, в порт подключения выдать vlan access.
'''


shpd_trunk = '''{num}. Организация услуги ШПД в интернет trunk'ом
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{mask}, согласовать с клиентом tag vlan, в порт подключения выдать vlan тегом.'''


gate_no = '''3. Организация услуги телефония
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
1. Заблаговременно создать заявку на ОНИТС СПД для настройки шлюза. 
2. Установить в АВ тел. шлюз {mod}. Установить в АВ телефонный кросс. 
3. Организовать {tel_lin} {kol_lin} Р{nu} тел. шлюза. В кроссе на лини{chis} установить штекер защиты.

ОНИТС СПД проведение работ:
1. Совместно с ОИПМ установить телефонный шлюз на АВ.
2. Передать информацию в ОЭППО.

ОЭППО проведение работ:
1. Настроить {tel_lin}-канальный тел. номер.'''

gate_yes = '''3. Организация услуги телефония
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
Организовать {tel_lin} {kol_lin1} от тел. шлюза {mod} (установлен на АВ) до телефонного оборудования клиента. {kol_lin2} Р{nu} тел. шлюза.
 
ОЭППО проведение работ:
1. Настроить {tel_lin}-канальный тел. номер. '''

hot_spot = '''{num}. Организация услуги Хот-спот {hot_name}
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

cks = '''{num}. Организация услуги ЦКС Etherline access'ом
------------------------------------------------------------------------------------------
  
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу ЦКС {cksrate} Мбит/с "{cksa} - {cksb}", в порт подключения выдать vlan access.
- Ограничить скорость и настроить маркировку трафика для ЦКС {ckspolicing}.'''


vls = '''{num}. Организация услуги ВЛС
------------------------------------------------------------------------------------------
 
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу Виртуальная Локальная сеть.'''


port_vls = '''{num}. Организация услуги порт ВЛС access'ом
------------------------------------------------------------------------------------------
 
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу порт Виртуальной Локальной Сети для ВЛС {vls_name} с полосой {vls_rate} Мбит/с, в порт подключения выдать vlan access.'''


var_lin = ('телефонную линию от АВ до телефонного оборудования клиента. Включить линию через кросс в порт', 'телефонные линии от АВ до телефонного оборудования клиента. Включить линии через кросс в порты', 'телефонных линий от АВ до телефонного оборудования клиента. Включить линии через кросс в порты')
var_lin2 = ('ю', 'и')
var_lin_gate_yes_1 = ('телефонную линию', 'телефонные линии', 'телефонных линий')
var_lin_gate_yes_2 = ('Включить линию через кросс в порт', 'Включить линии через кросс в порты')
hotspot_name = ('Стандарт', 'Премиум')
hotspot_st1 = ('ую', 'ые')
hotspot_st2 = ('ию', 'ии')
hotspot_st3 = ('ей', 'ями')
hotspot_model = ('D-Link DIR-300', 'Ubiquiti UniFi')
ckspolicing = ('полисером Subinterface', 'портом подключения')
condition = ['y', 'n', 'н', 'т']
yes = ['y', 'н']
no = ['n', 'т']

titles = [] # нужен для вставления в шаблоны в поле num


def input_text(question):
    '''Функция используется для вопросов с ответами да/нет.
       Принимает текст вопроса и возвращает введенный корректный символ'''
    while True:
        input_t = input(question)
        if input_t in condition:
            break
        else:
            print('Incorrect enter.\n')
    return input_t




def service():
    service = input('Услуга(ШПД-1, телефония-2, Хот-спот-3, ЦКС-4, ВЛС-5):  ')

    if service == '1':
        access = input('access/trunk(a,t): ')
        if access == 'a':
            mask = input('Input mask: ')
            result = shpd_access.format(mask=mask, num=len(titles)+1)
            title = result[:result.index('---')]
            titles.append(title)
        elif access == 't':
            mask = input('Input mask: ')
            result = shpd_trunk.format(mask=mask, num=len(titles)+1)
            title = result[:result.index('---')]
            titles.append(title)
    elif service == '2':
        gate = input_text('Требуется установка шлюза? ')
        if gate in yes:
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
        elif gate in no:
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
            result = hot_spot.format(hot_name=hotspot_name[0], hot_mod=hotspot_model[0], hot_st1=hotspot_st1[0], hot_st2=hotspot_st2[0], hot_st3=hotspot_st3[0], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        elif hotspot == '1' and int(hotspot_kol) > 1:
            result = hot_spot.format(hot_name=hotspot_name[0], hot_mod=hotspot_model[0], hot_st1=hotspot_st1[1], hot_st2=hotspot_st2[1], hot_st3=hotspot_st3[1], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        elif hotspot == '2' and hotspot_kol == '1':
            result = hot_spot.format(hot_name=hotspot_name[1], hot_mod=hotspot_model[1], hot_st1=hotspot_st1[0], hot_st2=hotspot_st2[0], hot_st3=hotspot_st3[0], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        elif hotspot == '2' and int(hotspot_kol) > 1:
            result = hot_spot.format(hot_name=hotspot_name[1], hot_mod=hotspot_model[1], hot_st1=hotspot_st1[1], hot_st2=hotspot_st2[1], hot_st3=hotspot_st3[1], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        title = result[:result.index('---')]
        titles.append(title)

    elif service == '4':
        cksa = input('Точка А: ').strip()
        cksb = input('Точка В: ').strip()
        cksrate = input('Скорость: ')
        ckspol = input('Маркировка: 1-sub/2-port: ')
        if ckspol == '1':
            result = cks.format(cksa=cksa, cksb=cksb, cksrate=cksrate, ckspolicing=ckspolicing[0], num=len(titles)+1)
        elif ckspol == '2':
            result = cks.format(cksa=cksa, cksb=cksb, cksrate=cksrate, ckspolicing=ckspolicing[1], num=len(titles)+1)
        title = result[:result.index('---')]
        titles.append(title)

    elif service == '5':
        #print(titles)
        vls_exist = input_text('Существующая ВЛС? ')
        if vls_exist in no:
            vls_name = input('Название ВЛС: ')
            vls_rate = input('Скорость: ')
            result = vls.format(num=len(titles)+1)
            title = result[:result.index('---')]
            titles.append(title)
            result2 = port_vls.format(num=len(titles)+1, vls_name=vls_name, vls_rate=vls_rate)
            title2 = result2[:result2.index('---')]
            titles.append(title2)
            title=title+title2
            result = result+'\n\n\n'+result2
        elif vls_exist in yes:
            vls_name = input('Название ВЛС: ')
            vls_rate = input('Скорость: ')
            result = port_vls.format(num=len(titles)+1, vls_name=vls_name, vls_rate=vls_rate)
            title = result[:result.index('---')]
            titles.append(title)
    return result, title, titles


serv = []
title_serv = []
kol = int(input('Количество услуг '))

for i in range(kol):
    usl, usl_tit, titles = service()
    serv.append(usl)
    title_serv.append(usl_tit)


sreda = input('Среда передачи(UTP-1,Fiber-2,Wi-Fi-3):  ')
pps = input('ППС: ')
pps = pps.strip()
kad = input('КАД: ')
kad = kad.strip()
if pps.startswith('АВ '):
    pass
else:
    pps ='АВ '+pps
if pps.endswith(', АВ'):
    pps = pps[:pps.index(', АВ')]
else:
    pass

def env():
    cswyn = 'w'
    csw100yn = 'w'
    if int(kol) == 1:
        if sreda == '1':
            result = med.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
            title = result[:result.index('-----')]
            titles.append(title)

        elif sreda == '2':
            idle = input_text('idle(y/n):  ')
            if idle in no:
                result = vols.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
                title = result[:result.index('-----')]
                titles.append(title)
            elif idle in yes:
                ppr = input('#ППР:  ')
                result = vols_idle.format(pps_idle=pps, kad_idle=kad, ppr_idle=ppr, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)
        elif sreda == '3':
            wireless = input('AP ')
            if wireless == 'i':
                title = infinet[:infinet.index('-----')]
                result = infinet.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                title = 'Стоимость оборудования Infinet H11 посчитана как "Прочее активное оборудование"\n\n' + title
                titles.append(title)
            elif wireless == 'u':
                result = ubi.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                title = 'Стоимость оборудования Nanostation M5 посчитана как "Прочее активное оборудование"\n\n' + title
                titles.append(title)
    else:
        quant = input('Количество линий от АВ ')
        if quant == '1':
            cswyn = input_text('Требуется ли CSW? ')

            if sreda == '1':
                result = med.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)

            elif sreda == '2' and cswyn in no:
                idle = input_text('idle(y/n):  ')
                if idle in no:
                    result = vols.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                    title = result[:result.index('-----')]
                    titles.append(title)
                elif idle in yes:
                    ppr = input('#ППР:  ')
                    result = vols_idle.format(pps_idle=pps, kad_idle=kad, ppr_idle=ppr, num=len(titles)+1)
                    title = result[:result.index('-----')]
                    titles.append(title)

            elif sreda == '2' and cswyn in yes:
                csw100yn = input_text('Магистраль на 100М? ')
                if csw100yn in yes:
                    result = vols_csw100.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
                    title = result[:result.index('-----')]
                    titles.append(title)
                elif csw100yn in no:
                    result = vols_csw1g.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
                    title = result[:result.index('-----')]
                    titles.append(title)
            elif sreda == '3':
                wireless = input('AP ')
                if wireless == 'i':
                    result = infinet.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                    title = result[:result.index('-----')]
                    title = 'Стоимость оборудования Infinet H11 посчитана как "Прочее активное оборудование"\n\n' + title
                    titles.append(title)
                elif wireless == 'u':
                    result = ubi.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                    title = result[:result.index('-----')]
                    title = 'Стоимость оборудования Nanostation M5 посчитана как "Прочее активное оборудование"\n\n' + title
                    titles.append(title)
        elif int(quant) == 2:
            if sreda == '1':
                result = med_two.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)
            elif sreda == '2':
                result = vols_two.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)
        else:
            pass
    csw_exist = 3
    csw_po = 0
    if cswyn in yes:
        csw_po = input('Количество линий от CSW: ')
        if csw100yn in no:
            csw_exist = 2
        else:
            csw_exist = 1
    else:
        pass
    return result, title, csw_exist, csw_po, titles


print('После услуг title_serv', title_serv)
print('После услуг titles', titles)
print('n')

line, title_line, csw_exist, csw_po, titles = env()

print('После линии title_serv', title_serv)
print('После линии titles', titles)
print('n')

def csw():
    if csw_exist == 2 and sreda == '2':
        result = CSW_1G.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
        title = result[:result.index('-----')]
        titles.append(title)
    elif csw_exist == 1 and sreda == '2':
        result = CSW_100M_O.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
        title = result[:result.index('-----')]
        titles.append(title)
    elif csw_exist == 1 and (sreda == '1' or sreda == '3'):
        result = CSW_100M_M.format(pps_l=pps, kad_l=kad, num=len(titles)-kol)
        title = result[:result.index('-----')]
        titles.append(title)
    else:
        result = []
        title = []
    return result, title, titles

def ports_csw(csw_exist, csw_po):
    if csw_exist == 1 or csw_exist == 2:
        result = csw_port_4.format(csw_po=csw_po, num=len(titles)-kol)
        title = result[:result.index('-----')]
        titles.append(title)
    else:
        result = []
        title = []
    return result, title, titles

#csw, csw_title, titles = csw()
#csw_port_4, title_csw_port_4, titles = ports_csw(csw_exist, csw_po)

'''for i in range(kol):
    usl, usl_tit, titles = service()
    serv.append(usl)
    title_serv.append(usl_tit)'''

csw, csw_title, titles = csw()
csw_port_4, title_csw_port_4, titles = ports_csw(csw_exist, csw_po)

print('После CSW titles', titles)
print('n')

print('\n\n')
print(title_line, end='')
if csw_exist == 1 or csw_exist == 2:
    print(csw_title, end='')
    print(title_csw_port_4, end='')
else:
    pass
for i in title_serv:
    print(i, end='')
print('\n')
print(line)
if csw_exist == 1 or csw_exist == 2:
    print('\n')
    print(csw)
    print('\n')
    print(csw_port_4)
else:
    pass
print('\n')
for i in serv:
    print(i, end='')
    print('\n')
