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
import tushare as ts   #60001

comInf=pd.read_csv('D:\\Soong\\Soong\\dongfangcaifu\\comNameCode.csv')
comName=comInf['NameCom']
comCode=[]
for index in range(len(comInf['CodeCom'])):
    comCode.append(str(comInf['CodeCom'][index])[:6])
    
#   dongfang54 is the news 
fnews3=pd.read_csv('D:\\Soong\\Soong\\dongfangcaifu\\data\\csv\\dongfang54.csv')
fnews3=fnews3

title=fnews3['title']
##对每个title 分词
def JieBaTitle (titleName):
    finTitle = []
    for index in range(len(titleName)):
        thisTitle = []

        titl = ''

        titl = titl.join(str((titleName[index])).replace(',', '').replace(': ', ''))
        titlez = jieba.cut_for_search(titl)
        for item in titlez:
            thisTitle.append(item)
        finTitle.append(thisTitle)
    return finTitle

token=JieBaTitle(title)

comNameTitle = []
indexW = []
comCodeTitle = []
indexCode=[]
for index in range(len(token)):
    for indexT in range(len(token[index])):
        for indexV in range(len(comName)):
            if (str(token[index][indexT]) in str(comName[indexV])) and str(comName[indexV]) in str(title[index]) and len(str(fnews3['content'][index])) is not 3:
                # comNameTitle.append(comName[indexV])
                a=1
                indexW.append(index)
#                 print(index)
                indexCode.append(indexV)
#                 print(indexV)
                # comCodeTitle.append(comCode[indexV])
                break
indexOfindexV =[]
SetIndexW=[]
for index in range(len(indexW)):
    if(indexW[index] not in SetIndexW):
        SetIndexW.append(indexW[index])
        indexOfindexV.append(index)
        
        
indexOfCode=[]
for index in indexOfindexV:
    indexOfCode.append(indexCode[index])  
indexNewsA=SetIndexW
indexCodeA=indexOfCode
NewTitle=[]
NewDate=[]
NewContent=[]
for index in indexNews:
#     NewNews.append(fnews['title'])
    NewTitle.append(fnews3['title'][index])
    NewDate.append(fnews3['date'][index])
    NewContent.append(fnews3['content'][index])
codeOftitleA=[]
nameOftitleA=[]
for index in indexCodeA:
    codeOftitleA.append(comCode[index])
    nameOftitleA.append(comName[index])    

date=[]
for datc in NewDate:
    dat=str(datc).replace('月','').replace('年','').replace('日','')[0:8]
    fin=''.join(dat)
    date.append(fin)

dataframe = pd.DataFrame({'title':NewTitle,'date':NewDate,'content':NewContent,'date1':date,'comCodeTitle':codeOftitleA,'comNameTitle':nameOftitleA})
dataframe.to_csv("D:\\Soong\\Soong\\dongfangcaifu\\data\\csv\\PreprofitDayy.csv",index=False,sep=',')















