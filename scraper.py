import bs4 as bs
import csv
import urllib.request
import lxml

url_main='https://karki23.github.io/Weather-Data/assignment.html'
sauce_main=urllib.request.urlopen(url_main).read()
srccode_main=bs.BeautifulSoup(sauce_main,'lxml')
print(srccode_main.title)


for i in srccode_main.find_all('a'):
 url=i.get('href')
 url_link='https://karki23.github.io/Weather-Data/'+url
 print(url_link)
 sauce=urllib.request.urlopen(url_link).read()
 srccode=bs.BeautifulSoup(sauce,'lxml')
 print(srccode.title)
 print('\n')
 table=srccode.find('table')
 results=table.find_all('tr')
 print('Number of results:',len(results))
  """creating columns and setting names of the columns"""
 rows=[]
 rows.append(['Date','Location','MinTemp','Maxtemp',
 'Rainfall','Evaporation','Sunshine','WindGustDir',
 'WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am'
 ,'WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am',
 'Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm',
 'RainToday','RISK_MM','RainTomorrow'])
 for result in results:
  data=result.find_all('td')
  if len(data)==0:
   continue
  #extracting data from each column for each row
  Date=data[0].getText()
  Location=data[1].getText()
  MinTemp=data[2].getText()
  MaxTemp=data[3].getText()
  Rainfall=data[4].getText()
  Evaporation=data[5].getText()
  Sunshine=data[6].getText()
  WindGustDir=data[7].getText()
  WindGustSpeed=data[8].getText()
  WindDir9am=data[9].getText()
  WindDir3pm=data[10].getText()
  WindSpeed9am=data[11].getText()
  WindSpeed3pm=data[12].getText()
  Humidity9am=data[13].getText()
  Humidity3pm=data[14].getText()
  Pressure9am=data[15].getText()
  Pressure3pm=data[16].getText()
  Cloud9am=data[17].getText()
  Cloud3pm=data[18].getText()
  Temp9am=data[19].getText()
  Temp3pm=data[20].getText()
  RainToday=data[21].getText()
  RISK_MM=data[22].getText()
  RainTomorrow=data[23].getText()
  #appending values from table in link to csv file
  rows.append([Date,Location,MinTemp,MaxTemp,Rainfall,Evaporation,Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,RainToday,RISK_MM,RainTomorrow])
 #printing rows to check how the output will be
 print(rows)
#writing it to csv file(appending values to already existing csv file)
 with open('io_progm.csv','a',newline='') as f_output:
  csv_output=csv.writer(f_output)
  csv_output.writerows(rows)