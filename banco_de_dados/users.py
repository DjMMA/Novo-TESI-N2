from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = 'banco.db'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'USERS'

def cria_conexao_banco():
    conexao = sqlite3.Connection(DB_FILE)
    conexao = sqlite3.connect(DB_FILE)
    cursor = conexao.cursor()
    sql = (
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            ' id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' nome_usuario TEXT UNIQUE NOT NULL,'
            ' senha_usuario TEXT NOT NULL'
        ')'
    )
    cursor.execute(sql)
    return conexao, cursor

def mostra_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'SELECT * FROM {TABLE_NAME}'
    cursor.execute(sql)
    print(cursor.fetchall())
    cursor.close()
    conexao.close()

def insere_valores(*args):
    conexao, cursor = cria_conexao_banco()
    sql = (
        f'INSERT INTO {TABLE_NAME} ( '
            ' nome_usuario, senha_usuario'
        ')'
        ' VALUES (?, ?)'
    )
    try:
        cursor.execute(sql, (args))
        conexao.commit()
        mostra_todos()
        cursor.close()
        conexao.close()
    except Exception as e:
        print("Este usuário já existe  -> ", e, "-> ", args[0])
        cursor.close()
        conexao.close()
        

    
def seleciona_por_nome(nome):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT senha_usuario FROM {TABLE_NAME} WHERE nome_usuario = ?'
    cursor.execute(sql, [nome])
    conexao.commit()
    senha = (cursor.fetchone()[0])
    cursor.close()
    conexao.close()
    return senha 

def seleciona_por_id(id):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT * FROM {TABLE_NAME} WHERE id_usuario = ?'
    cursor.execute(sql, [id])
    classe = cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()
    return classe
    
def limpa_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'DELETE FROM {TABLE_NAME}'
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

limpa_todos()
insere_valores('Julio', '1608jc')
mostra_todos()
print('\nseparação aqui\n')
print(seleciona_por_nome('Julio'))
seleciona_por_id('1')

con, cur = cria_conexao_banco()
cur.execute('SELECT * FROM USERS')
print(cur.fetchall())
    
    
