import sys
import os

# Agregar ruta relativa al directorio principal del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logica.conection import CConexion

import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter import messagebox  #mensaje pop

#from logica.conection import CConexion

class FormularioUser:
    
    def __init__(self, base):
        self.base = base
       
        self.base.title("Formulario User")
        self.base.geometry("500x500")
        self.base.configure(bg="gray")
        self.base.resizable(False, False)
    
        self.lbl_nombre = tk.Label(self.base, text="Nombre:", bg="gray")
        self.lbl_nombre.pack(pady=10, padx=10, anchor="w")

        self.text_box_nombre = tk.Entry(self.base,show="")
        self.text_box_nombre.pack(pady=10, padx=10, anchor="w")

        self.lbl_apellido = tk.Label(self.base, text="Apellido:", bg="gray")
        self.lbl_apellido.pack(pady=10, padx=10, anchor="w")

        self.text_box_apellido = tk.Entry(self.base,show="")
        self.text_box_apellido.pack(pady=10, padx=10, anchor="w")

        self.lbl_email = tk.Label(self.base, text="Email:", bg="gray")   
        self.lbl_email.pack(pady=10, padx=10, anchor="w")

        self.text_box_email = tk.Entry(self.base,show="")
        self.text_box_email.pack(pady=10, padx=10, anchor="w")  

        self.lbl_password = tk.Label(self.base, text="Contraseña:", bg="gray")
        self.lbl_password.pack(pady=10, padx=10, anchor="w")
        
        self.text_box_password = tk.Entry(self.base, show="*")
        self.text_box_password.pack(pady=10, padx=10, anchor="w")

        self.lbl_rol = tk.Label(self.base, text="Rol:", bg="gray")
        self.lbl_rol.pack(pady=10, padx=10, anchor="w")
        
        self.text_box_rol = tk.Entry(self.base, show="*")
        self.text_box_rol.pack(pady=10, padx=10, anchor="w")

        self.btn_regresar = tk.Button(self.base, text="Regresar", command=self.cerrar_ventana)
        self.btn_regresar.pack(pady=10, padx=10, anchor="e")

        self.btn_guardar = tk.Button(self.base, text="Guardar", command=self.guardar_usuario)
        self.btn_guardar.pack(pady=10, padx=10, anchor="w")

    def guardar_usuario(self):
        CConexion.insert_user(
            self.text_box_nombre.get(),
            self.text_box_apellido.get(),
            self.text_box_email.get(),
            self.text_box_password.get(),
            self.text_box_rol.get()
        )
        messagebox.showinfo("Guardar", "Usuario guardado exitosamente")

    def cerrar_ventana(self):
        self.base.destroy()
        

if __name__ == "__main__":
    base = tk.Tk()
    FormularioUser(base)
    base.mainloop()