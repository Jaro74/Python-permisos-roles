import os
import sys

# Obtener la ruta del directorio principal del proyecto
directorio_principal = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Imprimir la ruta para verificar 
#print(f"Directorio principal: {directorio_principal}")
if directorio_principal not in sys.path:
    sys.path.insert(0, directorio_principal)

from IGU.interfaz_1 import FormularioGeneral
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    formulario = FormularioGeneral(root)
    root.mainloop()