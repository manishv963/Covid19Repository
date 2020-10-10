
#from rasa_sdk import Action
#from rasa_sdk.events import SlotSet
from gensim.models import Word2Vec
import gensim.downloader as api
from gensim.models import KeyedVectors
import sqlite3
import gensim
import json
import numpy as np
import LoadCovidData
from datetime import timedelta
from rasa_sdk.events import AllSlotsReset

import pandas as pd
from num2words import num2words 
#from rasa_core.events import ReminderScheduled
import spell_corrector as spell
from rasa_sdk.events import SlotSet

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
#
#
from datetime import datetime

import numpy
import arrow

 
def compareTime():
    try:
        dbTime = InsertRefreshData.get_refresh_date_time()
        currentTime =InsertRefreshData.getCurrentTime()
        print('dbTime',dbTime)
        print('curr_time',currentTime)
        databaseTime = datetime.strptime(dbTime, '%M:%S')
        currentTime = datetime.strptime(currentTime, '%M:%S')
        if(dbTime == ''):
            InsertRefreshData.insert_refresh_data()
        print("current time is ",currentTime)
        if (currentTime > databaseTime):
            InsertRefreshData.insert_refresh_data()
            print("curent time greate")
            ActionRefreshCovidData.refreshDatainSql()
        return "success"
    except:
        print("no data")
        InsertRefreshData.insert_refresh_data()
        dbTime = InsertRefreshData.get_refresh_date_time()
        currentTime =InsertRefreshData.getCurrentTime()
        print('dbTime',dbTime)
        print('curr_time',currentTime)
        databaseTime = datetime.strptime(dbTime, '%M:%S')
        currentTime = datetime.strptime(currentTime, '%M:%S')
        if(dbTime == ''):
            InsertRefreshData.insert_refresh_data()
        
        if (currentTime > databaseTime):
            InsertRefreshData.insert_refresh_data()
            print("curent time greate")
            ActionRefreshCovidData.refreshDatainSql()
        return "success"

def validate_country_name(coutryName):
    
    coutryName = coutryName.replace(' ','_')
    print(coutryName)
    f = open("countrRegionList.txt", "r")
    countryNameList = []
    for countryNameFromList in f: 
        countryNameFromList = countryNameFromList.lower()
        countryNameFromList = countryNameFromList.replace('\n','')
        countryNameList.append(countryNameFromList)
    f.close()
    #print(countryNameList)
    if coutryName not in countryNameList:
            newName = spell.rectify(coutryName)
            if newName not in countryNameList:
                return "not_valid"
            else:
                newName = spell.rectify(coutryName)
                return newName
    else:
        return coutryName
def get_cosine_similarity(feature_vec_1, feature_vec_2):    
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]
def getSentenceEmbedding(sentence,model):
    absentFlag =False
    lisofwords= sentence.split()
    
    #if "coronavirus" not in  lisofwords :
        #absentFlag =True
        #lisofwords.append("coronavirus")

    
     
    vec =np.array([0]* len(model['russia'])) ### len(glove_model['hi'] this is the list of sample embedding from model 
    for word in lisofwords:
        if word == "corona":
            pass
        if word == "covid-19":
            pass
        try:
            
            vec = vec  + np.array(model[word])
        except:
            vec = vec  +np.array([0]* len(model['hi']))
    return vec.reshape(1,-1)
#numpy.array(glove_model['hi'])+ numpy.array(glove_model['hi'])

v2w_model = None

def loadWordEmbeddingsModel():
    v2w_modelLoaded = None
    try:
        print("loading w2v model from local dist")
        v2w_modelLoaded = gensim.models.KeyedVectors.load("../glove-wiki-gigaword-300.mod")
        return v2w_modelLoaded
        print("w2v model loaded")
    except:
        return v2w_modelLoaded  
        #v2w_model =api.load('glove-wiki-gigaword-300.mod')
        #v2w_model.save('./glove-wiki-gigaword-300.mod')
        #print("word2vecmodel loaded")

v2w_model = loadWordEmbeddingsModel()
print(type(v2w_model))

total = getSentenceEmbedding("total number of cases ",v2w_model)

class ActionAllCases(Action):
    
    def __init__(self):
        #v2w_model = loadWordEmbeddingsModel()

        total = getSentenceEmbedding("total number of cases ",v2w_model)
        print(total.shape)
    def name(self):
        return "action_showAllDetails"
    
    def run(self, dispatcher,tracker,domain) :
   
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  country,totalCases,deaths,recovered,activeCases,seriousCases,totalTest FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        validationResult = validate_country_name(country)
        if validationResult == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            dispatcher.utter_message(text="Country/Region : "+row[0])
            dispatcher.utter_message(text="Total Cases : "+num2words(row[1]) + "("+str(row[1])+")")
            dispatcher.utter_message(text="Total Deaths : "+num2words(row[2]) + "("+str(row[2])+")")
            dispatcher.utter_message(text="Recovered Cases : "+num2words(row[3]) + "("+str(row[3])+")")
            dispatcher.utter_message(text="Active Cases : "+num2words(row[4]) + "("+str(row[4])+")")
            dispatcher.utter_message(text="Serious_Cases : "+num2words(row[5]) + "("+str(row[5])+")")
            dispatcher.utter_message(text="Total Test : "+num2words(row[6]) + "("+str(row[6])+")")
        compareTime()
        return[SlotSet('region',country)]
        
        
