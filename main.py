


# Imports
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup
import sqlite3
from unidecode import unidecode
from datetime import datetime


def inicio_geracao():
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Início da geração: ", dt_string)

def fim_geracao():
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Fim da geração: ", dt_string)


def zerar_banco():
    try:
        con = sqlite3.connect('neoway.db')
        cur = con.cursor()
        cur.execute(
            'DELETE FROM candidatos')
        print(f'Total de candidatos apagados: {cur.rowcount}')
        con.commit()
        cur.close()
        con.close()
    except sqlite3.Error as erro:
        print('Erro ao apagar candidatos do banco.',erro)

def inserir_banco(candidato):
    #print(candidato)
    try:
        con = sqlite3.connect('neoway.db')
        cur = con.cursor()
        cur.execute('INSERT INTO candidatos (Nome, Score, CPF, Status) VALUES (?,?,?,?)',candidato,)
        con.commit()
        #print(f'Candidato {candidato[0]} incluso com sucesso.')
        cur.close()
        con.close()
    except sqlite3.Error as erro:
        print(f'Erro na inclusão {candidato[0]}.',erro)
    
def dados_candidato(cpf):
    candidato=[]
    url2 = 'https://sample-university-site.herokuapp.com/candidate/' + str(cpf)
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, "html.parser")
    for dados in soup.findAll('div'):
        d = str(dados).split('</b> ')
        d = d[1].split('<')
        ret = valida_nome(d[0])
        candidato.append(ret)
    candidato.append(cpf)
    #print(candidato)
    return candidato
    
def dados_pagina(pagina):
    # Set the URL you want to webscrape from
    url = 'https://sample-university-site.herokuapp.com/approvals/' + str(pagina)

    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    return soup.findAll('a')


def valida_nome(nome):
    nome = nome.title() #Primeira letra maiuscusla de cada palavra
    return unidecode(nome) #remove os acentos

def valida_cpf(cpf: str) -> bool:

    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validate('529.982.247-25')
    True
    >>> validate('52998224725')
    False
    >>> validate('111.111.111-11')
    False
    """

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True



if __name__ == '__main__':
    inicio_geracao()
    zerar_banco()
    print('Por favor, aguarde...')
    pagina = 1
    while True:
        # Set the URL you want to webscrape from
        url = 'https://sample-university-site.herokuapp.com/approvals/' + str(pagina)

        # Connect to the URL
        response = requests.get(url)

        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")

        
        arquivo = []
        qtd_pagina = 0
        #if pagina < 4672: #total de paginas da base de dados
        if pagina < 10: #simulei com 10 paginas
            for x in soup.findAll('a'):
                    link = x['href']
                    cpf = link.split('/')
                    cpf = cpf[2]
                    if qtd_pagina <10:
                        #arquivo.append(cpf)
                        d = dados_candidato(cpf)
                        if valida_cpf(cpf):
                            d.append('cpf valido')
                        else:
                            d.append('ERRO cpf invalido')
                        arquivo.append(d)
                        inserir_banco(arquivo[0])
                        qtd_pagina +=1
                        arquivo = []
                    else:
                        pagina +=1
                        #print(f'Por favor aguarde {pagina}')
                        qtd_pagina = 0
                        arquivo = []
        else:
            break
        #inserir_banco(arquivo)
        #print(arquivo)
    fim_geracao()
