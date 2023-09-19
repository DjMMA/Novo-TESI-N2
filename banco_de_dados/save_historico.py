from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = 'banco.db'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'SAVES'

def cria_conexao_banco():
    conexao = sqlite3.Connection(DB_FILE)
    cursor = conexao.cursor()
    sql = (
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            ' id_partida INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' status_vitoria INTEGER NOT NULL,'
            ' vida_jogador INTEGER NOT NULL,'
            ' vida_monstro INTEGER NOT NULL,'
            ' id_jogador INTEGER NOT NULL,'
            ' FOREIGN KEY (id_jogador) REFERENCES "USERS"("id_usuario")'
        ')'
    )
    cursor.execute(sql)
    return conexao, cursor

def insere_valores(*args):
    conexao, cursor = cria_conexao_banco()
    sql = (
        f'INSERT INTO {TABLE_NAME} ( '
            ' status_vitoria, vida_jogador, vida_monstro, id_jogador'
        ')'
        ' VALUES (?, ?, ?, ?)'
    )
    try:
        cursor.execute(sql, (args))
        conexao.commit()
        cursor.close()
        conexao.close()
    except Exception as e:
        print("Classe já existente na tabela, por favor insira outra. -> ", e, "-> ", args[0])
        cursor.close()
        conexao.close()
        
def mostra_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'SELECT * FROM {TABLE_NAME}'
    cursor.execute(sql)
    print(cursor.fetchall())
    cursor.close()
    conexao.close()
    
