import static as static
from bs4 import BeautifulSoup
import re,requests,json
from xlwt import Workbook

s = requests.session()
url = 'https://club.jd.com/comment/productPageComments.action'
data = {
    'callback':'fetchJSON_comment98vv61',
    'productId':'4238895', #纯悦水ID，可被替换为任意产品ID
    'score':0,
    'sortType':5,
    'pageSize':10,
    'isShadowSku':0,
    'page':0
}

book = Workbook()
sheet = book.add_sheet('京东Comments')
sheet.write(0, 0, '用户名')
sheet.write(0, 1, '时间戳')
sheet.write(0, 2, '客户端')
sheet.write(0, 3, '评价')
f = open("./Comments.csv", 'w+')
r = 1
while data['page'] < 100 :
    t = s.get(url, params = data).text
    try:
        t = re.search(r'(?<=fetchJSON_comment98vv61\().*(?=\);)',t).group(0)
    except Exception as e:
        break

    j = json.loads(t)
    commentSummary = j['comments']
    for comment in commentSummary:
        c_content = comment['content']
        c_time = comment['referenceTime']
        c_name = comment['nickname']
        c_client = comment['userClientShow']
        print('{}\t{}\t{}\t{}'.format(c_name,c_time,c_client,c_content), file=f)
        sheet.write(r, 0, c_name)
        sheet.write(r, 1, c_time)
        sheet.write(r, 2, c_client)
        sheet.write(r, 3, c_content)
        r += 1
    data['page'] += 1

f.close()

book.save('./jdComments.xls')