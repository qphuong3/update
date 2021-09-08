#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import re
import sched
import smtplib
import time
from requests.api import request
event_schedule = sched.scheduler(time.time, time.sleep)
def emailMe():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('bena1016@gmail.com','ffpctdbtkzcyqsrd')
    subject = 'spending-the-villains-money-to-extend-my-life has been updated'
    body = 'check UpdateNovel'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('bena1016@gmail.com','irischuluck@gmail.com',msg)
    print("email has been sent")
    server.quit()
def works():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('bena1016@gmail.com','ffpctdbtkzcyqsrd')
    subject = 'it still works'
    body = 'check UpdateNovel'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('bena1016@gmail.com','testercodeemail@gmail.com',msg)
    print("email has been sent")
    server.quit()    
while True:
    url = 'https://www.novelupdates.com/series/spending-the-villains-money-to-extend-my-life/'
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    temp = soup.find(id='myTable')
    update = soup.find("a",attrs={"class":"chp-release"})["title"]
    print(update)
    time.sleep(1800)
    if soup.find("a",attrs={"class":"chp-release"})["title"] == update:
        works()
        continue
    else:
        emailMe()