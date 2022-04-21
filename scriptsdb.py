import json
import database as db
import pandas as pd
import csv

tables = ['qualis', 'researchers']

# Dropando a tabelas caso elas já existam
for table in tables:
    sql = 'DROP TABLE {}'.format(table)
    db.create_db(sql)

# Criando a tabelas
sql = '''CREATE TABLE researchers( 
        nome_completo       VARCHAR(150), 
        citacao             VARCHAR(75),
        citacao_nCompleto   VARCHAR(75),
        categoria           VARCHAR(25),
        PRIMARY KEY (nome_completo, citacao)
        )'''

db.create_db(sql)

sql = '''CREATE TABLE qualis(
        issn          VARCHAR(10), 
        nome          VARCHAR(255), 
        qualis        VARCHAR(3),
        PRIMARY KEY (issn, nome)
        )'''

db.create_db(sql)

# inserindo dados na tabela
# researchers 
with open('PPCICresearchers.json', encoding='utf-8') as fileR:
    researchers = json.load(fileR)
    
    for category in researchers:
        for researcher in researchers[category]:
            for citations in researchers[category][researcher]:
                cit = ', '.join(citations)
                citNC = citations[1]+ ' ' + citations[0]
                sql = "INSERT INTO researchers (nome_completo, citacao, citacao_nCompleto, categoria) VALUES ('{}', '{}', '{}')".format(researcher, cit, citNC, category[6:])
                db.insert_db(sql)

# qualis
with open('qualis.csv', encoding='utf-8') as fileQ:
    table = csv.reader(fileQ)
    
    for line in table:
        if (line[0]!='ISSN'):
            sql = "INSERT INTO qualis (issn, nome, qualis) VALUES ('{}', '{}', '{}')".format(line[0], line[1].replace("'",""), line[2])
            db.insert_db(sql)
