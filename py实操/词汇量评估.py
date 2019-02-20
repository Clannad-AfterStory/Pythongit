import requests
import json
import sys
import time


# 定义函数restrict_input用以限定输入的内容；参数a为str类型，显示输入提示；参数b为列表类型，限定输入范围。
def restrict_input(a, b):
    while True:
        sr = input(a)
        while sr not in b:
            print('\n输入内容不符合规范，请根据提示重新输入！\n')
            break
        else:
            return sr
            break


print('\n此程序可以评估你所掌握的词汇量\n')
sf = restrict_input('是否想做个评估？（输入Y或者N）：', ['Y', 'N'])
while sf == 'N':
    sys.exit()
get = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
fanwei = json.loads(get.text)
print('''\n词库如下：
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
''')
bianhao = int(
    restrict_input('请输入你选择的词库编号，按Enter键确认。：',
                   ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
ciku = fanwei['data'][bianhao - 1][0]
cikumin = fanwei['data'][bianhao - 1][1]
test = requests.get(
    'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=' + ciku)
words = json.loads(test.text)
words_knows = []
not_knows = []
right_ranks = []
words_ranks = []
danci = []
print('\n测试现在开始。如果认识请输入Y，否则直接回车：')
n = 0
for x in words['data']:
    n = n + 1
    print("\n第{}个：{}".format(n, x['content']))
    words_ranks.append(x['rank'])
    answer = restrict_input('认识请输入Y，否则直接回车:', ['Y', ''])
    if answer == 'Y':
        words_knows.append(x)
        danci.append(x['content'])
    else:
        not_knows.append(x)
print('\n在上列{}个单词当中，有{}个是你觉得认识的，它们是：'.format(len(words['data']), len(danci)))
for dc in danci:
    print('\n' + dc)
    time.sleep(2)
print('\n现在我们来检测下你有没有真正的掌握它们：')
wrong_words = []
right_num = 0
for y in words_knows:
    print('\n单词\"' + y['content'] + '\"的翻译是：')
    print('\n' + 'A:' + y['definition_choices'][0]['definition'])
    print('B:' + y['definition_choices'][1]['definition'])
    print('C:' + y['definition_choices'][2]['definition'])
    print('D:' + y['definition_choices'][3]['definition'])
    xuanze = restrict_input('\n请选择正确选项：', ['A', 'B', 'C', 'D'])
    dic_rank = {'A': y['definition_choices'][0]['rank'], 'B': y['definition_choices'][1]['rank'],
                'C': y['definition_choices'][2]['rank'], 'D': y['definition_choices'][3]['rank']}
    dic_definition = {'A': y['definition_choices'][0]['definition'], 'B': y['definition_choices'][1]['definition'],
                      'C': y['definition_choices'][2]['definition'], 'D': y['definition_choices'][3]['definition']}
    if dic_rank[xuanze] == y['rank']:
        print('\n回答正确！')
        right_num += 1
        right_ranks.append(y['rank'])
    else:
        dicfz = dict(zip(dic_rank.values(), dic_rank.keys()))
        zq = dicfz[y['rank']]
        print('\n你选错啦！\n\n单词{}的正确翻译应该是{}:{}'.format(y['content'], zq, dic_definition[zq]))
        wrong_words.append(y)
print('\n现在到了揭晓结果的时刻了：')
print('在{}个{}词汇当中，你认识其中的{}个；在认识的词汇中实际掌握的有{}个，错误的有{}个。'.format(
    len(words['data']), cikumin, len(danci), right_num, len(wrong_words)))

data = {
    'category': ciku,
    'phase': '',
    'right_ranks': ','.join(list(map(str, right_ranks))),
    'word_ranks': ','.join(list(map(str, words_ranks)))
}
url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
header = {
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
response = requests.post(url, headers=header, data=json.dumps(data))
df = json.loads(response.text)
vocab = df['data']['vocab']
comment = df['data']['comment']
print('你掌握的{}的词汇量大约是{}个，{}'.format(cikumin, vocab, comment))

sfdy = restrict_input('是否打印并保存你的错词集？填入Y或N:', ['Y', 'N'])
if sfdy == 'Y':
    f = open('错题集.txt', 'a+', encoding='utf-8')
    print('你记错的单词有：')
    f.write('你记错的单词有：\n')
    m = 0
    for z in wrong_words:
        m += 1
        for x in z['definition_choices']:
            if x['rank'] == z['rank']:
                zqfy = x['definition']
        print(z['content'] + ',它的正确翻译是' + zqfy)
        time.sleep(1)
        f.write(str(m) + '.' + z['content'] + '  中文翻译：' + zqfy + '\n')
    print('你不认识的单词有：')
    f.write('你不认识的单词有：')
    n = 0
    for x in not_knows:
        n += 1
        for z in x['definition_choices']:
            if z['rank'] == x['rank']:
                zqfy = z['definition']
        print(x['content'] + ',它的正确翻译是' + zqfy)
        time.sleep(1)
        f.write(str(n) + '. ' + x['content'] + '  中文翻译：' + zqfy + '\n')
    print('记错的和没掌握的单词已保存到当前目录下“错题集.txt”文件中，记得要多加复习哦！')
else:
    print('那下次再见啦！')
