import os
import getpass
import json
import time
from datetime import datetime
import urllib.request

url_limit = 'http://192.243.116.174:4567/assets/limit.txt'

req = urllib.request.Request(url_limit)

def getLimitTime():
    limitTime=2700
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            limitTime = int(response.readline().decode('utf8'))
    except BaseException as e:
        limitTime=2700
    return limitTime

def readFile():
    with open('c:\\cfg.json', 'r') as f:
        return json.load(f)

def modifyFile(jsonStr):
    with open('c:\\cfg.json', 'w') as f:
        json.dump(jsonStr,f)

def checkTime(t):
    limitTime = getLimitTime()
    if t >= limitTime:
        return False
    else:
        return True

#print('hello, world.')
#print(getpass.getuser())

cuser = getpass.getuser().lower()

if 'wangxiao' != cuser and 'administrator' != cuser:
    s = readFile()
    cdate = datetime.now().strftime('%Y-%m-%d')
    if cdate != s['date']:
        s['date'] = cdate
        s['time'] = 0
    while checkTime(s['time']):
        time.sleep(120)
        s['time'] += 120
        modifyFile(s)
    os.system('shutdown -l')

