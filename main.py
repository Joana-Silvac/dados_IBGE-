import pandas as pd
import requests
from bs4 import BeautifulSoup
import time 
from selenium import webdriver


pesquisador=webdriver.Chrome()
pesquisador.get("https://censo2022.ibge.gov.br/panorama/")
time.sleep(3)
soup=BeautifulSoup(pesquisador.page_source,"html.parser")

tudo = soup.find('div', id="piramide-etaria", class_="grafico-piramideEtaria piramideV2")
idades=[]

if tudo:
        parte_dos_itens=tudo.find_all('div',class_="item item-v1")
        for i in parte_dos_itens:
            texto=i.find('div', class_="legenda")
            if texto:
               texto= texto.text.strip()
               idades.append(texto)



dic={"Idade": idades}

print(dic)
