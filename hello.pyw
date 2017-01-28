import os
import getpass
import json
import time
from datetime import datetime

def readFile():
    with open('c:\\cfg.json', 'r') as f:
        return json.load(f)

def modifyFile(jsonStr):
    with open('c:\\cfg.json', 'w') as f:
        json.dump(jsonStr,f)

def checkTime(t):
    if t > 3600:
        return False
    else:
        return True

#print('hello, world.')
#print(getpass.getuser())

cuser = getpass.getuser()

if 'jason' == cuser:
    s = readFile()
    cdate = datetime.now().strftime('%Y-%m-%d')
    if cdate != s['date']:
        s['date'] = cdate
        s['time'] = 0
    while checkTime(s['time']):
        time.sleep(300)
        s['time'] += 300
        modifyFile(s)
    os.system('shutdown -l')

