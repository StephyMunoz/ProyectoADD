import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient
import json

db = MongoClient('mongodb://localhost:27017').noticiasbbcinternacional

Noticia=[]
Fecha=[]
Fuente=[]
Escritor=[]

def find_2nd(string, substring):
    return string.find(substring, substring.find(substring)+1)

def find_1st(string, substring):
    return string.find(substring, substring.find(substring))

#response = requests.get('https://www.bbc.com/mundo/topics/c7zp57yyz25t#main-content')
#response = requests.get('https://www.bbc.com/mundo/topics/c7zp57yyz25t/page/10')america
response = requests.get('https://www.bbc.com/mundo/topics/c2lej05epw5t/page/9')
soup = BeautifulSoup(response.content,"lxml")

post_noticia=soup.find_all("span", class_="lx-stream-post__header-text gs-u-align-middle")
for element in post_noticia:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Noticia.append(limpio.strip())
    #print(limpio.strip())
Noticia

post_fecha=soup.find_all("span", class_="qa-post-auto-meta")
for element in post_fecha:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Fecha.append(str(limpio.strip()))
Fecha

post_fuente=soup.find_all("p", class_="qa-contributor-role lx-stream-post__contributor-description gel-brevier gs-u-m0")
for element in post_fuente:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Fuente.append(str(limpio.strip()))
Fuente
post_escritor=soup.find_all("p", class_="qa-contributor-name lx-stream-post__contributor-name gel-long-primer gs-u-m0")
for element in post_escritor:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Escritor.append(str(limpio.strip()))
Escritor

#dfDS=[]
#dfDS=pd.DataFrame({'Noticia':Noticia, 'Fecha':Fecha,'Fuente':Fuente,'escritor':Escritor})
#print(dfDS)

i=0
for j in post_noticia:
    doc={}
    id=i
    i=i+1
    try:
        doc = {'Noticia':Noticia[i],'Fecha': Fecha[i],'Fuente': Fuente[i],'Escritor':Escritor[i]}
        db.Internacional9.insert_one(doc)
        print("guardado exitosamente")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))