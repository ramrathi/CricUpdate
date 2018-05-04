import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
import sys


'''ALL INFO BEING TAKEN FROM CRICINFO LIVE SCORECARDS'''
sc=requests.get('http://www.espncricinfo.com/series/8052/game/1127628/lancashire-vs-somerset--county-championship-division-one-2018/')
match=BeautifulSoup(sc.text,'html.parser')
overs=str(match.find(class_='cscore_overs').text)[1:-1]
print(overs)

batsmen=[str(match.findAll(class_="short-name")[0].text),str(match.findAll(class_="short-name")[1].text)]

print(batsmen)