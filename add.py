import test_sss_parse as sss
import test_netswitch_parse as switch

med = '''{num}. Присоединение к СПД по медной линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать медную линию связи от {pps_l} до клиента.
- Подключить организованную линию для клиента в коммутатор {kad_l}, задействовать свободный порт.'''

med_two = '''{num}. Присоединение к СПД по медной линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать {quant} медных линии связи от {pps_l} до клиента.
- Подключить организованные линии для клиента в коммутатор {kad_l}, задействовать свободные порты.'''



vols = '''{num}. Присоединение к СПД по оптической линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {kad_l}, порт задействовать свободный.
- Установить на стороне клиента конвертер 1550 нм, выставить на конвертере режим работы 100 FD Force.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''

vols_two = '''{num}. Присоединение к СПД по оптической линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ {quant} конвертера 1310 нм, выставить на конвертерах режим работы 100 FD Force.
- Подключить организованные линии для клиента в коммутатор {kad_l}, порты задействовать свободные.
- Установить на стороне клиента {quant} конвертера 1550 нм, выставить на конвертерах режим работы 100 FD Force.

ОНИТС СПД проведение работ:
- На портах подключения клиента выставить скоростной режим Auto.'''


vols_idle = '''{num}. Присоединение к СПД по оптической линии связи с простоем связи услуг.
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


vols_csw100 = '''{num}. Присоединение к СПД по оптической линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {kad_l}, порт задействовать свободный.
- Установить на стороне клиента передатчик SFP WDM, дальность до 20 км (14dB), 1550 нм.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''


vols_csw1g = '''{num}. Присоединение к СПД по оптической линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {pps_l} до клиента по решению ОАТТР.
- Установить на стороне АВ передатчик SFP WDM, дальность до 20 км (12dB), 1310 нм.
- Подключить организованную линию для клиента в коммутатор {kad_l}, порт задействовать свободный.
- Установить на стороне клиента передатчик SFP WDM, дальность до 20 км (14dB), 1550 нм.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''


CSW_100M_M = '''{num}. Установка клиентского коммутатора.
------------------------------------------------------------------------------------------

МСРКБ:
- Проинформировать клиента о простое сервиса на время проведения работ.
- Согласовать время проведение работ.

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


CSW_100M_O = '''{num}. Установка клиентского коммутатора.
------------------------------------------------------------------------------------------

МСРКБ:
- Проинформировать клиента о простое сервиса на время проведения работ.
- Согласовать время проведение работ.

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для настройки клиентского коммутатора.
- Логическое подключение для клиентского коммутатора - {pps_l}, {kad_l}.

ОИПМ проведение работ:
- Установить в помещении клиента коммутатор D-Link DGS-1100-06/ME c оптическим передатчиком SFP WDM, дальность до 20 км (14dB), 1550 нм. Включить линию для клиента в Port 6 коммутатора D-Link DGS-1100-06/ME.
- Совместно с ОНИТС СПД запустить клиентский коммутатор.


ОНИТС СПД подготовиться к работам:
- В рамках заявки в Cordis подготовиться к установке клиентского коммутатора D-Link DGS-1100-06/ME.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ установить клиентский коммутатор.
- Передать информацию в ОУИ СПД.'''


CSW_1G = '''{num}. Установка клиентского коммутатора.
------------------------------------------------------------------------------------------

ВНИМАНИЕ!!!!!!!!!!!!!!!! ТРЕБУЕТСЯ УДАЛЕННАЯ НАСТРОЙКА КОММУТАТОРА D-Link DGS-1100-06/ME С ОНИТС СПД НА ЭТАПЕ ПОДГОТОВКИ К РАБОТАМ.


МСРКБ:
- Проинформировать клиента о простое сервиса на время проведения работ.
- Согласовать время проведение работ.

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для настройки клиентского коммутатора.
- Логическое подключение для клиентского коммутатора - {pps_l}, {kad_l}.
- Совместно с ОНИТС СПД удаленно настроить коммутатор D-Link DGS-1100-06/ME.

