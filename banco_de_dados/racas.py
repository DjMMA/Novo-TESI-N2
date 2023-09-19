from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = 'banco.db'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'RACAS'

def cria_conexao_banco():
    conexao = sqlite3.Connection(DB_FILE)
    cursor = conexao.cursor()
    sql = (
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            ' id_raca INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' nome_raca TEXT UNIQUE NOT NULL,'
            ' vida_raca INTEGER DEFAULT 0,'
            ' ataque_raca INTEGER DEFAULT 0,'
            ' defesa_raca INTEGER DEFAULT 0'
        ')'
    )
    cursor.execute(sql)
    return conexao, cursor

def insere_valores(*args):
    conexao, cursor = cria_conexao_banco()
    sql = (
        f'INSERT INTO {TABLE_NAME} ( '
            ' nome_raca, vida_raca, ataque_raca, defesa_raca'
        ')'
        ' VALUES (?, ?, ?, ?)'
    )
    cursor.execute(sql, (args))
    conexao.commit()
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
    sql = f'SELECT * FROM {TABLE_NAME} WHERE nome_raca = ?'
    cursor.execute(sql, [nome])
    print(cursor.fetchall())
    conexao.commit()
    cursor.close()
    conexao.close()

def seleciona_por_id(id):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT * FROM {TABLE_NAME} WHERE id_raca = ?'
    cursor.execute(sql, [id])
    print(cursor.fetchall())
    conexao.commit()
    cursor.close()
    conexao.close()
    
def limpa_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'DELETE FROM {TABLE_NAME}'
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

def retorna_nome():
    conexao, cursor = cria_conexao_banco()
    cursor.execute("SELECT nome_raca FROM RACAS")
    valores = cursor.fetchone()[0]
    conexao.close()
    print(valores)
    return valores


# limpa_todos()
# insere_valores('Humano', 0, 0, 0)
mostra_todos()
print()
retorna_nome()
    
    
