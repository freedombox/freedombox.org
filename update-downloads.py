#!/usr/bin/python3

import bs4
import htmllistparse
import re
import requests

url = 'https://ftp.freedombox.org/pub/freedombox/latest/'

req = requests.get(url, timeout=30)
req.raise_for_status()

soup = bs4.BeautifulSoup(req.content, 'html5lib')
cwd, listing = htmllistparse.parse(soup)

print('title: FreedomBox Download')
print('---')
print('release_version: <TODO>')
print('---')
print('release_date: <TODO>')
print('---')
print('images:')

for f in listing:
    if f.name.endswith('.xz'):
        if 'a20-olinuxino-lime-' in f.name:
            target = 'A20 OLinuXino LIME'
        elif 'a20-olinuxino-lime2' in f.name:
            target = 'A20 OLinuXino LIME2'
        elif 'a20-olinuxino-micro' in f.name:
            target = 'A20 OLinuXino MICRO'
        elif 'amd64.img' in f.name:
            target = '64-bit x86 (amd64)'
        elif 'amd64.qcow2' in f.name:
            target = 'Qemu 64-bit'
        elif 'amd64.vdi' in f.name:
            target = 'VirtualBox 64-bit'
        elif 'i386.img' in f.name:
            target = '32-bit x86 (i386)'
        elif 'i386.qcow2' in f.name:
            target = 'Qemu 32-bit'
        elif 'i386.vdi' in f.name:
            target = 'VirtualBox 32-bit'
        elif 'beaglebone' in f.name:
            target = 'BeagleBone Black'
        elif 'cubieboard2' in f.name:
            target = 'Cubieboard2'
        elif 'cubietruck' in f.name:
            target = 'Cubietruck'
        elif 'dreamplug' in f.name:
            target = 'DreamPlug'
        elif 'pcduino3' in f.name:
            target = 'pcDuino3'
        elif 'raspberry-' in f.name:
            target = 'Raspberry Pi'
        elif 'raspberry2' in f.name:
            target = 'Raspberry Pi 2'
        elif 'raspberry3' in f.name:
            target = 'Raspberry Pi 3'
        else:
            target = '<TODO>'

        parts = re.split("\W+|_", f.name)

        month = f.modified.tm_mon
        month = str(month) if month >= 10 else '0' + str(month)
        day = f.modified.tm_mday
        day = str(day) if day >= 10 else '0' + str(day)

        print()
        print('#### download_image ####')
        print('hardware_target: ' + target)
        print('----')
        print('tags:')
        print()
        print(str(f.modified.tm_year) + '-' + month + '-' + day)
        print(parts[-3])
        print(parts[1])
        print(parts[2])
        print('----')
        print('filename: ' + f.name)
        print('----')
        print('signature_filename: ' + f.name + '.sig')
        print('----')
        print('size: ' + str(round(f.size / 1e6)))