ОИПМ проведение работ:
- Установить на стороне {pps_l} оптический передатчик SFP WDM, дальность до 20 км (12dB), 1310 нм, задействовать свободный гигабитный порт.
- Переключить линию для клиента в установленный передатчик.
Старый порт: {client_port} коммутатора {kad_l}
Новый порт: свободный гигабитный порт коммутатора {kad_l}
- Установить в помещении клиента коммутатор D-Link DGS-1100-06/ME c оптическим передатчиком SFP WDM, дальность до 20 км (14dB), 1550 нм. Включить линию для клиента в Port 6 коммутатора D-Link DGS-1100-06/ME.
- Совместно с ОНИТС СПД запустить клиентский коммутатор на магистрали 1G.


ОНИТС СПД подготовиться к работам:
- В рамках заявки в Cordis подготовиться к установке клиентского коммутатора D-Link DGS-1100-06/ME.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ установить клиентский коммутатор.
- Передать информацию в ОУИ СПД.'''



csw_port_4 = '''{num}. Присоединение к клиентскому коммутатору по медной линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать {csw_po} медных линии от клиентского коммутатора до оборудования, установленного у клиента. Включить линии в порты:\n'''


infinet = '''{num}. Присоединение к СПД по беспроводной среде передачи данных.
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


ubi = '''{num}. Присоединение к СПД по беспроводной среде передачи данных.
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

shpd_access = '''{num}. Организация услуги ШПД в интернет access'ом.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской {mask}, в порт подключения выдать vlan access.
'''


shpd_trunk = '''{num}. Организация услуги ШПД в интернет trunk'ом.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу "Широкополосный доступ в интернет", использовать подсеть с маской /{mask}, согласовать с клиентом tag vlan, в порт подключения выдать vlan тегом.'''


gate_no = '''{num}. Организация услуги телефония.
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


gate_no_csw = '''{num}. Организация услуги телефония.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
1. Заблаговременно создать заявку на ОНИТС СПД для настройки шлюза. 
2. Установить в помещении клиента телефонный шлюз {mod}. Подключить лини{var_lin2} от порта КК в WAN порт тел. шлюза. 
3. Организовать {tel_lin} {var_lin_gate_yes_1} {kol_lin} Р{nu} тел. шлюза.

ОНИТС СПД проведение работ:
1. Совместно с ОИПМ установить телефонный шлюз.
2. Передать информацию в ОЭППО.

ОЭППО проведение работ:
1. Настроить {tel_lin}-канальный тел. номер.'''


gate_yes = '''{num}. Организация услуги телефония.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
Организовать {tel_lin} {kol_lin1} от тел. шлюза {mod} (установлен на АВ) до телефонного оборудования клиента. {kol_lin2} Р{nu} тел. шлюза.
 
ОЭППО проведение работ:
1. Настроить {tel_lin}-канальный тел. номер. '''

gate_sip = '''{num}. Организация услуги телефония
------------------------------------------------------------------------------------------

ОЭППО: Организовать 1-канальный телефонный номер с доступом с внешнего ip адреса.'''

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

cks = '''{num}. Организация услуги ЦКС Etherline access'ом
------------------------------------------------------------------------------------------
  
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу ЦКС {cksrate} "{cksa}", в порт подключения выдать vlan access.
- Ограничить скорость и настроить маркировку трафика для ЦКС {ckspolicing}.'''


vls = '''{num}. Организация услуги ВЛС
------------------------------------------------------------------------------------------
 
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу Виртуальная Локальная сеть.'''


port_vls = '''{num}. Организация услуги порт ВЛС access'ом
------------------------------------------------------------------------------------------
 
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу порт Виртуальной Локальной Сети для ВЛС {vls_name} с полосой {vls_rate} Мбит/с, в порт подключения выдать vlan access.'''

lvs2 = '''{num}. Установка маршрутизатора
------------------------------------------------------------------------------------------
 
