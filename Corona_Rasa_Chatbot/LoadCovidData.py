#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests, bs4
import time
import pandas as pd
def load_refresh_data(previousTotalCount):
        start_time = time.time()

        totalCasesToCheck = 0
        url="https://www.worldometers.info/coronavirus/"
        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text, "html5lib")
        liveCount = str(soup.select(".maincounter-number"))
        liveCount = liveCount.split('</div>')
        #print(liveCount[0].index('aaa'))
        totalCases = liveCount[0][59:liveCount[0].index('</span')]
        totalCases  = int(totalCases.replace(',',''))
        
        if(int(previousTotalCount) == totalCases):
            end_time1 = time.time()
            print(end_time1 -start_time)
            print("Notghingh")
            return None
        totalCasesToCheck =totalCases
        totalDeaths =str(liveCount[1].split('<span>')[1])[:liveCount[1].split('<span>')[1].index('</span>')]
        totalDeaths  = int(totalDeaths.replace(',',''))

        totalRecoveredCases = str(liveCount[2].split('<span>')[1])[:liveCount[1].split('<span>')[1].index('</span>')]
        totalRecoveredCases  = int(totalRecoveredCases.replace(',',''))


        activeCases = totalCases - totalRecoveredCases-totalDeaths
        mildCaseWeb  = str(soup.select(".number-table"))
        mildCaseWeb = mildCaseWeb.split('</span')
        mildCase =mildCaseWeb[0].split(">")
        mildCase = mildCase[1].replace(',','')
        mildCase = int(mildCase)
        seriousCase =mildCaseWeb[1].split(">")

        seriousCase = seriousCase[2]
        seriousCase = seriousCase.replace(',','')
        seriousCase = int(seriousCase)
        country  = str(soup.select("#main_table_countries_today"))
        country =country.split('</tr')
        dataList =[('countryName','totalCases','deaths','recoveredCases','seriousCases','totalTest','casespermillion','deathspermillion')]
        for i in range(9,len(country)):
            countryData  = country[i].split('td style="font-weight: bold; text-align:right">')
    
     #country name
            if(('</a></td>') in countryData[0]  in  countryData[0]):
                countryName = countryData[0].split('</a></td>')
                countryName1 = countryName[0].split('/">')
                actualName  = countryName[0].split('/">')[1]
        

            elif(('font-style:italic; "') in countryData[0]  in  countryData[0]):
            
                countryName = countryData[0].split('font-style:italic; "')
                countryName1 = countryName[1].split("', '>")        
                actualName =countryName1[0][1:countryName1[0].index('</span')]
            
    ####end of country name
  
    #total cases
            try:
                totalCases = countryData[1][:countryData[1].index('</td>')]
            except:
                totalCases = 'NA'
    # end of total cases
    #countryDeaths
    
        
            try:
                if('text-align:right;">' in  countryData[1]):
                    countryDeaths = countryData[1].split('text-align:right;">')
          
                else:
                    countryDeaths = countryData[1].split('text-align:right">')
        #print(countryDeaths)

        
    #print(countryDeaths)
                if(len(countryDeaths) ==  4):
                #print(len(countryDeaths))
                #print('4 ',countryDeaths[2].split('bold;')[0])
                    deaths =countryDeaths[2].split('bold;')[0]
                    deaths = deaths[:deaths.index('</td>')]
                elif(len(countryDeaths) ==  3):
            
                    deaths =countryDeaths[1].split('bold;')[0]
        
                    if(len(deaths) == 30 ):
            
            
                        deaths = countryDeaths[2][:countryDeaths[2].index('</td>')]
            
                #print(countryDeaths[1].split('bold;'))
                    else:  
                        deaths = deaths[:deaths.index('</td>')]
            #print(actualName,' ',deaths)

                else:
                    deaths =countryDeaths[1]
                    deaths = deaths[:deaths.index('</td>\n')]
    # end of total death
    
    
    ### recovered deaths
                recoveredCases  = countryData[2][:countryData[2].index('</td')]
                if('Uru' in actualName ):
                    print(recoveredCases)
    ##### active cases will be totalCase -recoveredCases-countryDeaths
    
    ####serious cases
                seriousCases  = countryData[3][:countryData[3].index('</td')]
    
    #####total test
                totalTest  = countryData[6][:countryData[6].index('</td')]
    #### cases per 1 million
    
                caseRate  = countryData[4][:countryData[4].index('</td')]
    ####deathRatePerPopulation
                deathRate  = countryData[5][:countryData[5].index('</td')]

                dataList.append((actualName,totalCases,deaths,recoveredCases,seriousCases,totalTest,caseRate,deathRate))
            except:
                dataList.append((actualName,totalCases,'NA','NA','NA','NA','NA','NA'))
              
    #print(len(dataList))
        countryName =[]
        totalCases=[]
        deaths=[]
        recoveredCases = []
        seriousCases = [] 
        totalTest = [] 
        casespermillion = []
        deathspermillion = []
        count = 0
        for data in dataList:
            if(count == 0):
                count = 1
                continue
            countryName.append(data[0].lower().replace(' ','_'))
            try:
                m = float(data[1].replace(',',''))
                totalCases.append(m)
            except:
                totalCases.append(0)
            try:
                m = float(data[2].replace(',',''))
                deaths.append(m)
            except:
                deaths.append(0)
    
            try:
                m = float(data[3].replace(',',''))
                recoveredCases.append(m)
            except:
                recoveredCases.append(0)
        
    
            try:
                m= float(data[4].replace(',',''))
                seriousCases.append(m)
            except:
                seriousCases.append(0)
            try:
                m= float(data[5].replace(',',''))
                totalTest.append(m)
            except:
                totalTest.append(0)
    
            try:
                m = float(data[6].replace(',',''))
                casespermillion.append(m)
            except:
                casespermillion.append(0)
            try:
                m= float(data[7].replace(',',''))
                deathspermillion.append(m)
            except:
                deathspermillion.append(0)
        
        covid19Data = pd.DataFrame(countryName,columns=['Country/Region'])
        covid19Data['Total_Cases']  = pd.Series(totalCases)
        covid19Data['Deaths']  = pd.Series(deaths)
        covid19Data['Recovered_Cases']  = pd.Series(recoveredCases)
        covid19Data['Active_Cases']  = covid19Data['Total_Cases'] -covid19Data['Deaths'] -covid19Data['Recovered_Cases'] 
        covid19Data['Serious_Cases']  = pd.Series(seriousCases)
        covid19Data['Total_Test']  = pd.Series(totalTest)
        covid19Data['Cases_per_million']  = pd.Series(casespermillion)
        covid19Data['Deaths_per_million']  = pd.Series(deathspermillion)   
    
        covid19Data.to_csv('data.csv')
        end_time = time.time()
        print(end_time -start_time)
        return totalCasesToCheck
    
