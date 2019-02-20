import requests
import json
import geohash
import random


def get_longitude_latitude(address, key):
    apiurl_amap = 'https://restapi.amap.com/v3/geocode/geo'
    parameters = {'address': address, 'key': key}
    response = requests.get(apiurl_amap, parameters)
    result = json.loads(response.text)
    return result['geocodes'][0]['location'].split(',')


def get_all_restaurants(geohash, latitude, longitude):
    eleme_url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=' + \
        geohash + '&latitude=' + latitude + '&limit=24&longitude=' + \
        longitude + '&offset=0&terminal=web'
    headers = {'cookie': 'ubt_ssid=tebkwnj5ey4211j63ra1fufwkccdd3g9_2018-12-04; _utrace=cbe7939ddcaba86d275d74316a3faf76_2018-12-04; cna=maZmFNcwdXQCAdOi7WlxHfM6; track_id=1545361463|45337d5fc56172933a4b130af8de0446ac06ed31f1126fb6b6|6aa3447ab2fc23b664a09a59857790c9; USERID=15250937; UTUSER=15250937; SID=lFaXhucyFG8LyAhCK2lXz6E7UrJ0Eu9D9sNA; isg=BIOD8w3l2_YZhJcC_Ya5kPi8BkftUBY464RIB7VgeeJadKCWaMpXixOF6gQ6VG8y',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}
    rps = requests.get(eleme_url, headers)
    result = json.loads(rps.text)
    return result


data = get_longitude_latitude(input('请输入想要查看的地址：'),
                              "038404048df63d921a4a5bbb98890b05")
print('你所填地址的精度为：' + data[0] + ' 纬度为：' + data[1])

current_geohash = geohash.encode(float(data[1]), float(data[0]))
print('经纬度由geohash编码后为：' + current_geohash)
# restaurants = get_all_restaurants(current_geohash, data[1], data[0])
# print(restaurants)


while True:
    restaurants = get_all_restaurants(current_geohash, data[1], data[0])
    # random_choice = random.choice(restaurants)
    print(restaurants)
    if input('\n对这家是否满意？') == '是':
        print('\n好的，已停止随机选择，祝你用餐愉快！')
        break
    """print('\n已为你随机选取一家餐馆：' + '\n商家名：' + random_choice['name'] + '\n地址：' +
          random_choice['address'] + '\n评分：' + str(random_choice['rating']) +
          '\n电话：' + random_choice['phone'])
    if input('\n对这家是否满意？') == '是':
        print('\n好的，已停止随机选择，祝你用餐愉快！')
        break

limiting_number = int(input('请输入你要查看附近商家的数量（最多为30家）：'))
count = 0
for i in restaurants:
    count += 1
    print(str(count) + '：' + '商家名：' + i['name'] + '\n地址：' + i['address'] + '\n评分：' + str(i['rating']) + '\n电话：' + i['phone'])
    if count == limiting_number + 1:
        break
"""
