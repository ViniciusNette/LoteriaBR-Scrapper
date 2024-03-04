from requests import get, exceptions
from bs4 import BeautifulSoup as sp
from operator import itemgetter

url = 'https://asloterias.com.br/lista-de-resultados-da-dia-de-sorte'

diadesorte_dezenas = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0,
                '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0,
                '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0,
                '30': 0, '31': 0}

meses_sorteados = {'Janeiro': 0, 'Fevereiro': 0, 'Março': 0, 'Abril': 0, 'Maio': 0, 'Junho': 0, 'Julho': 0, 'Agosto': 0,
                'Setembro': 0, 'Outubro': 0, 'Novembro': 0, 'Dezembro': 0}

try:
    print('Conectando e Extraindo Resultados do Site ...')
    with get(url, stream=True) as carregaurl:
        print('Conexão feita com sucesso!\n\n')
        saida_colunas = []
        for linhas_tr in sp(carregaurl.content, "lxml")\
                .findAll("div", class_="limpar_flutuacao"):
            saida_colunas.append(linhas_tr.previous_sibling)

except exceptions.HTTPError as erro:
    exit(f'--- Erro {erro} na conexao HTTP com o site ---')

with open('todos_os_resultados_diadesorte.csv', 'w', encoding='utf-8') as arquivo_com_resultados:
    arquivo_com_resultados.truncate(0)
    for resultado in list(saida_colunas):
        dez1 = int(resultado[17:19])
        dez2 = int(resultado[20:22])
        dez3 = int(resultado[23:25])
        dez4 = int(resultado[26:28])
        dez5 = int(resultado[29:31])
        dez6 = int(resultado[32:34])
        dez7 = int(resultado[35:37])
        mes = resultado[39:].strip()  # Extraindo o mês
        dezenas = f'{dez1},{dez2},{dez3},{dez4},{dez5},{dez6},{dez7},{mes}'
        print(dezenas, file=arquivo_com_resultados)
        for dezena in dezenas.split(','):
            if dezena in diadesorte_dezenas:
                diadesorte_dezenas[dezena] += 1
        if mes in meses_sorteados:
            meses_sorteados[mes] += 1

print('--- As 7 dezenas mais (+) sorteadas na Dia-de-Sorte até hoje ---')
for dezena, vezes in sorted(diadesorte_dezenas.items(), key=itemgetter(1), reverse=True)[:7]:
    print(f'{vezes:0} vezes > dezena: {dezena:0}')
print('\n--- As 7 dezenas menos (-) sorteadas na Dia-de-Sorte até hoje ---')
for dezena, vezes in sorted(diadesorte_dezenas.items(), key=itemgetter(1), reverse=False)[:7]:
    print(f'{vezes:0} vezes > dezena: {dezena:0}')

print('\n--- Os meses mais (+) sorteados na Dia-de-Sorte até hoje ---')
for mes, quantidade in sorted(meses_sorteados.items(), key=itemgetter(1), reverse=True)[:12]:
    print(f'{quantidade:0} vezes > Mês: {mes:0}')

print('\n--- As 31 dezenas mais (+) sorteadas na Dia-de-Sorte até hoje ---')
for dezena, vezes in sorted(diadesorte_dezenas.items(), key=itemgetter(1), reverse=True)[:31]:
    print(f'{vezes:0} vezes > dezena: {dezena:0}')
