
import tkinter as tk
from tkinter import messagebox, ttk
from models import listar_pacientes, criar_paciente, atualizar_paciente, excluir_paciente, listar_medicos

class TelaPacientes(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pacientes")
        self.geometry("840x540")
        self.resizable(False, False)

        tk.Label(self, text="Cadastro de Pacientes", font=("Arial", 14, "bold")).pack(pady=8)

        
        frm = tk.Frame(self); frm.pack(fill="x", padx=12)

        tk.Label(frm, text="Nome").grid(row=0, column=0, sticky="w")
        self.ent_nome = tk.Entry(frm); self.ent_nome.grid(row=0, column=1, sticky="ew", padx=6, pady=3)

        tk.Label(frm, text="Idade").grid(row=1, column=0, sticky="w")
        self.ent_idade = tk.Entry(frm); self.ent_idade.grid(row=1, column=1, sticky="ew", padx=6, pady=3)

        tk.Label(frm, text="Médico").grid(row=2, column=0, sticky="w")
        self.cb_medico = ttk.Combobox(frm, state="readonly"); self.cb_medico.grid(row=2, column=1, sticky="ew", padx=6, pady=3)

        tk.Label(frm, text="Status").grid(row=3, column=0, sticky="w")
        self.cb_status = ttk.Combobox(frm, state="readonly", values=["pendente", "atendido"])
        self.cb_status.grid(row=3, column=1, sticky="ew", padx=6, pady=3)
        self.cb_status.set("pendente")

        frm.columnconfigure(1, weight=1)

        btns = tk.Frame(self); btns.pack(fill="x", padx=12, pady=6)
        tk.Button(btns, text="Salvar / Cadastrar", command=self.salvar_novo).pack(side="left")
        tk.Button(btns, text="Atualizar Selecionado", command=self.atualizar_sel).pack(side="left", padx=6)
        tk.Button(btns, text="Excluir Selecionado", command=self.excluir_sel).pack(side="left")

        
        cols = ("id", "nome", "idade", "medico", "especialidade", "status", "medico_id")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=13)
        for c, txt, w in [
            ("id", "ID", 50),
            ("nome", "Nome", 200),
            ("idade", "Idade", 70),
            ("medico", "Médico", 180),
            ("especialidade", "Especialidade", 150),
            ("status", "Status", 100),
            ("medico_id", "medico_id", 0),
        ]:
            self.tree.heading(c, text=txt)
            self.tree.column(c, width=w, anchor="w")
        
        self.tree.column("medico_id", width=0, stretch=False)
        self.tree.pack(fill="both", expand=True, padx=12, pady=6)

        self.tree.bind("<<TreeviewSelect>>", self.preencher_form)

        
        self.map_medico_nome_por_id = {}
        self.map_medico_id_por_nome = {}
        self.carregar_medicos_cb()

        self.carregar()

    
    def limpar_form(self):
        self.ent_nome.delete(0, tk.END)
        self.ent_idade.delete(0, tk.END)
        if self.cb_medico["values"]:
            self.cb_medico.current(0)
        self.cb_status.set("pendente")

    def selecionado(self):
        sel = self.tree.selection()
        return sel[0] if sel else None

    def valores_sel(self):
        sel = self.selecionado()
        return self.tree.item(sel)["values"] if sel else None

    def carregar_medicos_cb(self):
        medicos = listar_medicos()  
        nomes = []
        self.map_medico_nome_por_id.clear()
        self.map_medico_id_por_nome.clear()
        for (mid, nome, _esp, _crm) in medicos:
            self.map_medico_nome_por_id[mid] = nome
            self.map_medico_id_por_nome[nome] = mid
            nomes.append(nome)
        if not nomes:
            nomes = ["—"]
        self.cb_medico["values"] = nomes
        if nomes:
            self.cb_medico.current(0)

    
    def carregar(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for (pid, nome, idade, medico_nome, esp, status, medico_id) in listar_pacientes():
            self.tree.insert("", "end", values=(pid, nome, idade, medico_nome, esp, status, medico_id))

    def preencher_form(self, _evt=None):
        vals = self.valores_sel()
        if not vals: return
        _id, nome, idade, medico_nome, _esp, status, _mid = vals
        self.ent_nome.delete(0, tk.END); self.ent_nome.insert(0, nome)
        self.ent_idade.delete(0, tk.END); self.ent_idade.insert(0, idade)
        
        if medico_nome in self.cb_medico["values"]:
            self.cb_medico.set(medico_nome)
        self.cb_status.set(status)

    def salvar_novo(self):
        nome = self.ent_nome.get().strip()
        idade = self.ent_idade.get().strip()
        medico_nome = self.cb_medico.get().strip()
        status = self.cb_status.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "Informe o nome do paciente.")
            return
        try:
            idade_int = int(idade) if idade else 0
        except ValueError:
            messagebox.showwarning("Aviso", "Idade inválida.")
            return

        medico_id = self.map_medico_id_por_nome.get(medico_nome, None)
        
        criar_paciente(nome, idade_int, medico_id, status)
        messagebox.showinfo("Cadastro", "Paciente cadastrado com sucesso!")
        self.limpar_form()
        self.carregar()

    def atualizar_sel(self):
        vals = self.valores_sel()
        if not vals:
            messagebox.showwarning("Aviso", "Selecione um paciente na lista.")
            return
        paciente_id = vals[0]
        nome = self.ent_nome.get().strip()
        idade = self.ent_idade.get().strip()
        medico_nome = self.cb_medico.get().strip()
        status = self.cb_status.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "Informe o nome do paciente.")
            return
        try:
            idade_int = int(idade) if idade else 0
        except ValueError:
            messagebox.showwarning("Aviso", "Idade inválida.")
            return

        medico_id = self.map_medico_id_por_nome.get(medico_nome, None)
        atualizar_paciente(paciente_id, nome, idade_int, medico_id, status)
        messagebox.showinfo("Atualização", "Paciente atualizado com sucesso!")
        self.carregar()

    def excluir_sel(self):
        vals = self.valores_sel()
        if not vals:
            messagebox.showwarning("Aviso", "Selecione um paciente na lista.")
            return
        if not messagebox.askyesno("Confirmar", "Deseja realmente excluir este paciente?"):
            return
        excluir_paciente(vals[0])
        self.limpar_form()
        self.carregar()
