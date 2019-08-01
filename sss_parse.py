from requests.auth import HTTPBasicAuth
import requests
import re

def request_sss(url):
    url = url.replace('dem_begin', 'dem_point')
    req = requests.get(url, verify=False, auth=HTTPBasicAuth('pankov.dmitriy', 'WoW098Nerulit'))
    return req.content.decode('utf-8')


def input_TR():
    url = input('Input TR: ')
    parsed = request_sss(url)
    return parsed

def matching(parsed):
    sservices_full = []
    sservices = []
    regex_serv = "Service_ID_\d+\'\>\r\n(?:\t)+<TD>(.+)</TD>\r\n(?:\t)+<TD>(.+)</TD>"
    for service in re.finditer(regex_serv, parsed):
        if service.group(1) == 'Сопровождение ИС' or service.group(1) == 'Другое':
            pass
        elif 'Телефон' in sservices:
            serv_plus_des = ' '.join(service.groups())
            for i in range(len(sservices_full)):
                if 'Телефон' in sservices_full[i]:
                    sservices_full[i]=sservices_full[i]+serv_plus_des
                else:
                    pass
        else:
            serv_plus_des = ' '.join(service.groups())
            sservices.append(service.group(1))
            sservices_full.append(serv_plus_des)

    print('\n'*2)
    for item in sservices_full:
        print(item)  #('Услуга: {}.   Примечание{}'.format(item[0], item[1]))

    match_AB = None
    regex_AB = 'Изменить</span></div>\r\n</td>\r\n<td colspan="2">\r\n\t(.+) &'
    match_AB = re.search(regex_AB, parsed)
    if match_AB is None:
        regex_AB = 'Изменить</a></div>\r\n</td>\r\n<td colspan="2">\r\n\t(.+) &'
        match_AB = re.search(regex_AB, parsed)
    new_AB = match_AB.group(1)
    print(new_AB)

    match_turnoff = None
    regex_turnoff = 'INPUT  disabled=\'disabled\' id=\'trTurnOff'
    match_turnoff = re.search(regex_turnoff, parsed)
    if match_turnoff is None:
        turnoff = True
        print('Требуется отключение')
    else:
        turnoff = False
        print('Отключение не требуется')
    print(turnoff)

    regex_env = 'Время на реализацию, дней</td>\r\n<td colspan="2">\d</td>\r\n</tr>\r\n\r\n\r\n\r\n\r\n\r\n<tr av_req="1">\r\n<td colspan="3" align="left">\r\n(.+)</td>\r\n</tr>\r\n\r\n\r\n\r\n<tr obt_req'
    match_env = re.search(regex_env, parsed, flags=re.DOTALL)
    try:
        oattr = match_env.group(1)
        print(oattr)
        wireless = ['инжектор', 'радиомаршрутизатор', 'радиоканал', 'точку доступа']
        vols = ['ОВ', 'ОК']
    
        #if (not 'ОК' in oattr) and ((i in wireless) in oattr):
        if ((not 'ОК' in oattr) and ('инжектор' in oattr)) or ((not 'ОК' in oattr) and ('точку доступа' in oattr)) or ((not 'ОК' in oattr) and ('радиомаршрутизатор' in oattr)) or ((not 'ОК' in oattr) and ('радиоканал' in oattr)):
            sreda = '3'
            print('Беспроводная среда')
            #break
        elif 'UTP от АВ' in oattr:
            sreda = '1'
            print('UTP')
        elif ('ОВ' in oattr) or ('ОК' in oattr) or ('ВОЛС' in oattr):
            sreda = '2'
            print('ВОЛС')
        else:
            sreda = '1'
            print('UTP')
    except AttributeError:
        sreda = '1'
        print('UTP')

    return sservices_full, sservices, new_AB, turnoff, sreda

if __name__ == '__main__':
    matching(input_TR())
