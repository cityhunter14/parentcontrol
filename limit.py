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

t=getLimitTime()
print( t )
print( t >500 )

