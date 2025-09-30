import pandas as pd
from bs4 import BeautifulSoup
import time 
import platform
from selenium import webdriver
  

pesquisador=webdriver.Chrome()
pesquisador.get("https://censo2022.ibge.gov.br/panorama/")
time.sleep(4)
soup=BeautifulSoup(pesquisador.page_source,"html.parser")

#Pirâmide etária

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


dic={"Idade": idades, "Mulheres": mulheres,"Homens": homens}


df = pd.DataFrame(dic)
sistema=platform.system()

if sistema=="Windows":
     df.to_csv('piramide_etaria.csv', index=False, encoding= 'utf-8-sig')
elif sistema == "Linux":
          df.to_csv('piramide_etaria.csv', index=False, encoding= 'utf-8')

#Cor-raça

cor_raca_categorias = []
cor_raca_populacao = []

cor_raca_card = soup.find('div', id='corOuRacaCard')
if cor_raca_card:
    legenda = cor_raca_card.find('div', class_='legenda')
    if legenda:
        itens_legenda = legenda.find_all('li')
        for item in itens_legenda:
            texto_completo = item.text.strip()
            if ':' in texto_completo:
                categoria = texto_completo.split(':')[0].strip()
                populacao = texto_completo.split(':')[1].strip()
                cor_raca_categorias.append(categoria)
                cor_raca_populacao.append(populacao)

dic_cor_raca = {"Cor-Raça": cor_raca_categorias, "População": cor_raca_populacao}

df_cor_raca = pd.DataFrame(dic_cor_raca)
sistema=platform.system()

if sistema=="Windows":
     df_cor_raca.to_csv('cor_raca.csv', index=False, encoding= 'utf-8-sig')
elif sistema == "Linux":
          df_cor_raca.to_csv('cor_raca.csv', index=False, encoding= 'utf-8')

pesquisador.quit()