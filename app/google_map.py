"""
出発地と目的地、時刻を入力として、移動距離と移動時間、目的地で雨が降り出す時間を出力
"""

# %%
import urllib.request, json
import urllib.parse
import datetime
import requests
import os

#Google Maps Platform Directions API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
# GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
GOOGLE_API_KEY = "AIzaSyBICPxWgeecD98TOFIbfvgmpzx_ghBTVGc"
#出発地、目的地を入力
origin = "名古屋駅" # 出発地
destination = "栄駅" # 目的地
dep_time = "2023/06/20 12:00" # yyyy/mm/dd hh:mm

#UNIX時間の算出
dtime = datetime.datetime.strptime(dep_time, '%Y/%m/%d %H:%M')
unix_time = int(dtime.timestamp())

# 目的地の緯度と経度を取得
# Google Maps Geocoding APIのエンドポイントURLとAPIキーを設定します
url = 'https://maps.googleapis.com/maps/api/geocode/json'

# 住所または場所名を指定してGeocoding APIを呼び出します

params = {
    'address': destination,
    'key': GOOGLE_API_KEY
}
response = requests.get(url, params=params)
data = response.json()

# 結果から緯度と経度を取得します
if data['status'] == 'OK':
    location = data['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
else:
    print('緯度と経度の取得に失敗しました。')

nav_request = 'language=ja&origin={}&destination={}&departure_time={}&key={}'.format(origin,destination,unix_time,GOOGLE_API_KEY)
nav_request = urllib.parse.quote_plus(nav_request, safe='=&')
request = endpoint + nav_request

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


# OpenWeatherMap APIキーを設定します
WEATHER_API_KEY = 'adf3684ba949b3bf361a0cdcbbcc5a62'

# 天気情報を取得するためのAPIリクエストを作成します
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}'

# APIリクエストを送信して天気情報を取得します
response = requests.get(url)
data = response.json()

rainy_periods = []
for forecast in data['list']:
    timestamp = forecast['dt']
    date_time = forecast['dt_txt']
    weather = forecast['weather'][0]['main']
    rain_probability = forecast['pop']  # 降水確率

    if rain_probability >= 50:
        rainy_periods.append((date_time, rain_probability))

# 降水確率が50%以上の時間帯と雨の予測開始時間を表示します
if not rainy_periods:
    print('今日は雨は予測されていません。')
else:
    print('降水確率が50%以上の時間帯:')
    for period in rainy_periods:
        print('時間:', period[0])
        print('降水確率:', period[1])
        print('---')
    print('雨が降り始める予測時間:', rainy_periods[0][0])
# %%
