no_log_con_med = '''Перенос сервиса {service}{sub}без смены логического подключения на КАД
-----------------------------------------------------------------------------------------------------------------------------------

МСРКБ:
1. Проинформировать клиента о простое сервиса на время проведения работ по переносу сервиса.
2. Согласовать время проведение работ.
3. Создать заявку в Cordis на ОНИТС СПД для переноса сервиса {service}{rek1}"{client_subnet}".

ОИПМ проведение работ:
1. Медную линию связи от {AB_last} нарастить до новой точки подключения клиента по решению ОАТТР.
2. Логическое подключение клиента не изменится.
3. Подтвердить окончание проведения работ в ОНИТС СПД.

ОНИТС СПД проведение работ:
1. По заявке в Cordis сопроводить работы ОИПМ по перенесу сервиса {service}{rek1}"{client_subnet}" для клиента в новую точку подключения.
2. Убедиться в восстановлении сервиса у клиента.'''


no_log_con_vols = '''Перенос сервиса {service}{sub}без смены логического подключения на КАД
---------------------------------------------------------------------------------------------------------------------------

МСРКБ:
1. Проинформировать клиента о простое сервиса на время проведения работ по переносу сервиса.
2. Согласовать время проведение работ.
3. Создать заявку в Cordis на ОНИТС СПД для переноса сервиса {service}{rek1}"{client_subnet}".

ОИПМ проведение работ:
1. Организовать ВОЛС от {AB_last} до новой точки подключения клиента по решению ОАТТР.
2. Логическое подключение клиента не изменится.
3. Подтвердить окончание проведения работ в ОНИТС СПД.

ОНИТС СПД проведение работ:
1. По заявке в Cordis сопроводить работы ОИПМ по перенесу сервиса {service}{rek1}"{client_subnet}" для клиента в новую точку подключения.
2. Убедиться в восстановлении сервиса у клиента.'''



log_con_kad_med = '''Перенос сервиса {service}{sub} со сменой логического подключения на КАД
-----------------------------------------------------------------------------------------------------------------------------------

МСРКБ:
1. Проинформировать клиента о простое сервиса на время проведения работ по переносу сервиса.
2. Согласовать время проведение работ.
3. Создать заявку в Cordis на ОНИТС СПД для переноса сервиса {service}{rek1}"{client_subnet}". В заявке Cordis указать время проведения работ по переносу сервиса.

ОИПМ:
1. Организовать медную линию связи от {AB_last} до новой точки подключения клиента по решению ОАТТР.
2. Подключить организованную линию связи в коммутатор {kad}, порт выбрать совместно с ОНИТС СПД.
3. Совместно с ОНИТС СПД протестировать новую линию связи.
4. Подтвердить окончание проведения работ по монтажу линии.

ОНИТС СПД:
1. По заявке в Cordis:
- подготовить настройки на оборудовании к переносу сервиса {service}{rek1}"{client_subnet}";
- перенести сервис {service}{rek1}"{client_subnet}" для клиента в новую точку подключения.
2. После переезда клиента актуализировать информацию в Cordis и системах учета.
3. Сообщить в ОЛИ СПД об освободившемся порте на коммутаторе {kad} после переезда клиента.'''


client_1G_temp = '''Переключение клиента на 1 Гбит/с
------------------------------------------------------------------------------------------

МСРКБ:
- Проинформировать клиента о простое сервиса на время проведения работ.
- Согласовать время проведение работ.
- Создать заявку в Cordis на ОНИТС СПД для переключения клиента.
- После переключения клиента увеличить скорость услуги ШПД в интернет до {speed} Мбит/с.


ОИПМ проведение работ:
- Организовать ВОЛС от {AB_last} до клиента по решению ОАТТР.
- Установить на стороне АВ оптический передатчик SFP WDM, дальность до 20 км (12dB), 1310 нм.
- Подключить организованную линию для клиента в порт Ethernet{port_new} коммутатора {kad}.
Старый порт: {client_port} коммутатора {kad}.
Новый порт: Ethernet{port_new} коммутатора {kad}.
- Установить на стороне клиента конвертер SNR-CVT-1000SFP-V2 с модулем SFP WDM, дальность до 20 км (14dB), 1550 нм. Выставить на конвертере режим работы Switch.
- Совместно с ОНИТС СПД протестировать новую линию связи.
- Подтвердить окончание проведения работ по монтажу линии.


ОНИТС СПД проведение работ:
1. По заявке в Cordis:
- подготовить настройки на оборудовании к переносу сервиса {service}{rek1}"{client_subnet}";
- перенести логическое подключение сервиса {service}{rek1}"{client_subnet}".
2. Актуализировать информацию в Cordis и системах учета.
3. Сообщить в ОЛИ СПД об освободившемся порте на коммутаторе {kad} после переключения клиента.'''


