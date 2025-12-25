import sqlite3

# 1. Conectar (Cria o arquivo se não existir)
conexao = sqlite3.connect('meu_projeto.db')
cursor = conexao.cursor()

# 2. Criar Tabela (DDL)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')

# 3. Inserir Dados (DML) - Sempre use '?' para evitar SQL Injection
cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", ("Aprender Python",))

# 4. Commit e Close (Obrigatório para salvar!)
conexao.commit()
conexao.close()