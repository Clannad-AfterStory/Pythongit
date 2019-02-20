import itchat
import requests
import re
# 抓取网页


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        return ""
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):
    # 当消息不是指定的某用户发出的时候才进行自动回复
    if not msg['FromUserName'] == Name[username]:
        # 回复给好友
        url = "http://www.tuling123.com/openapi/api?key=73ea50256fee4ac79f67f9e37dabf129&info="
        url = url + msg['Text']
        html = getHtmlText(url)
        message = re.findall(r'\"text\"\:\".*?\"', html)
        reply = eval(message[0].split(':')[1])
        return reply


if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    username = input("收到谁的信息可以不用小图灵自动回复呢？输入他的用户名就可以了：")
    itchat.run()
