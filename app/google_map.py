import urllib.request, json
import urllib.parse
import datetime
import os

#Google Maps Platform Directions API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
googlemap_api = os.environ["googlemap_api"]

#出発地、目的地を入力
origin = input('出発地を入力: ').replace(' ','+')
destination = input('目的地を入力: ').replace(' ','+')
dep_time = input('出発時間を入力: yyyy/mm/dd hh:mm 形式 ')

#UNIX時間の算出
dtime = datetime.datetime.strptime(dep_time, '%Y/%m/%d %H:%M')
unix_time = int(dtime.timestamp())

# print('')
# print('=====')
# print('unixtime')
# print(unix_time)
# print('=====')

nav_request = 'language=ja&origin={}&destination={}&departure_time={}&key={}'.format(origin,destination,unix_time,googlemap_api)
nav_request = urllib.parse.quote_plus(nav_request, safe='=&')
request = endpoint + nav_request

# print('')
# print('=====')
# print('url')
# print(request)
# print('=====')

#Google Maps Platform Directions APIを実行
response = urllib.request.urlopen(request).read()

#結果(JSON)を取得
directions = json.loads(response)

#所要時間を取得
for key in directions['routes']:
    #print(key) # titleのみ参照
    #print(key['legs']) 
    for key2 in key['legs']:
        print('')
        print('=====')
        print(key2['distance']['text'])
        print(key2['duration_in_traffic']['text'])
        print('=====')

