#!# encoding: utf-8
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
from bs4 import BeautifulSoup
from xlwt import Workbook

a = 1
def find_date(url,sheet):

    url = 'http://search.yhd.com/c0-0/mbname-b/a82967::1107-s2-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E9%A5%AE%E7%94%A8%E6%B0%B4/#page=2&sort=2'
    p_r = requests.get(url)
    p_c = p_r.content
    p_soup = BeautifulSoup(p_c, 'html.parser')
    all = p_soup.find_all('div', {'class': 'mod_search_pro'})
    print(len(all))
    global a
    for item in all:
        item_dic = {}
        title = item.find('p', {'class': 'proName clearfix'}).find('a').get('title')
        price = item.find('em', {'class': 'num'}).text
        num = item.find('span', {'class': 'comment'}).text
        # 第N行第0列
        sheet.write(a, 0,title)
        sheet.write(a, 1,price)
        sheet.write(a, 2, num)
        a += 1


if __name__ == '__main__':
    urllist = []
    url1 = 'http://search.yhd.com/c0-0/mbname-b/a82967::1107-s2-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E9%A5%AE%E7%94%A8%E6%B0%B4/'
    url2 = 'http://search.yhd.com/c0-0/mbname-b/a82967::1107-s2-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E9%A5%AE%E7%94%A8%E6%B0%B4/#page=2&sort=2'
    url3 = 'http://search.yhd.com/c0-0/mbname-b/a82967::1107-s2-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E9%A5%AE%E7%94%A8%E6%B0%B4/#page=3&sort=2'
    urllist.append(url2)
    #urllist.append(url2)
    #urllist.append(url3)

    # 写入excel方法
    book = Workbook()
    sheet = book.add_sheet('onestore')
    sheet.write(0, 0, '品牌')
    sheet.write(0, 1, '价格')
    sheet.write(0, 2, '销量')
    for i in  range(len(urllist)):
      find_date(urllist[i],sheet)

    book.save('./onestore2.xls')
