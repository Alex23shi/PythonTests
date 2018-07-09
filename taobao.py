# encoding: utf-8
#!/usr/bin/env python
'''
@author: Alex Shi
@license: (C) Copyright 2018-2020, New York University Tandon School of Engineering.
@contact: cs5615@nyu.edu
@software: PyCharm
@file: taobao.py
@time: 2018/7/9/006 13:48
@desc:
'''
import requests
import re
from xlwt import Workbook
import json
# import xlrd
# import time

def key_name(number):
    # 获取页面的内容并返回
    # name = '手机'
    # URL_1 = "https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20170905&stats_click=search_radio_all%3A1&js=1&imgfile=&q="
    # URL_2 = "&suggest=0_1&_input_charset=utf-8&wq=u&suggest_query=u&source=suggest&p4ppushleft=5%2C48&s="
    # URL = (URL_1 + name + URL_2 + str(number))
    URL="https://s.taobao.com/search?q=%E9%A5%AE%E7%94%A8%E6%B0%B4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc"
    URL2="https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.4247481cKSUg6t&q=%D2%FB%D3%C3%CB%AE&sort=d&style=g&from=mallfp..pc_1_searchbutton#J_Filter"
    # print(URL)
    res = requests.get(URL2)
    return res.text

# 淘宝的爬虫数据都是在json里面，可以先找"status":"show","data":{"****"
def find_date(text,sheet):
    # 根据整个页面的信息，获取商品的数据所在的HTML源码并放回
    reg = r',"data":{"postFeeText":"运费","trace":"msrp_auction","auctions":(\[{.+?}\]),"recommendAuctions"'
    reg = re.compile(reg)
    info = re.findall(reg, text)
    hjson = json.loads(info[0])
    for i in range(len(hjson)):
        dic = hjson[i]
        print(dic['raw_title'])
        print()
        # 第N行第0列
        sheet.write(i+1, 0,dic['raw_title'])
        sheet.write(i+1, 1,dic['view_price'])
        sheet.write(i+1, 2, dic['view_sales'])
    return info[0]







if __name__ == '__main__':
    URL="https://s.taobao.com/search?q=%E9%A5%AE%E7%94%A8%E6%B0%B4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc"
    URL2="https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.775c59abAFrnti&q=%E9%A5%AE%E7%94%A8%E6%B0%B4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&ie=utf8&initiative_id=tbindexz_20170306&tab=mall&sort=sale-desc"
    URL3="https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.775c59abisoTNF&q=%E9%A5%AE%E7%94%A8%E6%B0%B4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&ie=utf8&initiative_id=tbindexz_20170306&tab=mall&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s=44"
    res = requests.get(URL3).text
    # 写入excel方法
    book = Workbook()
    sheet = book.add_sheet('taobao')
    sheet.write(0, 0, '品牌')
    sheet.write(0, 1, '价格')
    sheet.write(0, 2, '销量')
    find_date(res,sheet)
    book.save('./tbWater2.xls')



#
# def main():
#     # 写入excel方法
#     book = Workbook()
#     sheet = book.add_sheet('taobao')
#     sheet.write(0, 0, '品牌')
#     sheet.write(0, 1, '价格')
#     # sheet.write(0, 2, '配置')
#     # k用于生成链接，每个链接的最后面的数字相差48.
#     # N用于记录表格的数据行数，便于写入数据
#     k = 0
#     N = 1
#     for i in range(3 + 1):
#         text = key_name(k + i * 48)
#         print(text)
#         info = find_date(text)
#         N = manipulation_data(info, N,sheet)
#         print('下载第' + str(i) + '页完成')
#     book.save('./taobao.xls')
#
# if __name__ == '__main__':
#     main()