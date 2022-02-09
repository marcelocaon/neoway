
# Imports
import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

import banco as banco
import validador as validador


def inicio_geracao():
    # data atual do sistema
    now = datetime.now()

    # converte para o padrao dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Início da geração: ", dt_string)

def fim_geracao():
    # data atual do sistema
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Fim da geração: ", dt_string)

    
def dados_candidato(cpf):
    """ Captura nas subpaginas o nome e o score do candidado usando o cpf dele.
    """
    candidato=[]
    url2 = 'https://sample-university-site.herokuapp.com/candidate/' + str(cpf)
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, "html.parser")
    #procura pelas tag 'div' onde consta as informacoes de nome e score
    #tem que ser feito um for pq sao duas informacoes, nome e score
    for dados in soup.findAll('div'):
        d = str(dados).split('</b> ')
        d = d[1].split('<')
        #chama a funcao valida nome
        ret = validador.valida_nome(d[0])
        candidato.append(ret)
    candidato.append(cpf)
    #print(candidato)
    return candidato




if __name__ == '__main__':
    """ Execução do programa
        - usuário informa o numero da pagina que deseja comecar a captura ou digita 1 para comecar do inicio
        - programa captura os dados html do site informado, procura pela tag "a" e do tipo candidate, pega o cpf e vai no endereco
        do usando o cpf para pegar o nome e score
        - apos isso valida o nome, removendo acentos e colocando maiusculas nas iniciais
        - apos valida cpf se correto, caso seja invalido preenche na coluna status do banco que o cpf esta invalido

        *Existe a possibilidade de ter feito um arquivo/classe para ler os dados, outro para validar e outro para inserir no banco mas pelo que
        observei o desenpenho não mudou
    """
    
    print('**Programa para captura de dados e armazenamento em banco de dados SQLite**\n')
    resposta = input(('Deseja iniciar a captura de qual página? (Por favor, digite de 1 a 4671, sendo 1 = a primeira)'))
    while resposta.isdigit() == False:
        resposta = input(('Voce digitou uma letra, por favor, digite de 1 a 4671, sendo 1 = a primeira: '))
    while int(resposta) not in range(1,4671):
        resposta = input(('Voce digitou uma página errada, por favor, digite de 1 a 4671, sendo 1 = a primeira: '))
    if int(resposta) == 1:        
        pagina = 1
        zerar_banco()
    else:
        pagina = int(resposta)

    #imprimi horario inicio captura    
    inicio_geracao()
    print('Por favor, aguarde...')
    while pagina < 4672: #total de paginas da base de dados +1
        # Informa a pagina que queremos capturar os dados
        url = 'https://sample-university-site.herokuapp.com/approvals/' + str(pagina)

        # conecta a pagina
        response = requests.get(url)

        # captura os dados HTML e salva no objeto
        soup = BeautifulSoup(response.text, "html.parser")

        arquivo = []
        for x in soup.findAll('a'):
                link = x['href']
                cpf = link.split('/')
                if cpf[1] == 'candidate':
                    cpf = cpf[2]
                    #arquivo.append(cpf)
                    d = dados_candidato(cpf)
                    if not validador.valida_cpf(cpf):
                        d.append('cpf invalido')
                    else:
                        d.append(None)
                    arquivo.append(d)
                    print(d)
                    banco.inserir_banco(arquivo[0])
                    arquivo = []
                else:
                    print(f'Página capturada: {pagina}')
                    pagina +=1                            
                    arquivo = []

        #inserir_banco(arquivo)
        #print(arquivo)

    #imprimi horario fim captura
    fim_geracao()