ОИПМ/ОВИТС проведение работ:
- Установить в помещении клиента маршрутизатор или использовать существующий. Включить линию для клиента в Wan-порт маршрутизатора.
- Организовать {lvs_line} линии от маршрутизатора до оборудования установленного у клиента. Включить линии в свободные lan-порты.
- Настроить на маршрутизаторе NAT+DHCP для портов LAN.'''

lvs1 = '''{num}. Установка маршрутизатора
------------------------------------------------------------------------------------------

ОИПМ/ОВИТС проведение работ:
- Установить в помещении клиента маршрутизатор или использовать существующий. Включить линию для клиента в Wan-порт маршрутизатора.
- Организовать {lvs_line} линию от маршрутизатора до оборудования установленного у клиента. Включить линию в свободный lan-порт.
- Настроить на маршрутизаторе NAT+DHCP для портов LAN.'''


itv32 = '''{num}. Организация услуги Вебург.ТВ
------------------------------------------------------------------------------------------

ОИПМ/ОВИТС проведение работ:
- Установить в помещении клиента маршрутизатор или использовать существующий. Включить линию для клиента в Wan-порт маршрутизатора.
- Организовать 2 линии от маршрутизатора до оборудования установленного у клиента и приставки. Включить линии в свободные lan-порты.
- Настроить на маршрутизаторе NAT+DHCP для портов LAN.'''


itv30 = '''{num}. Организация услуги Вебург.ТВ в vlan'е новой услуги ШПД в интернет
-----------------------------------------------------------------------------------
  
ОНИТС СПД проведение работ:
- По заявке в Cordis настроить SVI клиента, организованный по решению выше, на приём трафика multicast.
- Если в цепочке между АМ и КАД имеется КПА Cisco 3550 необходимо настроить MVR.

ОИПМ/ОВИТС проведение работ:
- Установить в помещении клиента маршрутизатор или использовать существующий. Включить линию для клиента в Wan-порт маршрутизатора.
- Организовать 2 линии от маршрутизатора до оборудования установленного у клиента и приставки. Включить линии в свободные lan-порты.
- Настроить на маршрутизаторе NAT+DHCP для портов LAN.'''


itv_vlan_one = '''{num}. Организация услуги Вебург.ТВ в отдельном vlan'е
-----------------------------------------------------------------------------------
  
ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу Вебург.ТВ, использовать серую подсеть с маской {mask}, в порт подключения выдать vlan access.
- Если в цепочке между АМ и КАД имеется КПА Cisco 3550 необходимо настроить MVR.'''


itv_vlan_any = '''{num}. Организация услуги Вебург.ТВ в отдельном vlan'е
-----------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis организовать клиенту услугу Вебург.ТВ, использовать серую подсеть с маской {mask}, в порты подключения выдать vlan access.
- Если в цепочке между АМ и КАД имеется КПА Cisco 3550 необходимо настроить MVR.'''


passage = '''{num}. Перенос сервиса {service}{sub}.
------------------------------------------------------------------------------------------

