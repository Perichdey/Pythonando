import pandas as pd
import os
from urllib.request import urlopen
import json


with open('E:\\Projetos\\GitHub\\Pythonando\\Back\\Codes\\arquivo2.txt','r',encoding='utf-8') as conteudo:
    print(conteudo.read())

resposta = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf-8')
dados = json.loads(resposta)[0]
dados
print('Título: ', dados['title'])
print('URL:  ', dados['url'])
print('Duração:  ', dados['duration'])
print('Número de visualizaçãoes:  ', dados['stats_number_of_plays'])
