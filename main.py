import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
import sys
from scoreupdate import update
import subprocess


'''ALL INFO BEING TAKEN FROM CRICINFO LIVE SCORECARDS'''

url = "http://static.cricinfo.com/rss/livescores.xml"
h=requests.get(url)
soup=BeautifulSoup(h.text,'html.parser')

i=0
for data in soup.findAll('item'):
    print('['+str(i)+'] '+data.find('description').text)
    i+=1

'''NO ERROR HANDLING INCLUDED BECAUSE USERS ARE EXPECTED TO BE SMART'''
'''ENTER ONLY THE NUMBERS AVAILABLE, ELSE SYSTEM FUCK UP'''
choice=int(input('Enter Match Number: '))
while choice>i or choice<0:
    print('Enter Valid Match')
    choice=int(input('Enter Match Number: '))

scorecard_links=[]
for link in soup.findAll('item'):
    scorecard_links.append(link.find('guid').text)

match_names=[]
for name in soup.findAll('item'):
    match_names.append(name.find('description').text)

match_name=match_names[choice]
match_link=scorecard_links[choice]

print('\n------------------------\n')
print(str(match_name))
print('\n------------------------\n')
print('How would you like to be updated?')
print('[0] Desktop Notifications')
print('[1] Terminal Notifications')
print('[2] Mobile Notifications (NOT AVAILABLE)')
print('[3] Email Notifications (NOT AVAILABLE)')
uchoice=int(input('Enter choice: '))

address=""
'''if uchoice==3:
    address=input('Enter email id: ')
if uchoice==2:
    address=input('Whatever is needed:')
'''

tl=int(input('Enter how often you want a notifiation (seconds):'))

print('\n------------------------')
print('Getting Scorecard Data')
h=requests.get(match_link)
soup=BeautifulSoup(h.text, 'html.parser')
print('Complete!\nEnjoy the game')
print('------------------------')

while 1>0:
    '''sc=requests.get(match_link)
    match=BeautifulSoup(sc.text,'html.parser')
    score=match.findAll('title')
    mess=(score[0].text)
    if uchoice==0:
        mess=(list(mess.split('-'))[0])
        mess=str(mess.split('(')[0])+' | '+str(mess.split('(')[1])    
        notify_desktop(mess)
    if uchoice==1:
        mess=(list(mess.split('-'))[0])
        mess=str(mess.split('(')[0])+'\n'+str(mess.split('(')[1])+'\n------------------------'
        print(mess)'''
    update(match_link, uchoice, address)
    sleep(tl)