import sqlite3

DB_NAME = "clinica.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_banco():
    conn = conectar()
    c = conn.cursor()

    
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    
    c.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            crm TEXT UNIQUE NOT NULL
        )
    """)

   
    c.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            medico_id INTEGER,
            status TEXT NOT NULL DEFAULT 'pendente',
            FOREIGN KEY (medico_id) REFERENCES medicos(id)
        )
    """)

    conn.commit()
    conn.close()
