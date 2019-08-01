from requests.auth import HTTPBasicAuth
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def parsingByNodename(node_name):
    url = 'https://cis.corp.itmh.ru/stu/NetSwitch/SearchNetSwitchProxy'
    data = {'IncludeDeleted': 'false', 'IncludeDisabled': 'true', 'HideFilterPane': 'false'}
    data['NodeName'] = node_name.encode('utf-8')
    req = requests.post(url, verify=False, auth=HTTPBasicAuth('pankov.dmitriy', 'WoW098Nerulit'), data=data)
    switch = req.content.decode('utf-8')


    regex_name_model = '\"netswitch-name\\\\\" >\\\\r\\\\n\s+?(\S+?[ekb|ntg|kur])\\\\r\\\\n\s+?</a>\\\\r\\\\n\s+?\\\\r\\\\n</td><td>(.+?)</td><td>\\\\r\\\\n\s+?<a href=\\\\\"/stu/Node'
    match_name_model = re.findall(regex_name_model, switch)
    # в regex добавлены знаки ?, чтобы отключить жадность. в выводе match список кортежей 

    regex_node = 'netswitch-nodeName\\\\\">\\\\r\\\\n\s+(.+?[АВ|КК|УА|РУА])\\\\r\\\\n '
    match_node = re.findall(regex_node, switch)
    # в regex добавлены знаки ?, чтобы отключить жадность. в выводе match список узлов - строк


    regex_ip = '\"telnet://([0-9.]+)\\\\'
    match_ip = re.findall(regex_ip, switch)
    # в выводе match список ip - строк

    regex_uplink = 'uplinks-count=\\\\\"\d\\\\\">\\\\r\\\\n(?:\\\\t)+ (.+?)\\\\r\\\\n(?:\\\\t)+ </span>'
    match_uplink = re.findall(regex_uplink, switch)
    # в выводе match список uplink - строк

    list_switches = []
    for i in range(len(match_node)):
        list_switches.append([match_name_model[i][0], match_name_model[i][1], match_node[i], match_ip[i], match_uplink[i]])

    for i in range(len(list_switches)):
        print('--------------------------------------')
        print('Название: {}'.format(list_switches[i][0]))
        print('Модель: {}'.format(list_switches[i][1]))
        print('Узел связи: {}'.format(list_switches[i][2]))
        print('IP-адрес: {}'.format(list_switches[i][3]))
        print('Uplink: {}'.format(list_switches[i][4]))

    return list_switches

if __name__ == '__main__':
    node_name = input('Узел Связи: ')
    parsingByNodename(node_name)

