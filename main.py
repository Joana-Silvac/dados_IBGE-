import pandas as pd
import requests
from bs4 import BeautifulSoup


url="https://censo2022.ibge.gov.br/panorama/"
resposta= requests.get(url)
soup=BeautifulSoup(resposta.text, 'lxml')