ОНИТС СПД проведение работ:
- По заявке в Cordis на установку клиентского коммутатора перенести сервис {service}{rek1}"{client_subnet}" с КАД на клиентский коммутатор, установленный по решению выше.
- Убедиться в восстановлении сервиса {service} у клиента.
- актуализировать информацию в Cordis'''


var_lin = ('телефонную линию от АВ до телефонного оборудования клиента. Включить линию через кросс в порт', 'телефонные линии от АВ до телефонного оборудования клиента. Включить линии через кросс в порты', 'телефонных линий от АВ до телефонного оборудования клиента. Включить линии через кросс в порты')
var_lin2 = ('ю', 'и')
var_lin_gate_yes_1 = ('телефонную линию', 'телефонные линии', 'телефонных линий')
var_lin_gate_yes_2 = ('Включить линию через кросс в порт', 'Включить линии через кросс в порты')
var_lin_gate_csw = ('от тел. шлюза до телефонного оборудования клиента. Включить линию в свободный порт', 'от тел. шлюза до телефонного оборудования клиента. Включить линии в свободные порты')
hotspot_name = ('Стандарт', 'Премиум')
hotspot_st1 = ('ую', 'ые')
hotspot_st2 = ('ию', 'ии')
hotspot_st3 = ('ей', 'ями')
hotspot_model = ('D-Link DIR-300', 'Ubiquiti UniFi')
ckspolicing = ('полисером Subinterface', 'портом подключения')
condition = ['y', 'n', 'н', 'т']
yes = ['y', 'н']
no = ['n', 'т']

titles = []  #используется для подстановки в num
csw_ports_tag = []

def input_text(question):
    '''Функция используется для вопросов с ответами да/нет.
       Принимает текст вопроса, проверяет совпадение введенного ответа с символами д, н, y, n, и возвращает введенный корректный символ'''
    while True:
        input_t = input(question)
        if input_t in condition:
            break
        else:
            print('Incorrect enter.\n')
    return input_t


def service(serv_des, sservices):
    
    if 'Интернет' in serv_des:
        masks = ['/29', '/28', '/ 29', '/ 28']
        if 'Интернет, DHCP' in serv_des:
            result = shpd_access.format(mask='/32', num=len(titles)+1)
            title = result[:result.index('---')]
            titles.append(title)
        #elif access == 't':

        else:
            for mas in masks:
                if mas in serv_des:
                    result = shpd_access.format(mask=mas, num=len(titles)+1)
                    break
                else:
                    result = shpd_access.format(mask='/30', num=len(titles)+1)

            title = result[:result.index('---')]
            titles.append(title)
        csw_ports_tag.append('ШПД в интернет')

    elif 'Телефон' in serv_des:
        analog = input_text('Аналог? ')
        if analog in yes:
            if cswyn in no:
                gate = input_text('Требуется установка шлюза? ')
                if gate in yes:
                    model = input('Модель: ')
                    linii = input('Количество линий ')
                    number_port = input('Порты на шлюзе ')
                    if int(linii) == 1:
                        result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[0], nu=number_port, chis=var_lin2[0], num=len(titles)+1)
                    elif 2 <= int(linii) <=4:
                        result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[1], nu=number_port, chis=var_lin2[1], num=len(titles)+1)
                    else:
                        result = gate_no.format(mod=model, tel_lin=linii, kol_lin=var_lin[2], nu=number_port, chis=var_lin2[1], num=len(titles)+1)
                    title = result[:result.index('---')]

                elif gate in no:
                    model = input('Модель: ')
                    linii = input('Количество линий ')
                    number_port = input('Порты на шлюзе ')
                    if int(linii) == 1:
                        result = gate_yes.format(mod=model, tel_lin=linii, kol_lin1=var_lin_gate_yes_1[0], nu=number_port, kol_lin2=var_lin_gate_yes_2[0], num=len(titles)+1)
                    elif 2 <= int(linii) <=4:
                        result = gate_yes.format(mod=model, tel_lin=linii, kol_lin1=var_lin_gate_yes_1[1], nu=number_port, kol_lin2=var_lin_gate_yes_2[1], num=len(titles)+1)
                    else:
                        result = gate_yes.format(mod=model, tel_lin=linii, kol_lin1=var_lin_gate_yes_1[2], nu=number_port, kol_lin2=var_lin_gate_yes_2[1], num=len(titles)+1)
                    title = result[:result.index('---')]
            elif cswyn in yes:
                model = input('Модель: ')
                linii = input('Количество линий ')
                number_port = input('Порты на шлюзе ')
                if int(linii) == 1:
                    result = gate_no_csw.format(mod=model, tel_lin=linii, kol_lin=var_lin_gate_csw[0], var_lin_gate_yes_1=var_lin_gate_yes_1[0],  var_lin2=var_lin2[0],  nu=number_port, num=len(titles)+1)
                elif 2 <= int(linii) <=4:
                    result = gate_no_csw.format(mod=model, tel_lin=linii, kol_lin=var_lin_gate_csw[1], var_lin_gate_yes_1=var_lin_gate_yes_1[1], var_lin2=var_lin2[1], nu=number_port, num=len(titles)+1)
                else:
                    result = gate_no_csw.format(mod=model, tel_lin=linii, kol_lin=var_lin_gate_csw[1], var_lin_gate_yes_1=var_lin_gate_yes_1[2], nu=number_port, var_lin2=var_lin2[1],  num=len(titles)+1)
                title = result[:result.index('---')]
                csw_ports_tag.append('Телефония')
        elif analog in no:
            result = gate_sip.format(num=len(titles)+1)
            title = result[:result.index('---')]

    elif 'ЛВС' in serv_des:
        lvs_line = input('Количество линий от маршрутизатора: ')
        if lvs_line == '1':
            result = lvs1.format(lvs_line=lvs_line, num=len(titles)+1)
        else:
            result = lvs1.format(lvs_line=lvs_line, num=len(titles)+1)
        title = result[:result.index('---')]
        titles.append(title)

    elif 'HotSpot' in serv_des:
        hotspot_client = input('Количество клиентов Хот-спот: ')
        hotspot_kol = input('Количество точек Хот-спот: ')
        if 'стандарт' in serv_des.lower() and hotspot_kol == '1':
            result = hot_spot.format(hot_name=hotspot_name[0], hot_mod=hotspot_model[0], hot_st1=hotspot_st1[0], hot_st2=hotspot_st2[0], hot_st3=hotspot_st3[0], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        elif 'стандарт' in serv_des.lower() and int(hotspot_kol) > 1:
            result = hot_spot.format(hot_name=hotspot_name[0], hot_mod=hotspot_model[0], hot_st1=hotspot_st1[1], hot_st2=hotspot_st2[1], hot_st3=hotspot_st3[1], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        elif 'премиум' in serv_des.lower() and hotspot_kol == '1':
            result = hot_spot.format(hot_name=hotspot_name[1], hot_mod=hotspot_model[1], hot_st1=hotspot_st1[0], hot_st2=hotspot_st2[0], hot_st3=hotspot_st3[0], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        elif 'премиум' in serv_des.lower() and int(hotspot_kol) > 1:
            result = hot_spot.format(hot_name=hotspot_name[1], hot_mod=hotspot_model[1], hot_st1=hotspot_st1[1], hot_st2=hotspot_st2[1], hot_st3=hotspot_st3[1], hot_client=hotspot_client, hot_kol=hotspot_kol, num=len(titles)+1)
        title = result[:result.index('---')]
        titles.append(title)
        csw_ports_tag.append('Хот-спот')

    elif 'ЦКС' in serv_des:
        list_strok = sss.match_cks(tochka)
        if len(list_strok) == 1:
            cksa = list_strok[0]
        else:
            for i in range(len(list_strok)):
                print('{}'.format(list_strok[i]))
            cksa = input('Точка А - Точка В: ').strip()
        if '1000' in serv_des:
            cksrate = '1 Гбит/с'
        elif '100' in serv_des:
            cksrate = '100 Мбит/с'
        elif '10' in serv_des:
            cksrate = '10 Мбит/с'
        elif '1' in serv_des:
            cksrate = '1 Гбит/с'
        else:
            cksrate = input('Скорость: ')
        ckspol = input('Маркировка: 1-sub/2-port: ')
        if ckspol == '1':
            result = cks.format(cksa=cksa, cksrate=cksrate, ckspolicing=ckspolicing[0], num=len(titles)+1)
        elif ckspol == '2':
            result = cks.format(cksa=cksa, cksrate=cksrate, ckspolicing=ckspolicing[1], num=len(titles)+1)
        title = result[:result.index('---')]
        titles.append(title)
        csw_ports_tag.append('ЦКС')

    elif 'iTV' in serv_des:
        if 'Интернет, DHCP' in sservices:
            result = itv32.format(num=len(titles)+1)
        elif 'Интернет, блок Адресов Сети Интернет' in sservices:
            marsh = input('iTV через марш? ')
            if marsh in yes:
                result = itv30.format(num=len(titles)+1)
            elif marsh in no:
                kol_itv = input('Количество приставок: ')
                if kol_itv == '1':
                    result = itv_vlan_one.format(num=len(titles)+1, mask='/30')
                    csw_ports_tag.append('Вебург.ТВ')
                else:
                    result = itv_vlan_any.format(num=len(titles)+1, mask='/29')
                    for i in range(int(kol_itv)):
                        csw_ports_tag.append('Вебург.ТВ')
        else:
            kol_itv = input('Количество приставок: ')
            if kol_itv == '1':
                result = itv_vlan_one.format(num=len(titles)+1, mask='/30')
                csw_ports_tag.append('Вебург.ТВ')
            else:
                result = itv_vlan_any.format(num=len(titles)+1, mask='/29')
                for i in range(int(kol_itv)):
                    csw_ports_tag.append('Вебург.ТВ')
        title = result[:result.index('---')]
        titles.append(title)

    elif 'ВЛС' in serv_des:
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
        csw_ports_tag.append('порт ВЛС')
    else:
        result = passage.format(num=len(titles)+1, service=client_service[client_serv][0], rek1=client_service[client_serv][1], client_subnet=client_subnet, sub=client_service[client_serv][2])
        title = result[:result.index('---')]
        titles.append(title)
        csw_ports_tag.append(client_service[client_serv][0])
    return result, title, titles, csw_ports_tag

sservices_full, sservices, new_AB, turnoff, sreda, tochka = sss.matching(sss.input_TR()) # sservices - поле услуга. sservices_full - поле услуга+описание.

client = input('Данные клиента: ')

client_list = client.split('	')
client_name = client_list[0]+' '+client_list[1]
client_address = client_list[4]
client_subnet = client_list[6]
client_serv = client_list[3]
client_kad = client_list[8]
client_port = client_list[9]

if 'vrf' in (client_list[6].lower() or client_list[7].lower()):
    client_serv = 'Порт виртуального маршрутизатора'

client_service = {'IP-адрес или подсеть':['"ШПД в интернет"', ' c реквизитами ', ' с маской '+client_subnet[-3:]+' '],
           'Порт виртуального коммутатора':['Порт ВЛС', ' ', ' '],
           'Порт виртуального маршрутизатора':['Порт ВМ', ' ', ' '],
           'Etherline':['ЦКС', ' ', ' ']}

data_client = 'Клиент {client_name} в точке подключения {client_address} подключен от {new_AB}, коммутатор {client_kad}, порт {client_port} и потребляет услугу {client_service}{rek1}"{client_subnet}".'.format(client_name=client_name, client_address=client_address, client_kad=client_kad, client_port=client_port, client_subnet=client_subnet, new_AB=new_AB, client_service=client_service[client_serv][0], rek1=client_service[client_serv][1])
sservices_full.append(client_serv)
sservices.append(client_serv)

for i in sservices_full:
    if 'ЦКС' in i:
        sservices_full.pop(sservices_full.index(i))
        sservices_full.append(i)
    elif 'HotSpot' in i:
        sservices_full.pop(sservices_full.index(i))
        sservices_full.append(i)
    elif 'iTV' in i:
        sservices_full.pop(sservices_full.index(i))
        sservices_full.append(i)
    elif 'ЛВС' in i:
        sservices_full.pop(sservices_full.index(i))
        sservices_full.append(i)
    elif 'Телефон' in i:
        sservices_full.pop(sservices_full.index(i))
        sservices_full.append(i)

print(sservices_full, sservices, new_AB, turnoff, sreda)

serv = []
title_serv = []
kol = len(sservices)    #Количество услуг

pps = new_AB
pps = pps.strip()


if pps.startswith('АВ '):
    pass
else:
    pps ='АВ '+pps
if pps.endswith(', АВ'):
    pps = pps[:pps.index(', АВ')]
else:
    pass

list_kad = []
list_switches = switch.parsingByNodename(new_AB)
if len(list_switches) == 1:
    kad = list_switches[0][0]
else:
    for i in range(len(list_switches)):
        if (list_switches[i][0].startswith('IAS')) or (list_switches[i][0].startswith('AR')):
            pass
        else:
            list_kad.append(list_switches[i][0])
    kad = ' или '.join(list_kad)


def env(turnoff):
    cswyn = 'n'
    csw100yn = 'w'
    if int(kol) == 1:
        if sreda == '1':
            result = med.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
            title = result[:result.index('-----')]
            titles.append(title)

        elif sreda == '2':
            if turnoff is False:
                result = vols.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)
            elif turnoff is True:
                ppr = input('#ППР:  ')
                result = vols_idle.format(pps_idle=pps, kad_idle=kad, ppr_idle=ppr, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)
        elif sreda == '3':
            wireless = input('AP infinet-i, ubiquity-u: ')
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
                    result = vols_csw100.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
                    title = result[:result.index('-----')]
                    titles.append(title)
                elif csw100yn in no:
                    result = vols_csw1g.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
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
        elif int(quant) > 1:
            if sreda == '1':
                result = med_two.format(quant=quant, pps_l=pps, kad_l=kad, num=len(titles)+1)
                title = result[:result.index('-----')]
                titles.append(title)
            elif sreda == '2':
                result = vols_two.format(quant=quant, pps_l=pps, kad_l=kad, num=len(titles)+1)
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
    return result, title, csw_exist, csw_po, titles, cswyn

def csw():
    if csw_exist == 2 and sreda == '2':
        result = CSW_1G.format(pps_l=pps, kad_l=kad, num=len(titles)+1, client_port=client_port)
        title = result[:result.index('-----')]
        titles.append(title)
    elif csw_exist == 1 and sreda == '2':
        result = CSW_100M_O.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
        title = result[:result.index('-----')]
        titles.append(title)
    elif csw_exist == 1 and (sreda == '1' or sreda == '3'):
        result = CSW_100M_M.format(pps_l=pps, kad_l=kad, num=len(titles)+1)
        title = result[:result.index('-----')]
        titles.append(title)
    else:
        result = []
        title = []
    return result, title, titles

def ports_csw(csw_exist, csw_po):
    if csw_exist == 1 or csw_exist == 2:
        result = csw_port_4.format(csw_po=csw_po, num=len(titles)+1)
        title = result[:result.index('-----')]
        titles.append(title)
    else:
        result = []
        title = []
    return result, title, titles

if len(sservices) == 1 and sservices[0] == 'Телефон':
    cswyn = 'n'
    csw_exist = 3
    outline = True
else:
    line, title_line, csw_exist, csw_po, titles, cswyn = env(turnoff)    #cswyn вытаскиваем, чтобы добавить в функцию с телефонией
    csw, csw_title, titles = csw()
    csw_port_4, title_csw_port_4, titles = ports_csw(csw_exist, csw_po)
    outline = False

for i in range(len(sservices)):
    usl, usl_tit, titles, csw_ports_tag = service(sservices_full[i], sservices)
    serv.append(usl)
    title_serv.append(usl_tit)


res_tag = []
print(csw_ports_tag)
for tag in range(len(csw_ports_tag)):
    res_tag.append('Port {numb} - "{tag}"'.format(numb=tag+1, tag=csw_ports_tag[tag]))

print('\n\n')

print(data_client)
print('\n\n')

if outline:
    pass
else:
    print(title_line, end='')

if csw_exist == 1 or csw_exist == 2:
    print(csw_title, end='')
    print(title_csw_port_4, end='')

for i in title_serv:
    print(i, end='')

print('\n')

if outline:
    pass
else:
    print(line)

if csw_exist == 1 or csw_exist == 2:
    print('\n')
    print(csw)
    print('\n')
    print(csw_port_4+'\n'.join(res_tag))
else:
    pass
print('\n')
for i in serv:
    print(i, end='')
    print('\n')
