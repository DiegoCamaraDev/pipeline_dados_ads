#regra de negocio: enriquecer os dados adicionando no destino um coluna para margem de lucros de cada produto
import csv
import sqlite3

#criar funcao para remover ponto da coluna preco_medio - utilizadi na funcao remover_ponto com o replace
def remover_ponto(valor):
    return int ((valor.replace('.', '')))

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
                receita_total INTEGER,
                margem_lucro REAL
            )''')
    #inserir cada linha do aquivo onde a quantidade for maior que 10
    for row in reader:
        if int(row[1]) > 10:               

            #remove o ponto da coluna preco_medio e transforma em inteiro
            row[3] = remover_ponto(row[3])

            #calcular a margem de lucro
            margem_lucro = (row[3] / float(row[1])) - float(row[2])

            #inserir o registro no banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))

    conn.commit()
    conn.close()

    print("Job executado com sucesso!") 