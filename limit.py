import urllib.request

url_limit = 'http://192.243.116.174:4567/assets/limit.txt'

req = urllib.request.Request(url_limit)

def getLimitTime():
    limitTime=1800
    try:
        with urllib.request.urlopen(req) as response:
            limitTime = int(response.readline().decode('utf8'))
    except BaseException as e:
        limitTime=1800
    return limitTime

t=getLimitTime()
print( t )
print( t >500 )

