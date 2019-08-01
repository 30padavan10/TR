from requests.auth import HTTPBasicAuth
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import stash_sw_parse as stash


def parsingByNodename(node_name):
    url = 'https://cis.corp.itmh.ru/stu/NetSwitch/SearchNetSwitchProxy'
    data = {'IncludeDeleted': 'false', 'IncludeDisabled': 'true', 'HideFilterPane': 'false'}
    data['NodeName'] = node_name.encode('utf-8')
    req = requests.post(url, verify=False, auth=HTTPBasicAuth('pankov.dmitriy', 'WoW567Nerulit'), data=data)
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


    regex_switch_id = 'span class=\\\\\"netSwitchPorts\\\\\" switch-id=\\\\\"(\d+)\\\\'
    match_switch_id = re.finditer(regex_switch_id, switch)
    list_ports = []
    for i in match_switch_id:
        ports = {}
        url_switch_id = 'https://cis.corp.itmh.ru/stu/Switch/Details/' + i.group(1)
        req_switch_id = requests.get(url_switch_id, verify=False, auth=HTTPBasicAuth('pankov.dmitriy', 'WoW567Nerulit'))
        switch_id = req_switch_id.content.decode('utf-8')

        regex_total_ports = 'for=\"TotalPorts\">(\d+)<'
        match_total_ports = re.search(regex_total_ports, switch_id)
        ports['Всего портов'] = match_total_ports.group(1)

        regex_broken_ports = 'for=\"BrokenPorts\">(\d+)<'
        match_broken_ports = re.search(regex_broken_ports, switch_id)
        ports['Неисправных'] = match_broken_ports.group(1)

        regex_client_ports = 'for=\"ClientCableUsedPorts\">(\d+)<'
        match_client_ports = re.search(regex_client_ports, switch_id)
        ports['Занятых клиентами'] = match_client_ports.group(1)

        regex_link_ports = 'for=\"LinkUsedPorts\">(\d+)<'
        match_link_ports = re.search(regex_link_ports, switch_id)
        ports['Занятых линками'] = match_link_ports.group(1)

        regex_zombi_ports = 'for=\"ZombieContractPorts\">(\d+)<'
        match_zombi_ports = re.search(regex_zombi_ports, switch_id)
        ports['Зомби'] = match_zombi_ports.group(1)

        regex_free_ports = 'for=\"FreePorts\">(\d+)<'
        match_free_ports = re.search(regex_free_ports, switch_id)
        ports['Свободные'] = match_free_ports.group(1)

        regex_avail_ports = 'for=\"AvailablePorts\">(\d+)<'
        match_avail_ports = re.search(regex_avail_ports, switch_id)
        ports['Доступные'] = match_avail_ports.group(1)

        list_ports.append(ports)
    list_switches = []
    for i in range(len(match_node)):
        list_switches.append([match_name_model[i][0], match_name_model[i][1], match_node[i], match_ip[i], match_uplink[i], list_ports[i]])

    for i in range(len(list_switches)):
        print('--------------------------------------')
        print('Название: {}'.format(list_switches[i][0]))
        print('Модель: {}'.format(list_switches[i][1]))
        print('Узел связи: {}'.format(list_switches[i][2]))
        print('IP-адрес: {}'.format(list_switches[i][3]))
        print('Uplink: {}'.format(list_switches[i][4]))
        print('Порты: {}'.format(list_switches[i][5]))
        if int(list_switches[i][5]['Доступные']) < 10:
            print(stash.stash(list_switches[i][0], list_switches[i][1]))


    
    return list_switches

if __name__ == '__main__':
    node_name = input('Узел Связи: ')
    parsingByNodename(node_name)

