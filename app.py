
import tkinter as tk
from login import TelaLogin
from menu import TelaMenu
from database import criar_banco

if __name__ == "__main__":
    criar_banco() 
    TelaLogin().mainloop()  