class ActionShowTotalCases(Action):
    

    def name(self):
        return "action_showTotalCases"
    
    def run(self, dispatcher,tracker,domain) :
    
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  totalCases FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Total Cases in  "+country + " are "+ num2words(row[0])+ "(" + str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)]
        
        

class ActionShowDeaths(Action):
    

    def name(self):
        return "action_showDeaths"
    
    def run(self, dispatcher,tracker,domain) :
    
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  deaths FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Total Deaths in  "+country + " are "+ num2words(row[0])+ "("  +  str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)]



class ActionShowTotalTest(Action):
    

    def name(self):
        return "action_showTotalTest"
    
    def run(self, dispatcher,tracker,domain) :
    
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  totalTest FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Total Test conducted by  "+country + " are "+ num2words(row[0])+ "("  +  str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)] 
class ActionValidateLocation(Action):
    
    
    def name(self):
       return "action_validate_location"
    
    def run(self, dispatcher,tracker,domain) :
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        if country == "not_valid":
            dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
            
            return[SlotSet('region','')] 
        else:
             return[SlotSet('region',country)] 
 
class ActionShowSerious(Action):
    

    def name(self):
        return "action_showSerious"
    
    def run(self, dispatcher,tracker,domain) :
    
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  seriousCases FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Total Serious cases in  "+country + " are "+ num2words(row[0])+ "("  +str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)] 
        
class ActionShowRecovered(Action):
    

    def name(self):
        return "action_showRecovered"
    
    def run(self, dispatcher,tracker,domain) :
    
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  recovered FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Total Recovered cases in  "+country + " are "+ num2words(row[0])+ "("  +str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)] 


class ActionShowActive(Action):
    

    def name(self):
        return "action_showActive"
    
    def run(self, dispatcher,tracker,domain) :
    
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  activeCases FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Active cases in  "+country + " are "+ num2words(row[0])+ "("  +str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)] 


class ActionShowTotalCases(Action):
    

    def name(self):
        return "action_showTotalCases"
    
    def run(self, dispatcher,tracker,domain) :
  
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("connection successful")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        print("1")
        sqlSelctQuery = ' SELECT  totalCases FROM  data where country = ?'
        country = tracker.get_slot('region')
        country = str(country).lower()
        country = validate_country_name(country)
        print(country)
        if country == "not_valid":
             dispatcher.utter_message("Please Specify Valid Country/Region Name. ")
             conn.close()
             return None
        print("2")
        params = (country,)
        print("2")
        cursor.execute(sqlSelctQuery,params)
        print("4")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
            dispatcher.utter_message(text="Total Cases in  "+country + " are "+ num2words(row[0])+ "("  + str(row[0])+ ")")
        compareTime()    
        return[SlotSet('region',country)]
        
        



class ActionRefreshCovidData():
    
    
    def refreshDatainSql() :
        rviousCase = LoadCovidData.load_refresh_data(0)
        df = pd.read_csv ('data.csv')
        
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("Asas")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        sql = ' DELETE FROM  data'
        print("Asas1")
        cursor.execute(sql)
        sql = 'INSERT INTO data(country,totalCases,deaths,recovered,activeCases,seriousCases,totalTest)  VALUES(?,?,?,?,?,?,?) '

        count = 0
        countryNameList = []
        for ind in df.index:
            if( df['Country/Region'][ind] in countryNameList):
                continue
            countryNameList.append(df['Country/Region'][ind].replace(' ' ,'_'))
            #print( str(df['Country/Region'][ind]).lower().replace(' ' ,'_'))
            data = ( str(df['Country/Region'][ind]).lower().replace(' ' ,'_'),str(df['Total_Cases'][ind]),
            str(df['Deaths'][ind]),
                str(df['Recovered_Cases'][ind]),
                str(df['Active_Cases'][ind]),
                str(df['Serious_Cases'][ind]),
                str(df['Total_Test'][ind]))
            #print(data) 
            cursor.execute(sql, data)
        count = count+1
        print(count)
        conn.commit()
        conn.close()
    
            

###this action is called after the remainder is triggered because it is necesssary to call any othe raction after event remainder action is triggered other wise the bot will run any random action
class ActionRandomEvent(Action):
    
    def name(self):
        return "action_random_event_after_reminder"
    
    def run(self, dispatcher,tracker,domain) :
        
        dispatcher.utter_message(text="AIsa hi")
   
       
            
       
class InsertRefreshData:
    
    def getCurrentTime():
        now = datetime.now()
        return str(now)[11:16]
    
    def insert_refresh_data() :
        
        conn = None
        try:
            conn = sqlite3.connect('./coronaFromWebScrappingDatabase.db')
            print("connected success")
        except Exception as e:
            print(e)
        
        cursor = conn.cursor()
        sql = ''' INSERT INTO refresh_data(refresh_date_time)  VALUES(?) '''
        
    
        now = datetime.now()
        now_plus_10m = now + timedelta(minutes = 5)
        
        data = (str(now_plus_10m),)
        
        cursor.execute(sql,data)
        print("1")
        conn.commit()
        conn.close()
        ActionRefreshCovidData.refreshDatainSql()
      
        return None
    def get_refresh_date_time():
        conn = None
        try:
            conn = sqlite3.connect('coronaFromWebScrappingDatabase.db')
            print("conn success")
        except Exception as e:
            print(e)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM refresh_data ORDER BY rowid DESC LIMIT 1;")
        data = cursor.fetchall()
        dt = arrow.get(data[0][0])
        dbTime = str(dt.time())[0:5]
        conn.commit()
        conn.close()
        return dbTime

class ActionResetSlot(Action):
    def name(self) :
            return "action_reset_slot"
    def run(self, dispatcher,tracker,domain):
        return [AllSlotsReset()]    