totalCasesToCheck= 0 
class LoadCovidData():
    def load_refresh_data(previousTotalCount):
        start_time = time.time()

        totalCasesToCheck = 0
        url="https://www.worldometers.info/coronavirus/"
        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text, "html5lib")
        liveCount = str(soup.select(".maincounter-number"))
        liveCount = liveCount.split('</div>')
        #print(liveCount[0].index('aaa'))
        totalCases = liveCount[0][59:liveCount[0].index('</span')]
        totalCases  = int(totalCases.replace(',',''))
        
        if(int(previousTotalCount) == totalCases):
            end_time1 = time.time()
            print(end_time1 -start_time)
            print("Notghingh")
            return None
        totalCasesToCheck =totalCases
        totalDeaths =str(liveCount[1].split('<span>')[1])[:liveCount[1].split('<span>')[1].index('</span>')]
        totalDeaths  = int(totalDeaths.replace(',',''))

        totalRecoveredCases = str(liveCount[2].split('<span>')[1])[:liveCount[1].split('<span>')[1].index('</span>')]
        totalRecoveredCases  = int(totalRecoveredCases.replace(',',''))


        activeCases = totalCases - totalRecoveredCases-totalDeaths
        mildCaseWeb  = str(soup.select(".number-table"))
        mildCaseWeb = mildCaseWeb.split('</span')
        mildCase =mildCaseWeb[0].split(">")
        mildCase = mildCase[1].replace(',','')
        mildCase = int(mildCase)
        seriousCase =mildCaseWeb[1].split(">")

        seriousCase = seriousCase[2]
        seriousCase = seriousCase.replace(',','')
        seriousCase = int(seriousCase)
        country  = str(soup.select("#main_table_countries_today"))
        country =country.split('</tr')

        
        
        
        dataList =[('countryName','totalCases','deaths','recoveredCases','seriousCases','totalTest','casespermillion','deathspermillion')]
        for i in range(9,len(country)):
            countryData  = country[i].split('td style="font-weight: bold; text-align:right">')
    
     #country name
            if(('</a></td>') in countryData[0]  in  countryData[0]):
                countryName = countryData[0].split('</a></td>')
                countryName1 = countryName[0].split('/">')
                actualName  = countryName[0].split('/">')[1]
        

            elif(('font-style:italic; "') in countryData[0]  in  countryData[0]):
            
                countryName = countryData[0].split('font-style:italic; "')
                countryName1 = countryName[1].split("', '>")        
                actualName =countryName1[0][1:countryName1[0].index('</span')]
            
    ####end of country name
  
    #total cases
            try:
                totalCases = countryData[1][:countryData[1].index('</td>')]
            except:
                totalCases = 'NA'
    # end of total cases
    #countryDeaths
    
        
            try:
                if('text-align:right;">' in  countryData[1]):
                    countryDeaths = countryData[1].split('text-align:right;">')
          
                else:
                    countryDeaths = countryData[1].split('text-align:right">')
        #print(countryDeaths)

        
    #print(countryDeaths)
                if(len(countryDeaths) ==  4):
                #print(len(countryDeaths))
                #print('4 ',countryDeaths[2].split('bold;')[0])
                    deaths =countryDeaths[2].split('bold;')[0]
                    deaths = deaths[:deaths.index('</td>')]
                elif(len(countryDeaths) ==  3):
            
                    deaths =countryDeaths[1].split('bold;')[0]
        
                    if(len(deaths) == 30 ):
            
            
                        deaths = countryDeaths[2][:countryDeaths[2].index('</td>')]
            
                #print(countryDeaths[1].split('bold;'))
                    else:  
                        deaths = deaths[:deaths.index('</td>')]
            #print(actualName,' ',deaths)

                else:
                    deaths =countryDeaths[1]
                    deaths = deaths[:deaths.index('</td>\n')]
    # end of total death
    
    
    ### recovered deaths
                recoveredCases  = countryData[2][:countryData[2].index('</td')]
                if('Uru' in actualName ):
                    print(recoveredCases)
    ##### active cases will be totalCase -recoveredCases-countryDeaths
    
    ####serious cases
                seriousCases  = countryData[3][:countryData[3].index('</td')]
    
    #####total test
                totalTest  = countryData[6][:countryData[6].index('</td')]
    #### cases per 1 million
    
                caseRate  = countryData[4][:countryData[4].index('</td')]
    ####deathRatePerPopulation
                deathRate  = countryData[5][:countryData[5].index('</td')]

                dataList.append((actualName,totalCases,deaths,recoveredCases,seriousCases,totalTest,caseRate,deathRate))
            except:
                dataList.append((actualName,totalCases,'NA','NA','NA','NA','NA','NA'))
    #print(len(dataList))
                end_time = time.time()
        print(end_time -start_time)
        return totalCasesToCheck
    






