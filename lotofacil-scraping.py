#!/usr/bin/env python3
import os
os.system("pip3 install --user beautifulsoup4")
from requests import get, exceptions
from bs4 import BeautifulSoup as sp
from operator import itemgetter

""" URL com todos os resultados da lotofacil   """

url = 'https://asloterias.com.br/lista-de-resultados-da-lotofacil'

loto_dezenas = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0,
                '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0,
                '23': 0, '24': 0, '25': 0}

try:

    print('Conectando-se ao site "asloterias.com.br" ...')

    with get(url, stream=True) as carregaurl:
        print('Conexão feita com sucesso!\n\n')
        saida_colunas = []
        for linhas_tr in sp(carregaurl.content, "lxml")\
                .findAll("div", class_="limpar_flutuacao"):
            saida_colunas.append(linhas_tr.previous_sibling)

except exceptions.HTTPError as erro:
    exit(f'--- Erro {erro} na conexao HTTP com o site ---')

with open('todos_os_resultados_lotofacil.csv', 'w') as arquivo_com_resultados:

    arquivo_com_resultados.truncate(0)
    for resultado in list(saida_colunas):
        dez1 = int(resultado[17:19])
        dez2 = int(resultado[20:22])
        dez3 = int(resultado[23:25])
        dez4 = int(resultado[26:28])
        dez5 = int(resultado[29:31])
        dez6 = int(resultado[32:34])
        dez7 = int(resultado[35:37])
        dez8 = int(resultado[38:40])
        dez9 = int(resultado[41:43])
        dez10 = int(resultado[44:46])
        dez11 = int(resultado[47:49])
        dez12 = int(resultado[50:52])
        dez13 = int(resultado[53:55])
        dez14 = int(resultado[56:58])
        dez15 = int(resultado[59:61])
        dezenas = f'{dez1},{dez2},{dez3},{dez4},{dez5},{dez6},{dez7},{dez8},{dez9},{dez10},{dez11},{dez12},{dez13},{dez14},{dez15}'
        print(dezenas, file=arquivo_com_resultados)
        for dezena in dezenas.split(','):
            if dezena in loto_dezenas:
                loto_dezenas[dezena] += 1

print('\nORDEM DECRESCENTE')
print('--- As 15 dezenas mais (+) sorteadas na LotoFácil até hoje ---')
for dezena, vezes in sorted(loto_dezenas.items(), key=itemgetter(1),\
    reverse=True)[:15]:
    print(f'{vezes:0} vezes > dezena: {dezena:0}'
          f'\r')
print('\n')
print('\nORDEM CRESCENTE')
print('--- As 10 dezenas menos (-) sorteadas na LotoFácil até hoje ---')
for dezena, vezes in sorted(loto_dezenas.items(), key=itemgetter(1),\
    reverse=False)[:10]:
    print(f'{vezes:0} vezes > dezena: {dezena:0}'
          f'\r')
print('\n')
print('\nTOTAL')
print('--- TODAS dezenas mais (+) sorteadas na LotoFácil até hoje ---')
for dezena, vezes in sorted(loto_dezenas.items(), key=itemgetter(1),\
    reverse=True)[:25]:
    print(f'{vezes:0} vezes > dezena: {dezena:0}'
          f'\r')
print('--- TODAS dezenas menos (-) sorteadas na LotoFácil até hoje ---\r')
