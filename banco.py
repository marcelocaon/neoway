
# Imports
import sqlite3

def zerar_banco():
    """ Apaga todos os registros do banco de dados."""
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
    """ Insere os dados do candidato no banco de dados.
        - Nome
        - Score
        - CPF
        - Status, se o CPF esta inválido, insere a informação de cpf inválido no banco
    """
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
