
import tkinter as tk
from tkinter import messagebox, ttk
from models import listar_pacientes, alterar_status

class TelaAtendimentos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Atendimentos - Status")
        self.geometry("820x520")
        self.resizable(False, False)

        tk.Label(self, text="Fila / Status de Atendimentos", font=("Arial", 14, "bold")).pack(pady=8)

        cols = ("id", "nome", "idade", "medico", "especialidade", "status")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=15)
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("idade", text="Idade")
        self.tree.heading("medico", text="Médico")
        self.tree.heading("especialidade", text="Especialidade")
        self.tree.heading("status", text="Status")
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("idade", width=70, anchor="center")
        self.tree.column("status", width=110, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=12, pady=6)

        btns = tk.Frame(self); btns.pack(pady=8)
        tk.Button(btns, text="Marcar como ATENDIDO", command=lambda: self.mudar_status("atendido")).pack(side="left", padx=6)
        tk.Button(btns, text="Marcar como PENDENTE", command=lambda: self.mudar_status("pendente")).pack(side="left", padx=6)
        tk.Button(btns, text="Recarregar", command=self.carregar).pack(side="left", padx=6)

        self.carregar()

    def carregar(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for (pid, nome, idade, medico, esp, status, _med_id) in listar_pacientes():
            self.tree.insert("", "end", values=(pid, nome, idade, medico, esp, status))

    def selecionado(self):
        sel = self.tree.selection()
        return sel[0] if sel else None

    def mudar_status(self, novo_status):
        sel = self.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Selecione um paciente na lista.")
            return
        pid = self.tree.item(sel)["values"][0]
        alterar_status(pid, novo_status)  
        self.carregar()
        messagebox.showinfo("Status", f"Status alterado para '{novo_status}'.")
