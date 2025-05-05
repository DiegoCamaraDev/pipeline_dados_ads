# 📊 Pipeline de Dados - Produção de Alimentos

Este projeto demonstra a construção de um pipeline de dados com foco em **extração**, **limpeza**, **transformação** e **enriquecimento** de informações contidas em um arquivo CSV. As operações foram desenvolvidas utilizando a linguagem **Python**, com o editor **Visual Studio Code**, e o banco de dados **SQLite3** para fins de armazenamento e consulta.

## 🧾 Descrição do Processo

O pipeline foi aplicado sobre o arquivo `producao_alimentos.csv`, que contém dados relacionados à produção de alimentos. As etapas executadas foram:

### 1. Criação do Banco de Dados
- Foi criado um banco de dados SQLite (`produtos.db`) com uma tabela para armazenar os registros processados.

### 2. Filtragem de Dados
- Foram inseridos apenas os produtos com **quantidade superior a 10 unidades**, conforme regra de negócio estabelecida.

### 3. Limpeza de Dados
- A coluna `preco_medio`, originalmente com valores utilizando ponto (`.`) como separador decimal, foi tratada para **remover o ponto** e converter os dados para o tipo **numérico (float)** corretamente.

### 4. Enriquecimento de Dados
- Foi adicionada uma nova coluna chamada `margem_lucro`, que representa a margem de lucro estimada de cada produto, calculada durante o processo de transformação.

### 5. Otimização e Formatação
- Os valores numéricos foram **arredondados** para melhor ocupação de memória e padronização dos dados no banco de dados.

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [SQLite3](https://www.sqlite.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- Bibliotecas padrão: `csv`, `sqlite3`

---

Este projeto tem como objetivo demonstrar as boas práticas de construção de um pipeline de dados simples, porém funcional, sendo possível expandi-lo para cenários mais complexos com uso de bibliotecas como **Pandas**, **SQL avançado** ou ferramentas de orquestração como **Apache Airflow**.


