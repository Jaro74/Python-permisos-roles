import sys
import os

# Agregar ruta relativa al directorio principal del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logica.conection import CConexion


#importamos los módulos restantes de tkinter
import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter import messagebox  #mensaje pop
#from logica.conection import CConexion
from interfaz_2 import FormularioUser
class FormularioGeneral:
    
    def __init__(self, base):
        self.base = base
        
        self.base.title("Formulario General")
        self.base.geometry("500x500")
        self.base.configure(bg="gray")
        self.base.resizable(False, False)
        
        
        
        #creamos un label
        self.lbl_nombre = tk.Label(base, text="Nombre:", bg="gray")  #.grid(row=0, column=0)
        self.lbl_nombre.pack(pady=10, padx=10, anchor="w")
        #creamos un entry
        self.text_box_nombre = tk.Entry(base,show="") #.grid(row=0, column=1)
        self.text_box_nombre.pack(pady=10, padx=10, anchor="w")

        self.lbl_password = tk.Label(base, text="Contraseña:", bg="gray")
        self.lbl_password.pack(pady=10, padx=10, anchor="w")
        self.text_box_password = tk.Entry(base, show="*")
        self.text_box_password.pack(pady=10, padx=10, anchor="w")

        #creamos un boton
        self.btn_mostrar = tk.Button(base, text="Mostrar Contraseña", command=self.alternar_contrasenia)
        self.btn_mostrar.pack(pady=10)

        self.btn_entrar = tk.Button(base, text="Entrar", command=self.entrar)
        self.btn_entrar.pack(pady=10)


    def alternar_contrasenia(self):
        current_show = self.text_box_password.cget('show')
        if current_show == '*':
            self.text_box_password.config(show = "")
            self.btn_mostrar.config(text="Ocultar Contraseña")
        else:
            self.text_box_password.config(show='*')
            self.btn_mostrar.config(text="Mostrar Contraseña")
    
    def entrar(self):
        resultado = CConexion.get_users()
        for user in resultado:
            if user[0] == self.text_box_nombre.get() and user[1] == self.text_box_password.get():
                nueva_ventana = tk.Toplevel(self.base)
                FormularioUser(nueva_ventana)
                messagebox.showinfo("Entrar", "Bienvenido al sistema")
                return
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

if __name__ == "__main__":
    base = tk.Tk()
    FormularioGeneral(base)
    base.mainloop()