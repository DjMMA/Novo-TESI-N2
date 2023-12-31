from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = 'banco.db'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'PERSONAS'

def cria_conexao_banco():
    conexao = sqlite3.Connection(DB_FILE)
    cursor = conexao.cursor()
    sql = (
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            ' id_PERSONA INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' nome_persona TEXT UNIQUE NOT NULL,'
            ' vida_persona INTEGER,'
            ' ataque_persona INTEGER,'
            ' defesa_persona INTEGER'
        ')'
    )
    cursor.execute(sql)
    return conexao, cursor

def insere_valores(*args):
    conexao, cursor = cria_conexao_banco()
    sql = (
        f'INSERT INTO {TABLE_NAME} ( '
            ' id_persona INTEGER PRIMARY KEY AUTOINCREMENT, '
            ' nome_persona TEXT NOT NULL,'
            ' vida_persona INTEGER,'
            ' ataque_persona INTEGER,'
            ' defesa_persona INTEGER'
        ')'
        ' VALUES (?, ?, ?, ?)'
    )
    try:
        cursor.execute(sql, (args))
        conexao.commit()
        cursor.close()
        conexao.close()
    except Exception as e:
        # print("Este usuário já existe  -> ", e, "-> ", args[0])
        cursor.close()
        conexao.close()
        
def mostra_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'SELECT * FROM {TABLE_NAME}'
    cursor.execute(sql)
    print(cursor.fetchall())
    cursor.close()
    conexao.close()
    
def seleciona_por_nome(nome):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT * FROM {TABLE_NAME} WHERE nome_persona = ?'
    cursor.execute(sql, [nome])
    senha = cursor.fetchall()
    print(senha, ' <- senha')
    conexao.commit()
    cursor.close()
    conexao.close()
    return senha

def seleciona_por_id(id):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT * FROM {TABLE_NAME} WHERE id_PERSONA = ?'
    cursor.execute(sql, [id])
    persona = cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()
    return persona
    
def limpa_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'DELETE FROM {TABLE_NAME}'
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()


    
