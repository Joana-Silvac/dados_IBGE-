import pandas as pd
import requests
from bs4 import BeautifulSoup
import time 
import platform
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

            texto=i.find('div', class_="legenda")
            if texto:
               texto= texto.text.strip()
               idades.append(texto)


            valor_mulher = i.find('div', class_="valor-2 legenda-2")
            if valor_mulher:
                 mulheres.append(valor_mulher.text.strip())
            else:
                  mulheres.append('')

            valor_homem = i.find('div', class_="valor-1 legenda-1")
            if valor_homem:
                 homens.append(valor_homem.text.strip())
            else:
                  homens.append('')


min_len = min(len(idades),
              len(mulheres), len(homens))
idades = idades[:min_len]
mulheres = mulheres[:min_len]
homens = homens[:min_len]

dic={"Idade": idades, "Mulheres": mulheres,"Homens": homens}



df = pd.DataFrame(dic)
sistema=platform.system()

if sistema=="Windows":
     df.to_csv('piramide_etaria.csv', index=False, encoding= 'utf-8-sig')
elif sistema == "Linux":
          df.to_csv('piramide_etaria.csv', index=False, encoding= 'utf-8')

pesquisador.quit()