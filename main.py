# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:42:36 2020

@author: aman"""
import pandas as pd
import pyttsx3
import datetime
import train_list
from textblob.classifiers import NaiveBayesClassifier
import speech_recog 
import speech_recognition as sr
import pyowm
import time
import re
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import nltk
import smtplib
import json
from flask import jsonify
import pprint
from pandas.io.json import json_normalize
import folium 
from geopy.geocoders import Nominatim 
import requests
import json
import webbrowser
from selenium import webdriver
import time
import os
import random
nltk.download('punkt')
from tkinter import *
#root=Tk()
#root.geometry("500x400")
engine = pyttsx3.init("sapi5")
engine.say("Hi, i am sofi, your virtual assistant. What can i help you with?")
engine.runAndWait()
print("Hi, i am sofi, your virtual assistant. What can i help you with?")
data1=train_list.train
cl=NaiveBayesClassifier(data1)
if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)
    response = speech_recog.recognize_speech_from_mic(recognizer, microphone)


print(cl.classify(response))

##############################1111111111111111111111111111#############################################
#speech_recog.engine.say(cl.classify(response))
#speech_recog.engine.runAndWait()

if cl.classify(response)== "wquery":
    #https://home.openweathermap.org/api_keysimport pyowm
    
   
    
    d="http://api.ipstack.com/103.46.200.101?access_key=56cb4835a5e0ef67b356fccb7387e780"
    response1=requests.get(d)
    a=response1.json()
#print(a['latitude'],a['longitude'])
    la=a['latitude']
    lo=a['longitude']
    re=a['region_name']
    co=a['region_code']
    owm = pyowm.OWM('8edf181ff931f273b55166139bb0b7b3')
    observation = owm.weather_at_place(str(re))
    w = observation.get_weather()
    engine.say("today's temperature is {}, maximum and minimum temperature are {} and {} respectively".format(w.get_temperature('celsius')['temp'],w.get_temperature('celsius')['temp_max'],w.get_temperature('celsius')['temp_min'])),engine.runAndWait()
    print("Sofi: Today's temperature is {}, the wind speed is {} and humidity is {}".format(w.get_temperature('celsius'),w.get_wind(),w.get_humidity()))
    
    #print(w.get_wind())
    #print(w.get_humidity())
    
    
   # label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
    #label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
    #label3=Label(root,text="Sofi: Today's temperature is {}, the wind speed is {} and humidity is {}".format(w.get_temperature('celsius'),w.get_wind(),w.get_humidity(),font=("Times", 15)).place(x=10,y=100)
    #root.title('SofiBot')
    #root.mainloop()
#w.get_wind()
#w.get_humidity()
#w.get_temperature('celsius')
########################################2222222222222222222222222222222#####################################    

elif cl.classify(response)=="greeting":
    day_time = int(time.strftime('%H'))
    
    if day_time < 12:
        engine.say('Hello Sir. Good morning'),engine.runAndWait()
        #label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
        #label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
        #label3=Label(root,text="Sofi: Hello Sir. Good morning" ,font=("Times", 15)).place(x=10,y=100)
        #root.title('SofiBot')
        #root.mainloop()
        print('Hello Sir. Good morning')
    elif 12 <= day_time < 18:
        engine.say('Hello Sir. Good afternoon'),engine.runAndWait()
        #label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
        #label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
        #label3=Label(root,text="Sofi: Hello Sir. Good afternoon" ,font=("Times", 15)).place(x=10,y=100)
        #root.title('SofiBot')
        #root.mainloop()
        print('Hello Sir. Good afternoon')
    else:
        engine.say('Hello Sir. Goodevening '),engine.runAndWait()
        #label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
        #label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
        #label3=Label(root,text="Sofi: Hello Sir. Good evening" ,font=("Times", 15)).place(x=10,y=100)
        #root.title('SofiBot')
        #root.mainloop()
        print('Hello Sir. Goodevening')
##############################3333333333333333333333333333333333333#########################################        
elif cl.classify(response)=="time":
    time=datetime.datetime.now()
    engine.say("the time is {} hours and {} minutes".format(time.hour,time.minute)),engine.runAndWait();
    print("the time is {} hours and {} minutes".format(time.hour,time.minute))
    
    #label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
    #label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
    #label3=Label(root,text="Sofi: The time is {} hours and {} minutes".format(time.hour,time.minute) ,font=("Times", 15)).place(x=10,y=100)
    #root.title('SofiBot')
    #root.mainloop()
##########################444444444444444444444444444444444444444444444444444###########################      

elif cl.classify(response)=="yt":
    engine.say('what do you want to play, sir'),engine.runAndWait();
    query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    browser=webdriver.Chrome()
#time.sleep(2)
    query=query.replace(" ","+")
    browser.get("https://www.youtube.com/results?search_query="+query)
    select=browser.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
    select.click()
    
   # label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
    #label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
    #label3=Label(root,text="Sofi: What do you want to play, sir" ,font=("Times", 15)).place(x=10,y=100)
    #label4=Label(root,text="Me: {}".format(query) ,font=("Times", 15)).place(x=10,y=140)
    #label5=Label(root,text="Sofi: Your query has been generated, sir" ,font=("Times", 15)).place(x=10,y=180)
    #root.title('SofiBot')
    #root.mainloop()
    
    
############################55555555555555555555555555555555555##############################################    
elif cl.classify(response)=="google":
    engine.say('what do you want to search, sir'),engine.runAndWait();
    query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    browser=webdriver.Chrome()
#time.sleep(2)
    query=query.replace(" ","+")
    browser.get("https://www.google.com/search?q="+query+"&oq=justin&aqs=chrome..69i57.2236j0j8&sourceid=chrome&ie=UTF-8=")
    
   # label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
   # label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
   # label3=Label(root,text="Sofi: what do you want to search, sir" ,font=("Times", 15)).place(x=10,y=100)
   # label4=Label(root,text="Me: {}".format(query) ,font=("Times", 15)).place(x=10,y=140)
   # label5=Label(root,text="Sofi: Your query has been generated, sir" ,font=("Times", 15)).place(x=10,y=180)
   # root.title('SofiBot')
   # root.mainloop()
    
############################6666666666666666666666666666666666666############################################  
elif cl.classify(response)=="mail":
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('amannnoberoiii@gmail.com','PROJECTPASSWORD101')
    engine.say('what do you want the subject to be, sir'),engine.runAndWait();
    subject=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    time.sleep(2)
    engine.say('what do you want the message to be, sir'),engine.runAndWait();
    body=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
            'amannnoberoiii@gmail.com','amysingh.oberoi@gmail.com',msg
            )
    
    engine.say('mail sent'),engine.runAndWait();
    
  #  label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
   # label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
   # label3=Label(root,text="Sofi: what do you want the subject to be, sir" ,font=("Times", 15)).place(x=10,y=100)
   # label4=Label(root,text="Me: {}".format(subject) ,font=("Times", 15)).place(x=10,y=140)
   # label5=Label(root,text="Sofi: what do you want the message to be, sir ",font=("Times", 15)).place(x=10,y=180)
   # label6=Label(root,text="Me: {}".format(body) ,font=("Times", 15)).place(x=10,y=220)
   # label7=Label(root,text="Sofi: mail sent" ,font=("Times", 15)).place(x=10,y=260)
   # root.title('SofiBot')
   # root.mainloop() 
###########################77777777777777777777777777777777777777777777########################################    
elif cl.classify(response)=="covid":
    
    re_pattern = r'\bworld.*?\b'
    m=re.findall(re_pattern, response)
    if str(m) in response:
        r2=requests.get('https://coronavirus-19-api.herokuapp.com/all')
        r=r2.json()
        print("the total number of cases are {} where {} died and {} recovered".format(r['cases'],r['deaths'],r['recovered']))
        engine.say("the total number of cases are {} where {} died and {} recovered".format(r['cases'],r['deaths'],r['recovered'])),engine.runAndWait()
    #    label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
     #   label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
     #   label3=Label(root,text="Sofi: the total number of cases are {} where {} died and {} recovered".format(r['cases'],r['deaths'],r['recovered']) ,font=("Times", 15)).place(x=10,y=100)
     #   root.title('SofiBot')
     #   root.mainloop() 
        
        
        
        
    else:
        engine.say('please choose the country of consideration'),engine.runAndWait()
        country=speech_recog.recognize_speech_from_mic(recognizer, microphone)
        response=requests.get('https://coronavirus-19-api.herokuapp.com/countries/'+country)
        #response1=requests.get('https://coronavirus-19-api.herokuapp.com/countries')
        #r3=requests.get(' https://api.covid19india.org/raw_data.json')
        r=response.json()
        print("the total number of cases are {} where {} died and {} recovered in {}".format(r['cases'],r['deaths'],r['recovered'],r['country']))    
        engine.say("the total number of cases are {} where {} died and {} recovered in {}".format(r['cases'],r['deaths'],r['recovered'],r['country'])),engine.runAndWait()
     #   label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
     #   label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
      #  label3=Label(root,text="Sofi: the total number of cases are {} where {} died and {} recovered in {}".format(r['cases'],r['deaths'],r['recovered'],r['country']) ,font=("Times", 15)).place(x=10,y=100)
      #  root.title('SofiBot')
      #  root.mainloop()
 
###################################8888888888888888888888888888888888888888########################################
        
        
elif cl.classify(response)=="news":
    import news_scrapper
    engine.say('please select the subject of news, sir'),engine.runAndWait();
    #india
    #local news
    #world
    #technology
    #entertainment
    #sports
    #science
    #health
    #buisness
    sub=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    print(sub)
    if sub == "India" :
        news_scrapper.india()
    elif sub == "local news":
        news_scrapper.Your_local_news()
    elif sub == "World" :
        news_scrapper.World()
    elif sub == "Technology" :
        news_scrapper.Technology()
    elif sub == "entertainment" :
        news_scrapper.Entertainment()
    elif sub == "Sports" :
        news_scrapper.Sports()
    elif sub == "Science" :
        news_scrapper.Science()
    elif sub == "health" :
        news_scrapper.Health()     
    elif sub == "buisness" :
        news_scrapper.Business()       
    else:
        engine.say("try again"),engine.runAndWait();

#####################################99999999999999999999999999999999###########################################


elif cl.classify(response)=="events":
    
    d="http://api.ipstack.com/103.46.200.101?access_key=56cb4835a5e0ef67b356fccb7387e780"
    response1=requests.get(d)
    a=response1.json()
#print(a['latitude'],a['longitude'])
    la=a['latitude']
    lo=a['longitude']
    re=a['region_name']
    co=a['region_code']

    print(la,lo)
    def get_category_type(row):
        try:
            categories_list = row['categories']
        except:
            categories_list = row['venue.categories']
        
        if len(categories_list) == 0:
            return None
        else:
            return categories_list[0]['name']



    CLIENT_ID='4CWXIQQONROMXHF4NUWUQTDMUOVZL2XUXZCGX44TCSFJFHD3'
    CLIENT_SECRET='ZNV0XDDP3QZGUO0P53DP4VFBKZAHGVF4EXNG44XCGJRMTSEM'
    VERSION='20180323'
    neighborhood_latitude=str(la)
    neighborhood_longitude=str(lo)
    radius=2000
    LIMIT=100
    engine.say('what events are you searching for, sir'),engine.runAndWait()
    SECTION=speech_recog.recognize_speech_from_mic(recognizer, microphone)#food, drinks, coffee, shops, arts, outdoors, sights, trending, nextVenues, or topPicks
    url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}&section={}'.format(
        CLIENT_ID, 
        CLIENT_SECRET, 
        VERSION, 
        neighborhood_latitude, 
        neighborhood_longitude, 
        radius, 
        LIMIT,
        SECTION
        )
    results = requests.get(url).json()
    #print(results)
    venues = results['response']['groups'][0]['items']
    nearby_venues = json_normalize(venues)
    # filter columns
    filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
    nearby_venues =nearby_venues.loc[:, filtered_columns]
    # filter the category for each row
    nearby_venues['venue.categories'] = nearby_venues.apply(get_category_type, axis=1)
    # clean columns
    nearby_venues.columns = [col.split(".")[-1] for col in nearby_venues.columns]
    print(nearby_venues)
    
    venues_map = folium.Map(location=[neighborhood_latitude, neighborhood_longitude], zoom_start=15)
    # add a red circle marker to represent the BEDOKVILLE
    folium.CircleMarker(
        [neighborhood_latitude, neighborhood_longitude],
        radius=10,
        color='red',
        popup='my location',
        fill = True,
        fill_color = 'red',
        fill_opacity = 0.6
    ).add_to(venues_map)
    # add all venues as blue circle markers
    for name, lat, lng, label in zip(nearby_venues.name, nearby_venues.lat, nearby_venues.lng, nearby_venues.categories):
        folium.CircleMarker(
            [lat, lng],
            radius=5,
            color='blue',
            popup=name,
            fill = True,
            fill_color='blue',
            fill_opacity=0.6
        ).add_to(venues_map)
    
    
    venues_map.save("map.html")
    webbrowser.open("map.html")
#    label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
 #   label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
 #   label3=Label(root,text="Sofi: Your query has been generated" ,font=("Times", 15)).place(x=10,y=100)
 #   root.title('SofiBot')
 #   root.mainloop()
#######################################1010101001010101010101010101010101010##################################    
    
elif cl.classify(response)=="insta":
    engine.say('what are you searching for, sir'),engine.runAndWait()
    query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    driver=webdriver.Chrome()
    time.sleep(2)
    driver.get('https://instagram.com/accounts/login')
    time.sleep(2)
    login=driver.find_element_by_name('username').send_keys("amanoberoi1111")
    password=driver.find_element_by_name('password').send_keys("Instagrampassword123")
    enter=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
    time.sleep(4)
    pop1=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
    time.sleep(3)
    search=driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(query)
    time.sleep(10)
    follow1=driver.find_element_by_class_name('yCE8d').click() 
    
#    label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
#    label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
#    label3=Label(root,text="Sofi: what are you searching for, sir" ,font=("Times", 15)).place(x=10,y=100)
#    label4=Label(root,text="Me: {}".format(query)+"\n",font=("Times", 15)).place(x=10,y=140)
#    label5=Label(root,text="Sofi: Your query has been generated" ,font=("Times", 15)).place(x=10,y=180)
#    root.title('SofiBot')
#    root.mainloop()
##############################################11111111111111111111111#######################################
elif cl.classify(response)=="fb":
    engine.say('what are you searching for, sir'),engine.runAndWait()
    query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    driver=webdriver.Chrome()
    username="aaoobbeerrooii@gmail.com"
    pas="Facebookpassword123"
    time.sleep(2)
    driver.get('https://www.facebook.com/')
    time.sleep(4)
    login=driver.find_element_by_id('email').send_keys(username)
    password=driver.find_element_by_id('pass').send_keys(pas)
    ent=driver.find_element_by_id('loginbutton').click()
    time.sleep(2)
    search=driver.find_element_by_class_name('_1frb').send_keys(query)
    time.sleep(10)
    #find=driver.find_element_by_xpath('//*[@id="js_g"]/form/button').click()
    #time.sleep(2)
    query1=driver.find_element_by_class_name('_19bs').click()
    #ent=driver.find_element_by_xpath('//*[@id="facebar_typeahead_view_list"]/div[1]/li/div/a').click()
    time.sleep(3)
    query2=driver.find_element_by_class_name('_6xu6').click()
    
#    label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
#    label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
#    label3=Label(root,text="Sofi: what are you searching for, sir" ,font=("Times", 15)).place(x=10,y=100)
#    label4=Label(root,text="Me: {}".format(query)+"\n",font=("Times", 15)).place(x=10,y=140)
#    label5=Label(root,text="Sofi: Your query has been generated" ,font=("Times", 15)).place(x=10,y=180)
#    root.title('SofiBot')
#    root.mainloop()
#############################121212121212121212121212######################################################

elif cl.classify(response)=="translate":
    
    
    engine.say('do you want to translate or detect the language?, sir'),engine.runAndWait()
    q=speech_recog.recognize_speech_from_mic(recognizer, microphone)
#    label1=Label(root,text="Sofi: Hi, i am sofi, your virtual assistant. What can i help you with? \n",font=("Times", 15)).place(x=10,y=20)
#    label2=Label(root,text="Me: {}".format(response)+"\n",font=("Times", 15)).place(x=10,y=60)
 #   label3=Label(root,text="Sofi: do you want to translate or detect the language?, sir" ,font=("Times", 15)).place(x=10,y=100)
 #   label4=Label(root,text="Me: {}".format(q)+"\n",font=("Times", 15)).place(x=10,y=140)
    if str(q)=="detect":
        from googletrans import Translator
        translator = Translator()
        engine.say('please speak now, sir'),engine.runAndWait()
        query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
        m=translator.detect(query)
        engine.say(m),engine.runAndWait()
        print(m)
  #      label5=Label(root,text="Me: detect",font=("Times", 15)).place(x=10,y=180)
   #     label6=Label(root,text="Sofi: please speak now, sir" ,font=("Times", 15)).place(x=10,y=220)
    #    label7=Label(root,text="Me: {}".format(query)+"\n",font=("Times", 15)).place(x=10,y=260)
     #   label8=Label(root,text="Sofi: {}".format(m),font=("Times", 15)).place(x=10,y=300)
      #  root.title('SofiBot')
       # root.mainloop()
        
        
        

    elif str(q)=="translate":
        from translate import Translator
        engine.say('select language, sir'),engine.runAndWait()
        query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
        translator= Translator(to_lang=query)
        engine.say('speak now, sir'),engine.runAndWait()
        query1=speech_recog.recognize_speech_from_mic(recognizer, microphone)
        translation = translator.translate(query1)
        print(translation)
        engine.say(translation),engine.runAndWait()
#        label5=Label(root,text="Me: translate",font=("Times", 15)).place(x=10,y=180)
 #       label6=Label(root,text="Sofi: select language, sir" ,font=("Times", 15)).place(x=10,y=220)
  #      label7=Label(root,text="Me: {}".format(query)+"\n",font=("Times", 15)).place(x=10,y=260)
    #    label8=Label(root,text="Sofi: speak now, sir",font=("Times", 15)).place(x=10,y=300)
     #   label9=Label(root,text="Me: {}".format(query1),font=("Times", 15)).place(x=10,y=340)
      #  label10=Label(root,text="Sofi: {}".format(translation),font=("Times", 15)).place(x=10,y=380)
       # root.title('SofiBot')
        #root.mainloop()

################################131313131313131313313131313##################################################
elif cl.classify(response)=="bms":
    import re
    engine.say('do you want to know events or movies?, sir'),engine.runAndWait()
    query=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    r1= r'\b(?:event|events|Event|Events)\b'
    r2= r'\b(?:movies|movie|Movies|Movie)\b'
    m=re.findall(r1,query)
    n=re.findall(r2,query)
    if str(m)=="events" or "event":
        url="https://in.bookmyshow.com/national-capital-region-ncr/events"
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'lxml')
            
        p=[]
        m=[]
        for a in soup.find_all("a",{"style":"text-decoration:none"}):
            titles=a.get('title')
            hre=a.get('href')
            p.append(titles)
            m.append(hre)
        print(p[:5])    
        engine.say(p[0]),engine.runAndWait()
        engine.say(p[1]),engine.runAndWait()
        engine.say(p[2]),engine.runAndWait()
        engine.say(p[3]),engine.runAndWait()
        engine.say(p[4]),engine.runAndWait()
       # engine.say('which event do you want to go for?'),engine.runAndWait()    
        #user=speech_recog.recognize_speech_from_mic(recognizer, microphone)
        #browser=webdriver.Chrome()
        
        #browser.get(url+p[int(user)])    
        #print(p[:5])
    
            
            
    elif str(n)=="movies" or "movie":
        url="https://in.bookmyshow.com/national-capital-region-ncr/movies"
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'lxml')
        f2=soup.find("div",{"class":"listing-tabs movies-listing-tabs"})
        m=[]
        for f in f2.find_all("a"):
            movies=f.get("data-toggle")
            m.append(movies)
        engine.say(m[0]),engine.runAndWait()    
        engine.say(m[1]),engine.runAndWait()
        engine.say('which movie do you want to go for?'),engine.runAndWait()    
        user=speech_recog.recognize_speech_from_mic(recognizer, microphone)
        browser=webdriver.Chrome()
        browser.get(url+m[int(user)])
        print(m[:2])    
#####################################1414141414141414141414144141########################################    
elif cl.classify(response)=="zomato":
    d="http://api.ipstack.com/103.46.200.101?access_key=56cb4835a5e0ef67b356fccb7387e780"
    response=requests.get(d)
    a=response.json()
#print(a['latitude'],a['longitude'])
    lat=a['latitude']
    lon=a['longitude']
    re=a['region_name']
    co=a['region_code']
    url='https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'.format(lat,lon)
    headers={"user-key": "8f9038836ecbfd8b4938ba7627d29e06"}
    results = requests.get(url,headers=headers).json()


    m1=results['nearby_restaurants'][0]['restaurant']['name'],results['nearby_restaurants'][0]['restaurant']['location']['locality']                                     
    m2=results['nearby_restaurants'][1]['restaurant']['name'],results['nearby_restaurants'][1]['restaurant']['location']['locality']  
    m3=results['nearby_restaurants'][2]['restaurant']['name'],results['nearby_restaurants'][2]['restaurant']['location']['locality']  
    m4=results['nearby_restaurants'][3]['restaurant']['name'],results['nearby_restaurants'][3]['restaurant']['location']['locality']  
    m5=results['nearby_restaurants'][4]['restaurant']['name'],results['nearby_restaurants'][4]['restaurant']['location']['locality']  
    
    engine.say("some of the cuisines and restaurants near you are the following:"),engine.runAndWait()
    print(m1,m2,m3,m4,m5)
    engine.say(m1[1]),engine.runAndWait()
    engine.say(m1[0]),engine.runAndWait()
    
    engine.say(m2[1]),engine.runAndWait()
    engine.say(m2[0]),engine.runAndWait()
    
    engine.say(m3[1]),engine.runAndWait()
    engine.say(m3[0]),engine.runAndWait()
    
    engine.say(m4[1]),engine.runAndWait()
    engine.say(m4[0]),engine.runAndWait()
    
    engine.say(m5[1]),engine.runAndWait()
    engine.say(m5[0]),engine.runAndWait()



#############################################15151551551515151515151515515#####################################################################

elif cl.classify(response)=="movie":
     
     engine.say('select the genre, sir'),engine.runAndWait();
     #'Comedy,'Romance','Thriller','Family','Adventure','Crime','Action','Science Fiction',
     #'Music','History','Drama','Mystery','Horror','TV Movie','Foreign','Fantasy','Documentary','Animation'
     #or most liked
     genre1=speech_recog.recognize_speech_from_mic(recognizer, microphone)
     genre1=genre1.title()
     #genre1=pd.Series(genre1)
     print(genre1)
     import pandas as pd
     from ast import literal_eval
     import numpy as np
     md = pd.read_csv("C:/Users/amysi/Desktop/datasets/movie_dataset/movies_metadata.csv")

#print(md)
     md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
     vote_counts = md[md['vote_count'].notnull()]['vote_count'].astype('int')
     vote_averages = md[md['vote_average'].notnull()]['vote_average'].astype('int')
     C = vote_averages.mean()
#print(C)
     m = vote_counts.quantile(0.95)
     md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
     qualified = md[(md['vote_count'] >= m) & (md['vote_count'].notnull()) & (md['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity', 'genres']]
     qualified['vote_count'] = qualified['vote_count'].astype('int')
     qualified['vote_average'] = qualified['vote_average'].astype('int')
     def weighted_rating(x):
         v = x['vote_count']
         R = x['vote_average']
         return (v/(v+m) * R) + (m/(m+v) * C)
     qualified['wr'] = qualified.apply(weighted_rating, axis=1)
     qualified = qualified.sort_values('wr', ascending=False).head(250)
     #qualified["title"][:10])
     
     s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
     s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
     s.name = 'genre'
     gen_md = md.drop('genres', axis=1).join(s)
     def build_chart(genre, percentile=0.85):
         df = gen_md[gen_md['genre'] == genre]
         vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
         vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
         C = vote_averages.mean()
         m = vote_counts.quantile(percentile)
    
         qualified1 = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
         qualified1['vote_count'] = qualified1['vote_count'].astype('int')
         qualified1['vote_average'] = qualified1['vote_average'].astype('int')
    
         qualified1['wr'] = qualified1.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
         qualified1 = qualified1.sort_values('wr', ascending=False).head(10)
    
         return qualified1
     m=[]
     for a in build_chart(str(genre1))["title"][0:5]:
            m.append(a)
     print(m)      
     engine.say(m[0:5]),engine.runAndWait();
    

    

########################################################161616161616616161166116161616########################################################################################



elif cl.classify(response)=="whatsapp":
    from twilio.rest import Client
    engine.say("what's your message, sir"),engine.runAndWait()
    query=speech_recog.recognize_speech_from_mic(recognizer, microphone)


    #failsafe ssd27krvS7zWIQ0Xvfk8xig9MSxDocvbKT6cm75d
    twilio_sid='AC415618dac9582515c6d5803d2e96090b'
    auth_token='e85b0894532a1fdf92af51c13b13d6b6'
    
    # whstapp on +14155238886 join sign-zulu,join wire- light
    
    client=Client(twilio_sid,auth_token)
    
    contact_dir={'anshul':'+918882222116','aakash':'+918285246803'}
    
   # engine.say("what's your message?, sir"),engine.runAndWait()
    for key,value in contact_dir.items():
        msg=client.messages.create(body=query
                               ,from_='whatsapp:+14155238886'
                               ,to='whatsapp:'+value,
                               )
        print("message sent")
    engine.say("message sent, sir"),engine.runAndWait()

###########################################1717171717171717111711717################################   
    
    

elif cl.classify(response)=="files":  
    engine.say("what do you want to open, sir"),engine.runAndWait()
    command=speech_recog.recognize_speech_from_mic(recognizer, microphone)
    notepad_re=r'\b(?:notepad|Notepad|notes)\b'
    query=re.findall(notepad_re,command)
    if str(query) in command:
        os.startfile(r"C:\Users\amysi\Desktop\datasets\apps\notepad.txt")
        engine.say("Your query has been generated, sir"),engine.runAndWait()
         
    excel_re=r'\b(?:excel|Excel|access|sheets)\b'
    query=re.findall(excel_re,command)
    if str(query) in command:
        os.startfiler(r"C:\Users\amysi\Desktop\datasets\apps\excel.xlsx")
        engine.say("Your query has been generated, sir"),engine.runAndWait()
       
         
    ppt_re=r'\b(?:powerpoint|Powerpoint|ppt)\b'
    query=re.findall(ppt_re,command)
    if str(query) in command:
        os.startfile(r"C:\Users\amysi\Desktop\datasets\apps\ppt.pptx")
        engine.say("Your query has been generated, sir"),engine.runAndWait()

    word_re=r'\b(?:word|Word|Document|document)\b'
    query=re.findall(word_re,command)
    if str(query) in command:
        os.startfile(r"C:\Users\amysi\Desktop\datasets\apps\word.docx")
        engine.say("Your query has been generated, sir"),engine.runAndWait()    

    pic_re=r'\b(?:images|Images|picture|pictures)\b'
    query=re.findall(pic_re,command)
    if str(query) in command:
        os.startfile(r"C:\Users\amysi\Desktop\datasets\apps\pic1.jpg")
        engine.say("Your query has been generated, sir"),engine.runAndWait()

    song_re=r'\b(?:song|songs|music)\b'
    query=re.findall(song_re,command)
    if str(query) in command:
        os.startfile(r"C:\Users\amysi\Desktop\datasets\apps\song1.mp3")
        engine.say("Your query has been generated, sir"),engine.runAndWait()
        
        
        
########################################################################################################################        
        
  
else:
     engine.say("Can't recognize your command, please try again"),engine.runAndWait()
    
    
    
    








   


    
    
    
    
 
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    



        