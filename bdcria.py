import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "criando.bd"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_RACA = "RACAS"
TABLE_CLASSE = "CLASSES"

CRIAR_RACA = (
    f'CREATE TABLE IF NOT EXISTS {TABLE_RACA}('
        'RA_ID INTEGER NOT NULL PRIMARY KEY autoincrement,'
        'RA_NOME varchar(40) NOT NULL,'
        'RA_COSTITUICAO INT(50)   NOT NULL,'
        'RA_FORCA INT(50)   NOT NULL,'
        'RA_INTELIGENCIA INT(50) NOT NULL,'
        'RA_CARISMA INT(50) NOT NULL,'
        'RA_AGILIDADE INT(50)   NOT NULL,'
        'RA_DEFESA INT(50) NOT NULL'
    ')'
)

CRIAR_CLASSE = (
    f'CREATE TABLE IF NOT EXISTS {TABLE_CLASSE}('
        'CLAS_ID INTEGER NOT NULL primary key autoincrement,'
        'CLAS_NOME varchar(0) NOT NULL,'
        'CLAS_CONSTITUICAO INT(0) NULL,'
        'CLAS_FORCA INT(50) NOT NULL,'
        'CLAS_INTELIGENCIA INT(50) NOT NULL,'
        'CLAS_CARISMA INT(50) NOT NULL,'
        'CLAS_AGILIDADE      INT(50) NOT NULL,'
        'CLAS_DEFESA INT(0) NULL'
    ')'
)

INSERT_INTO_RACA = (
    f'INSERT INTO {TABLE_RACA} VALUES ('
        'NULL, ?, ?, ?, ?, ?, ?, ?'
    ')'
)

INSERT_INTO_CLASSE = (
    f'INSERT INTO {TABLE_CLASSE} VALUES ('
        'NULL, ?, ?, ?, ?, ?, ?, ?'
    ')'
)

SELECT_ALL_RACAS = (
    f'SELECT * FROM {TABLE_RACA}'
)

SELECT_ALL_CLASSES = (
    f'SELECT * FROM {TABLE_CLASSE}'
)

def conecta():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    return (connection,cursor)

connection, cursor = conecta()
cursor.execute(CRIAR_RACA)
connection.commit()

cursor.execute(CRIAR_CLASSE)
connection.commit()

cursor.execute(f'DELETE FROM {TABLE_RACA}')
connection.commit()

cursor.execute(f'DELETE FROM {TABLE_CLASSE}')
connection.commit()

cursor.execute(f'DELETE FROM sqlite_sequence')
connection.commit()

cursor.executemany(INSERT_INTO_RACA, (
                            ('Orc', 3, 4, -2, -1, 2, 10),
                            ('Humano', 1, -2, -1, 4, 2, 10),
                            ('Elfo', 1, 1, 3, -3, 2, 10),
                            ('Demônio', 2, -1, 3, -2, 3, 10),
                        )
)
connection.commit()

cursor.executemany(INSERT_INTO_CLASSE, (
                            ('Guerreiro', 0, 3, 0, 0, 0, 0),
                            ('Ladino', 0, 0, 4, 0, 0, 0),
                            ('Feiticeiro', 0, 0, 0, 3, 0, 0),
                            ('Bardo', 0, 0, 0, 0, 4, 0),
                        )
)
connection.commit()

cursor.execute(SELECT_ALL_RACAS)
racas = cursor.fetchall()
print(racas)

cursor.execute(SELECT_ALL_CLASSES)
classes = cursor.fetchall()
print(classes)

