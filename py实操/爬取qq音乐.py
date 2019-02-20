import requests
import json


for i in range(1, 6):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63635111669320151&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=' + str(i) + '&n=20&w=%E8%AE%B8%E5%B5%A9&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}
    res = requests.get(url, headers)
    jsoners = json.loads(res.text)
    music = jsoners['data']['song']['list']
    for x in music:
        print('歌名为：' + x['name'] + '\n所属专辑：' + x['album']['name'] + '\n时长：' + str((x['interval'])) + '秒\n播放链接：https://y.qq.com/n/yqq/song/' + x['mid'] + '.html\n')
