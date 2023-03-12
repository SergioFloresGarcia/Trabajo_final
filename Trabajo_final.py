from tkinter import ttk

from tkinter import *

import sqlite3

class product:
   def __init__(self, window):
     self.wind = window
     self.wind.litle('products aplication')

     #crear un frame dentro de contenedor

     frame = LabelFrame(self.wind, text='ferreteria el tornillo feliz')
     frame.grd(row=0, colum=0, columnspan=3, pady=10)

     #Entrada para el nombre:

     Label(frame, text='DNI ').grid(row=1, column=0)
     self.dni =Entry(frame)
     self.dni.focus()
     self.dni.grid(row=1, column=1)

     #Colocar otro elemento:

     Label(frame, text='Apellidos ').grid(row=2, column=0)
     self.apellido =Entry(frame)
     self.apellido.grid(row=2, column=1)

     Label(frame, text="Nombres ").grid(row=2, column=2)
     self.nombre =Entry(frame)
     self.nombre.grid(row=2, column=3)

     Label(frame, text="Direccion ").grid(row=3, column=0)
     self.direccion =Entry(frame)
     self.direccion.grid(row=3, column=1, columnspan=3, sticky= W + E)
     
     Label(frame, text="Cod pod ").grid(row=3, column=0)
     self.codpod =Entry(frame)
     self.codpod.grid(row=6, column=0, padx=3, pady=3, sticky="W")

     Label(frame, text="Descripcion ").grid(row=5, column=1)
     self.descripcion =Entry(frame)
     self.descripcion.grid(row=6, column=1, padx=3, pady=3, sticky="W")

     Label(frame, text="Unidad ").grid(row=5, column=2)
     self.unidad =Entry(frame)
     self.unidad.grid(row=6, column=2, padx=3, pady=3, sticky="W")

     Label(frame, text="Cantidad ").grid(row=5, column=3)
     self.cantidad =Entry(frame)
     self.cantidad.grid(row=6, column=3, padx=3, pady=3, sticky="W")

     Label(frame, text="Precio ").grid(row=5, column=4)
     self.precio =Entry(frame)
     self.precio.grid(row=6, column=4, padx=10, pady=10, sticky="W")

     Label(frame, text="Subtotal ").grid(row=5, column=5)
     self.subtotal =Entry(frame)
     self.subtotal.grid(row=6, column=5, padx=10, pady=10, sticky="W")

if __name__== '__main__' :
   window = Tk()
   aplication =product(window)
   window.mainloop()