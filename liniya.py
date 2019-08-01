med = '''1. Присоединение к СПД по медной линии связи.
------------------------------------------------------------------------------------------

ОИПМ проведение работ:
- Организовать медную линию связи от {} до клиента.
- Подключить организованную линию для клиента в коммутатор {}, задействовать свободный порт.'''

vols = '''1. Присоединение к СПД по оптической линии связи.
------------------------------------------------------------------------------------------
 
xОИПМ проведение работ:
- Организовать ВОЛС от {} до клиента по решению ОАТТР.
- Установить на стороне АВ конвертер 1310 нм, выставить на конвертере режим работы 100 FD Force.
- Подключить организованную линию для клиента в коммутатор {}, порт задействовать свободный.
- Установить на стороне клиента конвертер 1550 нм, выставить на конвертере режим работы 100 FD Force.

ОНИТС СПД проведение работ:
- На порту подключения клиента выставить скоростной режим Auto.'''

vols_idle = '''1. Присоединение к СПД по оптической линии связи с простоем связи услуг.
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



infinet = '''1. Присоединение к СПД по беспроводной среде передачи данных.
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для выделения реквизитов беспроводных точек доступа WDS/WDA.
- Доставить в офис ОНИТС СПД беспроводные точки Infinet H11 для их настройки.


ОИПМ проведение работ:
После выполнения подготовительных работ в рамках заявки в Cordis и настройки точек в офисе ОНИТС СПД:
- Установить на стороне {} и на стороне клиента беспроводные точки доступа по решению ОАТТР. На АВ использовать для подключения беспроводной точки коммутатор {}, свободные порты есть.

ОНИТС СПД подготовиться к работам:
- По заявке в Cordis выделить реквизиты для управления беспроводными точками.
- Настроить беспроводные точки Infinet H11 в офисе.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ подключить к СПД и запустить беспроводные станции (WDS/WDA).'''


ubi = '''1. Присоединение к СПД по беспроводной среде передачи данных.
------------------------------------------------------------------------------------------

ОИПМ подготовиться к работам:
- Создать заявку в Cordis на ОНИТС СПД для выделения реквизитов беспроводных точек доступа WDS/WDA.

ОИПМ проведение работ:
После выполнения подготовительных работ в рамках заявки в Cordis на ОНИТС СПД:
- Установить на стороне {} и на стороне клиента беспроводные точки доступа по решению ОАТТР. На АВ использовать для подключения беспроводной точки коммутатор {}, свободные порты есть.

ОНИТС СПД подготовиться к работам:
- По заявке в Cordis выделить реквизиты для управления беспроводными точками.

ОНИТС СПД проведение работ:
- Совместно с ОИПМ подключить к СПД и запустить беспроводные станции WDS/WDA.'''


def env():
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


    if sreda == '1':
        result = med.format(pps, kad)
        title = med[:med.index('-----')]
    elif sreda == '2':
        idle = input('idle(y/n):  ')
        if idle == 'n':
            result = vols.format(pps, kad)
            title = vols[:vols.index('-----')]
        elif idle == 'y':
            ppr = input('#ППР:  ')
            result = vols_idle.format(pps_idle=pps, kad_idle=kad, ppr_idle=ppr)
            title = vols_idle[:vols_idle.index('-----')]
        else:
            pass
    elif sreda == '3':
        wireless = input('AP ')
        if wireless == 'i':
            title = infinet[:infinet.index('-----')]
            result = infinet.format(pps, kad)
            title = 'Стоимость оборудования Infinet H11 посчитана как "Прочее активное оборудование"\n\n' + title
        elif wireless == 'u':
            title = ubi[:ubi.index('-----')]
            result = ubi.format(pps, kad)
            title = 'Стоимость оборудования Nanostation M5 посчитана как "Прочее активное оборудование"\n\n' + title
    return result, title

line, title_line = env()

import services
usluga, title_usluga = services.service()

print('\n\n')
print(title_line, end='')
print(title_usluga)
print(line)
print('\n')
print(usluga)
print('\n')