log_con_address_temp = '''2. Перенос сервиса {service}{sub}
------------------------------------------------------------------------------------------

МСРКБ:
- Проинформировать клиента о простое сервиса на время проведения работ по переносу сервиса.
- Согласовать время проведение работ.
- Создать заявку в Cordis на ОНИТС СПД для переноса сервиса {service}{rek1}"{client_subnet}". В заявке Cordis указать время проведения работ по переносу сервиса.


ОНИТС СПД проведение работ:
- По заявке в Cordis:
 - подготовить настройки на оборудовании к переносу сервиса {service}{rek1}"{client_subnet}";
 - перенести сервис {service}{rek1}"{client_subnet}" для клиента в новую точку подключения.
- После переезда клиента актуализировать информацию в Cordis и системах учета.
- Сообщить в ОЛИ СПД об освободившемся порте на коммутаторе {kad} после переезда клиента.'''


log_con_32_temp = '''2. Перенос сервиса {service}{sub}
------------------------------------------------------------------------------------------

МСРКБ:
- Согласовать с клиентом:
- необходимость смены реквизитов;
- необходимость перерыва связи на время проведения работ.
- Создать заявку на ОНИТС СПД для смены реквизитов.


ОНИТС СПД подготовиться к работам:
- По заявке в Cordis выделить подсеть с маской /32.
- Логическое подключение клиента изменится.

ОНИТС СПД проведение работ:
- По согласованию с клиентом сменить реквизиты на новую подсеть с маской /32.
- Убедиться в восстановлении связи у клиента.
- После смены реквизитов:
- разобрать ресурс {client_subnet} на договоре.
- актуализировать информацию в системах учета.
- Сообщить в ОЛИ СПД об освободившемся порте на коммутаторе {kad} после переезда клиента.'''


med_temp = '''1. Присоединение к СПД по медной линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ.
- Организовать медную линию связи от {AB_new} до клиента.
- Подключить организованную линию для клиента в коммутатор {kad_new}, задействовать свободный порт.
'''


vols_temp = '''1. Присоединение к СПД по оптической линии связи
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать ВОЛС от {AB_new} до клиента по решению ОАТТР.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {kad_new}, порт задействовать свободный.
- Установить на стороне клиента конвертер 1550 нм, выставить на конвертере режим работы 100 FD Force.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.
'''




client = input('Данные клиента: ')

client_list = client.split('	')
client_name = client_list[0]+' '+client_list[1]
client_address = client_list[4]
client_subnet = client_list[6]
client_serv = client_list[3]
client_kad = client_list[8]
client_port = client_list[9]

def clear_AB(AB):
    AB = AB.strip()
    if AB.startswith('АВ '):
        pass
    else:
        AB = 'АВ '+AB
    if AB.endswith(', АВ'):
        AB = AB[:AB.index(', АВ')]
    else:
        pass
    return AB


if 'vrf' in (client_list[6].lower() or client_list[7].lower()):
    client_serv = 'Порт виртуального маршрутизатора'

service = {'IP-адрес или подсеть':['"ШПД в интернет"', ' c реквизитами ', ' с маской '+client_subnet[-3:]+' '],
           'Порт виртуального коммутатора':['Порт ВЛС', ' ', ' '],
           'Порт виртуального маршрутизатора':['Порт ВМ', ' ', ' '],
           'Etherline':['ЦКС', ' ', ' ']}

AB_last = clear_AB(input('АВ от которого включен клиент: '))


