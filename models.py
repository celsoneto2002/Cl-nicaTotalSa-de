from database import conectar


def usuario_por_login(email, senha):
    conn = conectar(); c = conn.cursor()
    c.execute("SELECT id, nome FROM usuarios WHERE email=? AND senha=?", (email, senha))
    row = c.fetchone(); conn.close()
    return row

def registrar_usuario(nome, email, senha):
    conn = conectar(); c = conn.cursor()
    try:
        c.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)", (nome, email, senha))
        conn.commit()
        return True, "Usuário registrado!"
    except Exception:
        return False, "E-mail já cadastrado."
    finally:
        conn.close()


def criar_medico(nome, especialidade, crm):
    conn = conectar(); c = conn.cursor()
    try:
        c.execute("INSERT INTO medicos (nome, especialidade, crm) VALUES (?,?,?)", (nome, especialidade, crm))
        conn.commit(); return True, "Médico cadastrado!"
    except Exception:
        return False, "CRM já cadastrado."
    finally:
        conn.close()

def listar_medicos():
    conn = conectar(); c = conn.cursor()
    c.execute("SELECT id, nome, especialidade, crm FROM medicos ORDER BY nome")
    dados = c.fetchall(); conn.close()
    return dados

def atualizar_medico(medico_id, nome, especialidade, crm):
    conn = conectar(); c = conn.cursor()
    try:
        c.execute("UPDATE medicos SET nome=?, especialidade=?, crm=? WHERE id=?", (nome, especialidade, crm, medico_id))
        conn.commit(); return True, "Médico atualizado!"
    except Exception:
        return False, "CRM já existe para outro médico."
    finally:
        conn.close()

def excluir_medico(medico_id):
    conn = conectar(); c = conn.cursor()
    c.execute("UPDATE pacientes SET medico_id=NULL WHERE medico_id=?", (medico_id,))
    c.execute("DELETE FROM medicos WHERE id=?", (medico_id,))
    conn.commit(); conn.close()


def criar_paciente(nome, idade, medico_id, status="pendente"):
    conn = conectar(); c = conn.cursor()
    c.execute("INSERT INTO pacientes (nome, idade, medico_id, status) VALUES (?,?,?,?)", (nome, idade, medico_id, status))
    conn.commit(); conn.close()

def listar_pacientes():
    conn = conectar(); c = conn.cursor()
    c.execute("""
        SELECT p.id, p.nome, COALESCE(p.idade,0), COALESCE(m.nome, '—'), COALESCE(m.especialidade, '—'), p.status, p.medico_id
        FROM pacientes p
        LEFT JOIN medicos m ON m.id = p.medico_id
        ORDER BY p.nome
    """)
    dados = c.fetchall(); conn.close()
    return dados

def atualizar_paciente(paciente_id, nome, idade, medico_id, status):
    conn = conectar(); c = conn.cursor()
    c.execute("UPDATE pacientes SET nome=?, idade=?, medico_id=?, status=? WHERE id=?", (nome, idade, medico_id, status, paciente_id))
    conn.commit(); conn.close()

def excluir_paciente(paciente_id):
    conn = conectar(); c = conn.cursor()
    c.execute("DELETE FROM pacientes WHERE id=?", (paciente_id,))
    conn.commit(); conn.close()

def alterar_status(paciente_id, novo_status):
    conn = conectar(); c = conn.cursor()
    c.execute("UPDATE pacientes SET status=? WHERE id=?", (novo_status, paciente_id))
    conn.commit(); conn.close()
