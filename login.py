import tkinter as tk
from tkinter import messagebox
from models import usuario_por_login, registrar_usuario
from menu import TelaMenu

class TelaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clínica Total Saúde - Login")
        self.geometry("360x260")
        self.resizable(False, False)

        frame = tk.Frame(self, padx=10, pady=10)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="E-mail").pack(anchor="w")
        self.email = tk.Entry(frame)
        self.email.pack(fill="x", pady=4)

        tk.Label(frame, text="Senha").pack(anchor="w")
        self.senha = tk.Entry(frame, show="*")
        self.senha.pack(fill="x", pady=4)

        tk.Button(frame, text="Entrar", command=self.entrar).pack(fill="x", pady=6)
        tk.Button(frame, text="Registrar novo usuário", command=self.abrir_registro).pack(fill="x")

    def entrar(self):
        email = self.email.get().strip()
        senha = self.senha.get().strip()
        if not email or not senha:
            messagebox.showwarning("Aviso", "Preencha e-mail e senha.")
            return
        user = usuario_por_login(email, senha)
        if user:
            messagebox.showinfo("Bem-vindo", f"Acesso permitido: {user[1]}")
            self.destroy()
            TelaMenu().mainloop()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

    def abrir_registro(self):
        TelaRegistro(self)

class TelaRegistro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registrar Usuário (Recepção)")
        self.geometry("380x280")
        self.resizable(False, False)

        frame = tk.Frame(self, padx=10, pady=10)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="Nome").grid(row=0, column=0, sticky="w")
        self.nome = tk.Entry(frame); self.nome.grid(row=0, column=1, sticky="ew", pady=4)

        tk.Label(frame, text="E-mail").grid(row=1, column=0, sticky="w")
        self.email = tk.Entry(frame); self.email.grid(row=1, column=1, sticky="ew", pady=4)

        tk.Label(frame, text="Senha").grid(row=2, column=0, sticky="w")
        self.senha = tk.Entry(frame, show="*"); self.senha.grid(row=2, column=1, sticky="ew", pady=4)

        frame.columnconfigure(1, weight=1)

        btns = tk.Frame(frame); btns.grid(row=3, column=0, columnspan=2, pady=8, sticky="ew")
        tk.Button(btns, text="Registrar", command=self.registrar).pack(side="left")
        tk.Button(btns, text="Fechar", command=self.destroy).pack(side="right")

    def registrar(self):
        ok, msg = registrar_usuario(self.nome.get().strip(), self.email.get().strip(), self.senha.get().strip())
        if ok:
            messagebox.showinfo("Sucesso", msg); self.destroy()
        else:
            messagebox.showerror("Erro", msg)
