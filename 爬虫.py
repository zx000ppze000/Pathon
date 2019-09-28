# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 13:23:19 2019

@author: zhangx
"""


from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html,"lxml")
    texts = bf.find_all('div',class_='showtxt')
    #print(texts)
    
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url = target)
    html = req.text
    div_bf = BeautifulSoup(html,"lxml")
    div = div_bf.find_all('div', class_ = 'listmain')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
         print(each.string, server, each.get('href'))