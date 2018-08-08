import sys
from importlib import reload

reload(sys)
#sys.setdefaultencoding("utf-8")

import jieba
import jieba.analyse

wf = open('./clean_title.txt', 'w+')
for line in open('./Comments.csv'):
    item = line.strip('\n\r').split('\t') # 制表格切分
    # print item[1]
    tags = jieba.analyse.extract_tags(item[3]) # jieba分词
    tagsw = ",".join(tags) # 逗号连接切分的词
    wf.write(tagsw)

wf.close()

word_lst = []
word_dict = {}
with open('./clean_title.txt') as wf, open("word.txt", 'w') as wf2: #打开文件

    for word in wf:
        word_lst.append(word.split(',')) #使用逗号进行切分
        for item in word_lst:
            for item2 in item:
                if item2 not in word_dict: #统计数量
                    word_dict[item2] = 1
                else:
                    word_dict[item2] += 1


    for key in word_dict:
        print
        key, word_dict[key]
        wf2.write(key + ' ' + str(word_dict[key]) + '\n') #写入文档
