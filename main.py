import pandas as pd
import requests
from bs4 import BeautifulSoup


url="https://censo2022.ibge.gov.br/panorama/"
resposta= requests.get(url)
soup=BeautifulSoup(resposta.text, 'lxml')

df = pd.read_csv('dados.csv', delimiter=';')
total = df['População (pessoas)'].sum()
df['Percentual'] = (df['População (pessoas)'] / total * 100).round(2)
df.to_csv('analise_cor_raca.csv', index=False)
