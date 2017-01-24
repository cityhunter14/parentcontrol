import os
import getpass
import json
from datetime import datetime

#print('hello, world.')
#print(getpass.getuser())

cuser = getpass.getuser()

if 'jason' == cuser:
    os.system('shutdown -l')
else:
    with open('c:\\cfg.json', 'r') as f:
        s = json.load(f)
    cdate = datetime.now().strftime('%Y-%m-%d')
    if cdate == s['date']:
    else:
        s['date'] = cdate
        s['time'] = 0
        with open('c:\\cfg.json', 'r') as f:
    #print(s['date'])
    print(s)
    exit(0)