data_client = 'Клиент {client_name} в точке подключения {client_address} подключен от {AB_last}, коммутатор {client_kad}, порт {client_port} и потребляет услугу {service}{rek1}"{client_subnet}".'.format(client_name=client_name, client_address=client_address, client_kad=client_kad, client_port=client_port, client_subnet=client_subnet, AB_last=AB_last, service=service[client_serv][0], rek1=service[client_serv][1])

new_address = ['в пределах здания', 'на адрес']
move = input('1-в пределах здания, 2-новый адрес, 3-переключение на 1G: ')

if move=='1':
    kuda = 'Требуется перенести точку подключения клиента {}.'.format(new_address[0])
    env = input('1-Медь, 2-Оптика: ')
    if env == '1':
        log_con = input('1-Без смены порта, 2-со сменой порта: ')
        if log_con == '1':
            total = no_log_con_med.format(service=service[client_serv][0], AB_last=AB_last, rek1=service[client_serv][1], client_subnet=client_subnet, sub=service[client_serv][2])
        elif log_con == '2':
            total = log_con_kad_med.format(service=service[client_serv][0], AB_last=AB_last, rek1=service[client_serv][1], client_subnet=client_subnet, sub=service[client_serv][2], kad=client_kad)
    elif env == '2':
        total = no_log_con_vols.format(service=service[client_serv][0], AB_last=AB_last, rek1=service[client_serv][1], client_subnet=client_subnet, sub=service[client_serv][2])
elif move=='2':
    address = input('Новый адрес: ').strip()
    kuda = 'Требуется перенести точку подключения клиента {}'.format(new_address[1])+' '+address+'.'

    env = input('1-Медь, 2-Оптика: ')
    if env == '1':
        AB_new = clear_AB(input('Новый АВ: '))
        kad_new = input('Новый КАД: ').strip()
        med = med_temp.format(AB_new=AB_new, kad_new=kad_new)
        title_med = med[:med.index('---')]
        if client_subnet[-3:] == '/32':
            log_con_32 = log_con_32_temp.format(kad=client_kad, client_subnet=client_subnet, service=service[client_serv][0], sub=service[client_serv][2])
            title_log_con_32 = log_con_32[:log_con_32.index('---')]
            total = title_med+title_log_con_32+'\n\n'+med+'\n\n'+log_con_32
        else:
            log_con_address = log_con_address_temp.format(service=service[client_serv][0], rek1=service[client_serv][1], client_subnet=client_subnet, sub=service[client_serv][2], kad=client_kad)
            title_log_con_address = log_con_address[:log_con_address.index('---')]
            total = title_med+title_log_con_address+'\n\n'+med+'\n\n'+log_con_address
    elif env == '2':
        AB_new = clear_AB(input('Новый АВ: '))
        kad_new = input('Новый КАД: ').strip()
        vols = vols_temp.format(AB_new=AB_new, kad_new=kad_new)
        title_vols = vols[:vols.index('---')]
        if client_subnet[-3:] == '/32':
            log_con_32 = log_con_32_temp.format(kad=client_kad ,client_subnet=client_subnet, service=service[client_serv][0], sub=service[client_serv][2])
            title_log_con_32 = log_con_32[:log_con_32.index('---')]
            total = title_vols+title_log_con_32+'\n\n'+vols+'\n\n'+log_con_32
        else:
            log_con_address = log_con_address_temp.format(service=service[client_serv][0], rek1=service[client_serv][1], client_subnet=client_subnet, sub=service[client_serv][2], kad=client_kad)
            title_log_con_address = log_con_address[:log_con_address.index('---')]
            total = title_vols+title_log_con_address+'\n\n'+vols+'\n\n'+log_con_address
elif move == '3':
    speed = input('Новая скорость: ').strip()
    port_new = input('Новый порт: ').strip()
    total = client_1G_temp.format(service=service[client_serv][0], rek1=service[client_serv][1], kad=client_kad, AB_last=AB_last, speed=speed, port_new=port_new, client_port=client_port, client_subnet=client_subnet)
    kuda = 'Требуется в данной точке увеличить скорость ШПД до {} Мбит/с.'.format(speed)


print('\n'*2)
print(data_client)
print('\n')
print(kuda)
print('\n')
print(total)
print('\n'*2)

