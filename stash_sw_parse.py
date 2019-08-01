import re
from requests.auth import HTTPBasicAuth
import requests


def stash(sw, model):
    url = 'https://stash.itmh.ru/projects/NMS/repos/pantera_extrim/raw/backups/' + sw + '-config?at=refs%2Fheads%2Fmaster'
    req = requests.get(url, verify=False, auth=HTTPBasicAuth('pankov.dmitriy', 'WoW567Nerulit'))
    switch = req.content.decode('utf-8')
    if 'SNR' in model or 'Cisco' in model or 'Orion' in model:
        regex_description = '\wnterface (\S+)(.+?)!'

        match_description = re.finditer(regex_description, switch, flags=re.DOTALL)

        for i in match_description:
            if 'description' in i.group(2): 
                desc = i.group(2).split('\r\n')
                if 'description' in desc[1]:
                    desc = i.group(2).split('\r\n')[1]
                else:
                    desc = i.group(2).split('\r\n')[2]
            else:
                desc = '---'
            if 'shutdown' in i.group(2):
                link = 'admin down'
            else:
                link = '---'
            if 'switchport access vlan 4094' in i.group(2):
                vlan = 'vlan 4094'
            else:
                vlan = '-----'
            print('{} {:40} {:15} {}'.format(i.group(1), desc, link, vlan))
    elif 'D-Link' in model:
        regex_description = 'config (ports \d+) (?:.+?) (description \".*?\")\n'
        match_description = re.finditer(regex_description, switch, flags=re.DOTALL)
        for i in match_description:
            print(i.group(1), i.group(2))

        regex_free = 'config vlan stub add untagged (\S+)'
        match_free = re.search(regex_free, switch)
        print('Свободные порты: {}'.format(match_free.group(1)))


if __name__ in '__main__':
    sw = input('Название КАД: ')
    model = input('Модель: ')
    stash(sw, model)
