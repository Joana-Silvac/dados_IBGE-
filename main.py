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
mulheres=[]
homens=[]

if tudo:
        parte_dos_itens=tudo.find_all('div',class_="item item-v1")
        for i in parte_dos_itens:
            #nessa parte mandei o código ir atras dos anos q correspondem a porcentagem 
            texto=i.find('div', class_="legenda")
            if texto:
               texto= texto.text.strip()
               idades.append(texto)
            #nessa parte o codigo deve corresponder a porcentagem das mulheres e então caso encontre adicionar na lista mulheres[]

            #E nessa parte o codigo tem q ir atrás da porcentagem masculina e adicionar na lista homens[]



dic={"Idade": idades, "Mulheres": mulheres,"Homens": homens}

print(dic) 

#criar o dataframe com o dic


#fazer o codigo identificar se a maquina é windows ou linux e fazer ser criado um arquivo csv com o data frame dentro

#windows


#Linux