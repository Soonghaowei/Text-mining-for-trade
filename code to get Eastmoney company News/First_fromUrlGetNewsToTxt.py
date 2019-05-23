import random
import requests
import csv
import jieba
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time
import requests
from nltk.tokenize import WordPunctTokenizer
import jieba
import random
from bs4 import BeautifulSoup
import unicodedata
import json
from nltk.tokenize import WordPunctTokenizer
import numpy as np
def userAgent():
    user_agents = [
        "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )", ]

    UserAgent = random.choice(user_agents)
    return UserAgent
def getContentOfNews(url):
 try:
    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    cookie = 'qgqp_b_id=de6f5b2aab0bf1b85367cff30462fbd1; st_pvi=64069861991421; st_sp=2019-01-24%2018%3A36%3A57; st_si=94918195918945; st_asi=delete; bdshare_firstime=1548326400263; st_sn=12; st_psi=2019012418445425-111000300841-9825945936'
    refer = 'http://finance.eastmoney.com/news/cgnjj_1.html'
    proxy_list = [
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"}
    ]
    proxy = random.choice(proxy_list)
    headers = {'User-Agent': userAgent(), 'Cookie': cookie, 'Refer': refer, 'proxies': proxy}

    # titleList=[]
    # dateList=[]
    # suorceList=[]
    # summaryList=[]
    # contentList=[]
    time.sleep(3)
    r = requests.get(url, headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.select('div.newsContent > h1')[0]
    title = str(title).replace('<h1>', '')
    title = str(title).replace('</h1>', '')
    print(title)
    # titleList.append(title)
    f = open('D:\\Soong\\Soong\\dongfangcaifu\\data\\dongfangcaifuAllcsvTXT\\' + str(title).replace(' ','') + '.txt', 'a+', encoding='utf-8')
    print("sdff")
    f.write(str(title))
    f.write(str('\n'))
    date = soup.select('div.time')[0]
    date = str(date).replace('<div class="time">', '')
    date = str(date).replace('</div>', '')
    print(date)
    f.write(str(date))
    # dateList.append(date)
    f.write(str('\n'))

    source = soup.select('div.source')[0]
    source = str(source).replace('<div class="source data-source" data-source="', '')
    source = str(source).replace('">', '')
    source = str(source).replace('<span>À´Ô´£º</span>', '')
    source = str(source).replace('</div>', '')
    source = str(source).replace(' ', '')
    source = str(source).replace('\n', '')

    # suorceList.append(source)
    f.write(str(source))
    f.write(str('\n'))
    # summary= soup.select('div.b-review')[0]
    # summary = str(summary).replace('<div class="b-review">', '')
    # summary = str(summary).replace('</div>', '')
    # # print(summary)
    # summaryList.append(summary)
    # print('summary')
    # print(summaryList)
    content1 = ''
    time.sleep(1)
    for content in soup.select('div.Body'):
        content = content.select('p')
        content = str(content).replace('[<p>¡¡¡¡', '')
        content = str(content).replace('</p>]', '')
        content = str(content).replace('</p>, <p>', '')
        content = str(content).replace('<p style="display:none;height:1px;overflow:hidden;">', '')
        content = str(content).replace('<br/>', '')
        content = str(content).replace('<p style="text-align:center;">', '')
        content = str(content).replace('[<p>¡¡¡¡', '')
        content = str(content).replace('[<p>¡¡¡¡', '')

        # print(content)
        content1 = content1 + content
    f.write(str(content1))
    # contentList.append(content1)
    # print('********************')
    # print('title')
    # print(titleList)
    #
    # print('date')
    # print(dateList)
    #
    # print('source')
    # print(suorceList)
    #
    # print('content')
    # print(contentList)
    #
    # print('********************')
    # with open('D:\\Soong\\materialOfNlp\\dongfangcaifu\\dongfangcaifuNews.csv', 'a+', newline='') as f:
    #
    #         writer = csv.writer(f)
    #         writer.writerows(zip(titleList, dateList,suorceList,summaryList,contentList))
    #         print('1111111111')

    time.sleep(1)
    f.close()
 except:
     a=1
import sys
import os

from xlrd import open_workbook # xlrd用于读取xld
# import xlwt  # 用于写入xls
# data = pd.read_csv('D:\\Soong\\Soong\\dongfangcaifu\\data\\dongfangcaifuAllcsv\\'+'1.xls')
# data.head()
for filename in os.listdir('D:\\Soong\\Soong\\dongfangcaifu\\data\\dongfangcaifuAllcsv'):
    workbook =open_workbook(r'D:\\Soong\\Soong\\dongfangcaifu\\data\\dongfangcaifuAllcsv\\'+filename)
    sheet_name= workbook.sheet_names()  # 打印所有sheet名称，是个列表
    sheet = workbook.sheet_by_index(0)  # 根据sheet索引读取sheet中的所有内容
    # sheet1= workbook.sheet_by_name('网址')  # 根据sheet名称读取sheet中的所有内容
    # print(sheet.name, sheet.nrows, sheet.ncols)  # sheet的名称、行数、列数
    content = sheet.col_values(5)  # 第六列内容
    # print(content)
    a=0
    for con in content:
        time.sleep(4)
        a=a+1
        if(a>1):
            # print(con)
            getContentOfNews(con)
