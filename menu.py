
import tkinter as tk
from medicos import TelaMedicos
from pacientes import TelaPacientes
from atendimentos import TelaAtendimentos

class TelaMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clínica Total Saúde - Menu")
        self.geometry("420x300")
        self.resizable(False, False)

        tk.Label(self, text="Menu Principal", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self, text="Cadastro de Médicos", width=28, command=self.abrir_medicos).pack(pady=5)
        tk.Button(self, text="Cadastro de Pacientes", width=28, command=self.abrir_pacientes).pack(pady=5)
        tk.Button(self, text="Lista / Status de Atendimentos", width=28, command=self.abrir_atendimentos).pack(pady=5)
        tk.Button(self, text="Sair", width=28, command=self.destroy).pack(pady=20)

    def abrir_medicos(self):
       
        self.tela_medicos = TelaMedicos(self)  
        self.tela_medicos.grab_set()  

    def abrir_pacientes(self):
        
        self.tela_pacientes = TelaPacientes(self)  
        self.tela_pacientes.grab_set()  

    def abrir_atendimentos(self):
        
        self.tela_atendimentos = TelaAtendimentos(self) 
        self.tela_atendimentos.grab_set()  
