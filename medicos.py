
import tkinter as tk
from tkinter import messagebox, ttk
from models import listar_medicos, criar_medico, atualizar_medico, excluir_medico

class TelaMedicos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Médicos")
        self.geometry("700x480")
        self.resizable(False, False)

       
        tk.Label(self, text="Cadastro de Médicos", font=("Arial", 14, "bold")).pack(pady=8)

       
        frm = tk.Frame(self); frm.pack(fill="x", padx=12)

        tk.Label(frm, text="Nome").grid(row=0, column=0, sticky="w")
        self.ent_nome = tk.Entry(frm); self.ent_nome.grid(row=0, column=1, sticky="ew", padx=6, pady=3)

        tk.Label(frm, text="Especialidade").grid(row=1, column=0, sticky="w")
        self.ent_esp = tk.Entry(frm); self.ent_esp.grid(row=1, column=1, sticky="ew", padx=6, pady=3)

        tk.Label(frm, text="CRM").grid(row=2, column=0, sticky="w")
        self.ent_crm = tk.Entry(frm); self.ent_crm.grid(row=2, column=1, sticky="ew", padx=6, pady=3)

        frm.columnconfigure(1, weight=1)

        btns = tk.Frame(self); btns.pack(fill="x", padx=12, pady=6)
        tk.Button(btns, text="Salvar / Cadastrar", command=self.salvar_novo).pack(side="left")
        tk.Button(btns, text="Atualizar Selecionado", command=self.atualizar_sel).pack(side="left", padx=6)
        tk.Button(btns, text="Excluir Selecionado", command=self.excluir_sel).pack(side="left")

        
        cols = ("id", "nome", "especialidade", "crm")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("especialidade", text="Especialidade")
        self.tree.heading("crm", text="CRM")
        self.tree.column("id", width=50, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=12, pady=6)

        self.tree.bind("<<TreeviewSelect>>", self.preencher_form)

        self.carregar()

    
    def limpar_form(self):
        self.ent_nome.delete(0, tk.END)
        self.ent_esp.delete(0, tk.END)
        self.ent_crm.delete(0, tk.END)

    def selecionado(self):
        sel = self.tree.selection()
        return sel[0] if sel else None

    def valores_sel(self):
        sel = self.selecionado()
        return self.tree.item(sel)["values"] if sel else None

   
    def carregar(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for (id_, nome, esp, crm) in listar_medicos():
            self.tree.insert("", "end", values=(id_, nome, esp, crm))

    def preencher_form(self, _evt=None):
        vals = self.valores_sel()
        if not vals: return
        _id, nome, esp, crm = vals
        self.ent_nome.delete(0, tk.END); self.ent_nome.insert(0, nome)
        self.ent_esp.delete(0, tk.END); self.ent_esp.insert(0, esp)
        self.ent_crm.delete(0, tk.END); self.ent_crm.insert(0, crm)

    def salvar_novo(self):
        nome = self.ent_nome.get().strip()
        esp = self.ent_esp.get().strip()
        crm = self.ent_crm.get().strip()
        if not (nome and esp and crm):
            messagebox.showwarning("Aviso", "Preencha Nome, Especialidade e CRM.")
            return
        ok, msg = criar_medico(nome, esp, crm)
        messagebox.showinfo("Cadastro", msg)
        if ok:
            self.limpar_form()
            self.carregar()

    def atualizar_sel(self):
        vals = self.valores_sel()
        if not vals:
            messagebox.showwarning("Aviso", "Selecione um médico na lista.")
            return
        medico_id = vals[0]
        nome = self.ent_nome.get().strip()
        esp = self.ent_esp.get().strip()
        crm = self.ent_crm.get().strip()
        if not (nome and esp and crm):
            messagebox.showwarning("Aviso", "Preencha Nome, Especialidade e CRM.")
            return
        ok, msg = atualizar_medico(medico_id, nome, esp, crm)
        messagebox.showinfo("Atualização", msg)
        if ok:
            self.carregar()

    def excluir_sel(self):
        vals = self.valores_sel()
        if not vals:
            messagebox.showwarning("Aviso", "Selecione um médico na lista.")
            return
        if not messagebox.askyesno("Confirmar", "Deseja realmente excluir este médico?"):
            return
        excluir_medico(vals[0])  
        self.limpar_form()
        self.carregar()
