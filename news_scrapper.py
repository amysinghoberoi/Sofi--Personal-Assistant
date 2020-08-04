# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:33:43 2020

@author: amysi
"""
import pyttsx3
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init("sapi5")
#print(response)
def india():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"India"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait() 

##############################################################

def Your_local_news():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Your local news"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   

#################################################################

def World():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"World"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   
#########################################################################
def Technology():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Technology"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()  
############################################################################

def Entertainment():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Entertainment"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   

##########################################################################
def Sports():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Sports"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   
#########################################################################
def Science():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Science"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   
#########################################################################
def Health():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Health"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   

#########################################################################
def Business():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Business"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]),engine.say(a[:5]),engine.runAndWait()   



































'''


a=[]
url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")
r1=soup.find("div",{"jsname":"V2bVMb"})
r2=r1.find("div",{"aria-label":"Business"})
#print(r2)
h=r2.find("a",class_="SFllF")["href"]
link="https://news.google.com"+h
#print(link)
new=requests.get(link)
soup=BeautifulSoup(new.content,"lxml")
for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
    s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
    s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
    a.append(s3.text)
print(a[:5]) 
    
#print(a[:5]) '''
