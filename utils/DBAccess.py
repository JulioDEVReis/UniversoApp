import sqlite3

db = 'database/frases.db'


def db_consulta(consulta, parametros=()):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchall()
        con.commit()
        return resultado


def buscar_frase_aleatoria_BD():
    # TABLESAMPLE busca uma linha de forma aleatória na tabela do banco de dados.
    # ORDER BY random() usamos também para resgatar em caso de poucas linhas na tabela. Podemos complementar
    # com LIMIT 5, por exemplo, para pegar 5 frases aleatórias
    query = 'SELECT frase FROM frase ORDER BY random()'
    registos = db_consulta(query)
    return registos[0] if registos else None


def buscar_tres_frases_BD():
    query = 'SELECT frase FROM frase ORDER BY random() LIMIT 3'
    registos = db_consulta(query)
    return registos[:3]


"""def mostrar_todas_frases_BD():
    query = 'SELECT frase FROM frase'
    registos = db_consulta(query)
    return registos


def add_frase_BD(parametros):
    query = 'INSERT INTO frase VALUES(NULL, ?, ?)'
    db_consulta(query, parametros)"""
