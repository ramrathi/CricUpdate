import requests
import time
from bs4 import BeautifulSoup
import pynotify
from time import sleep
import sys
import subprocess

def update(match_link, uchoice, address):
	sc=requests.get(match_link)
	match=BeautifulSoup(sc.text,'html.parser')
	score=match.findAll('title')
	mess=(score[0].text)

	if uchoice==0:
		desktop(mess)

	if uchoice==1:
		terminal(mess)
		
	if uchoice==2:

		'''NEED TO ADD FUNCTIONALITY'''
		print('NOT AVAILABLE YET')
	
	if uchoice==3:
		'''NEED TO ADD FUNCTIONALITY'''
		print('NOT AVAILABLE YET')


def desktop(mess):
   
	mess=(list(mess.split('-'))[0])
	mess=str(mess.split('(')[0])+' | '+str(mess.split('(')[1])
	subprocess.Popen(['notify-send', mess])
	return


def terminal(mess):
	mess=(list(mess.split('-'))[0])
	mess=str(mess.split('(')[0])+'\n'+str(mess.split('(')[1])+'\n------------------------'
	print(mess)
	return

def mobile(tile,message):
	return
