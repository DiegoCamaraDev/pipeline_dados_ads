import csv
import sqlite3

#abre os arquivos CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r') as file:
    #criar leitor csv
    reader = csv.reader(file)
    #pular primeira linha
    next(reader)

    #conectar com o db
    conn= sqlite3.connect('dsadb.db')

    #deleta a tabela existente se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    #criar uma nova tabela
    conn.execute('''CREATE TABLE producao (
                produto TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                receita_total REAL
            )''')
    #inserir cada linha do aquivo onde a quantidade for maior que 10
    for row in reader:
        if int(row[1]) > 10:
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)   

    conn.commit()
    conn.close()

    print("Job executado com sucesso!") 