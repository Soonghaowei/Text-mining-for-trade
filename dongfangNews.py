
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import urllib.request
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml.html import fromstring
import pandas as pd
import csv
import codecs

import importlib
import  sys
import codecs


newsUrl = []  # save url
writer = csv.writer(open('D:\\test\\txtTocsv\linking\\testnews.csv', 'w', newline='',encoding='utf-8-sig'))
writer.writerow(['title','date','source','content'])
writer.writerow(codecs.BOM_UTF8)
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


def getIp():
    ip = [
        "http://202.159.118.50:80",
        "http://41.210.252.16:8080",
        "http://159.148.119.39:3128",
        "http://204.16.1.182:3128",
        "http://129.107.60.14:80",
        "http://200.65.129.2:80",
        "http://67.69.254.240:80",
        "http://193.37.152.206:3128",
        "http://169.235.24.133:3127",
        "http://200.204.154.29:6588",
        "http://200.174.85.195:3128",
        "http://67.69.254.248:80",
        "http://67.69.254.243:80",
        "http://152.101.118.253:8080",
        "http://189.112.246.145:8080",
        "http://79.148.249.246:8080",
    ]

    IP = random.choice(ip)
    return IP


def getHTMLText(url ):


        agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        cookie = 'qgqp_b_id=de6f5b2aab0bf1b85367cff30462fbd1; st_pvi=64069861991421; st_sp=2019-01-24%2018%3A36%3A57; st_si=94918195918945; st_asi=delete; bdshare_firstime=1548326400263; st_sn=12; st_psi=2019012418445425-111000300841-9825945936'
        refer = 'http://finance.eastmoney.com/news/cgnjj_1.html'
        headers = {'User-Agent': userAgent(), 'Cookie': cookie, 'Refer': refer}

        r = requests.get(url, headers)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')

        # print(soup)
        ##µÃµ½£¨Ã¿Ò»Ò³µÄ£©Ã¿Ò»¸öÍøÕ¾

        for eachurl in soup.select('p.title'):
            hrefCom = eachurl.select('a')[0]['href']
            # print(hrefCom)
            if hrefCom not in newsUrl:
            #
                newsUrl.append(hrefCom)
                getContentOfNews(hrefCom )
            # else:
            #     continue

        # print(newsUrl)



def getAllurlOfNews():

    for i in range(26):
        # http://finance.eastmoney.com/a/cgsxw_3.html
        try:
            url = 'http://finance.eastmoney.com/a/cgsxw_' + str(i) + '.html'
            getHTMLText(url )
        except:
            a=1

def getContentOfNews(url ):
    titleZ = []
    dateZ = []
    sourceZ = []
    contentZ = []

    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    cookie = 'qgqp_b_id=de6f5b2aab0bf1b85367cff30462fbd1; st_pvi=64069861991421; st_sp=2019-01-24%2018%3A36%3A57; st_si=94918195918945; st_asi=delete; bdshare_firstime=1548326400263; st_sn=12; st_psi=2019012418445425-111000300841-9825945936'
    refer = 'http://finance.eastmoney.com/news/cgnjj_1.html'
    headers = {'User-Agent': userAgent(), 'Cookie': cookie, 'Refer': refer}

    r = requests.get(url, headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.select('div.newsContent > h1')[0]
    title = str(title).replace('<h1>', '')
    title = str(title).replace('</h1>', '')
    print(title)

    # f = open('D:/Soong/materialOfNlp/dongfangcaifuGONGSI/' + title + '.txt', 'a+', encoding='utf-8')
    print("sdff")
    title=str(title)
    titleZ.append(title)


    date = soup.select('div.time')[0]
    date = str(date).replace('<div class="time">', '')
    date = str(date).replace('</div>', '')
    print(date)
    date = str(date)
    dateZ.append(date)

    source = soup.select('div.source')[0]
    source = str(source).replace('<div class="source data-source" data-source="', '')
    source = str(source).replace('">', '')
    source = str(source).replace('<span>À´Ô´£º</span>', '')
    source = str(source).replace('</div>', '')
    source = str(source).replace(' ', '')
    source = str(source).replace('\n', '')
    source = str(source)
    sourceZ.append(source)

    # f.write(str(source))
    # f.write(str('\n'))

    content1 = ''
    for content in soup.select('div.Body'):
        content = content.select('p')
        content = str(content).replace('[<p>¡¡¡¡', '')
        content = str(content).replace('</p>]', '')
        content = str(content).replace('</p>, <p>', '')
        # print(content)
        content1 = content1 + content
        content1= str(content1)
    # f.write(str(content1))
    contentZ.append(content1)

    time.sleep(1)
    # print(titleZ)
    # f.close()

    writer.writerow([titleZ,dateZ, sourceZ,contentZ])

for a in range(2000000):

        getAllurlOfNews()
        time.sleep(36000)
        # dataframe = pd.DataFrame({'title': titleZ, 'date': dateZ, 'source': sourceZ, 'content': contentZ})
        #
        # dataframe.to_csv(address, index=False, sep=',',encoding="utf_8_sig")

    # else:
    #     getAllurlOfNews()
    #     time.sleep(93600)##one day
    # a=a+1

