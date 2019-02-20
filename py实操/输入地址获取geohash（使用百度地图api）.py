import requests
import json
import geohash


def get_longitude_latitude(address, ak):
    apiurl = 'http://api.map.baidu.com/geocoder/v2/?address=' + address + '&output=json&ak=' + ak
    response = requests.get(apiurl)
    result = json.loads(response.text)
    return result['result']['location']


data = get_longitude_latitude('厦门市政府', "TKjovHiKZGLCZAwcqUGKzTw0BWWqSGyk")
print('精度：%.6f' % data['lng'] + '纬度：%.6f' % data['lat'])
geohash = geohash.encode(float(data['lat']), float(data['lng']))
print(geohash)
