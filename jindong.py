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
import re

import requests
from bs4 import BeautifulSoup
from xlwt import Workbook


a = 1
def find_date(url,sheet):
    p_r = requests.get(url)
    p_c = p_r.content
    p_soup = BeautifulSoup(p_c, 'html.parser')
    all = p_soup.find_all('li', {'class': 'gl-item'})
    print(len(all))
    global a

    for item in all:

        title = item.find('div', {'class': 'p-name'}).find('em').text.replace('京东超市','').replace('新老包装替换，随机发货','').replace('新老包装随机发货','')


        print(title)
        price = item.find('div', {'class': 'p-price'}).find('i').text
        num = item.find('div', {'class': 'p-commit'}).find('a').text
        print(a)
        # 第N行第0列
        sheet.write(a, 0,title)
        sheet.write(a, 1,price)
        sheet.write(a, 2, num)
        a += 1


if __name__ == '__main__':
    urllist = []
    url1 = 'https://search.jd.com/search?keyword=%E9%A5%AE%E7%94%A8%E6%B0%B4&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%A5%AE%E7%94%A8%E6%B0%B4&psort=3&cid2=1585&cid3=10975&stock=1&click=0'
    url2 = 'https://search.jd.com/search?keyword=%E9%A5%AE%E7%94%A8%E6%B0%B4&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%A5%AE%E7%94%A8%E6%B0%B4&psort=3&cid2=1585&cid3=10975&stock=1&page=3&s=61&click=0'
    urllist.append(url1)
    urllist.append(url2)

    # 写入excel方法
    book = Workbook()
    sheet = book.add_sheet('jindong')
    sheet.write(0, 0, '品牌')
    sheet.write(0, 1, '价格')
    sheet.write(0, 2, '销量')
    for i in  range(len(urllist)):
      find_date(urllist[i],sheet)

    book.save('./jdWater.xls')


