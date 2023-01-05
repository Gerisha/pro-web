
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'




headers=['name','distance','mass','radius']
star_data=[]
r=requests.get(START_URL)
    #htmlcontent=r.content
        
soup=BeautifulSoup(r.text,'html.parser')
star_table=soup.find('table')
temp_list=[]
table_row=star_table.find_all("tr")
for tr_tag in table_row:
    td=tr_tag.find_all("td")
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)
    star_names=[]
    mass=[]
    distance=[]
    radius=[]
    luminous=[]
    for i in range(1,len(temp_list)):
        star_names.append(temp_list[i][1])
        mass.append(temp_list[i][5])
        distance.append(temp_list[1][3])
        radius.append(temp_list[i][6])
        luminous.append(temp_list[i][7])
    df=pd.DataFrame(list(zip(star_names,mass,distance,radius,luminous)),columns=['star_names','mass','distance','radius','luminous'])
    df.to_csv("scape.csv")





