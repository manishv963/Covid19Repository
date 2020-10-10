# Covid19Repository Chatbot



Chatbot provide real time data of country. The number of active cases, serious cases, deaths and total test conducted by country.
The data is extracted from the link https://www.worldometers.info/coronavirus/#countries using WebScrapping. LoadCovidData file downloads the data from web and store it in data.csv

The Spell corrector is implemented in case th there is spelling error of country name.

The file system databse  is maintained which is used to store the real time data. We store the last time data was updated. If the difference between current time and last update time from database is greater than 15 minutes than only data is loaded again from internet.
