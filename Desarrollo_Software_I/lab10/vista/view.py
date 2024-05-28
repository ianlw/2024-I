from tkinter import Tk, Text, Button, END

class View:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.pantalla = Text(ventana, state='disabled', width=40, height=3, 
                                    background='white', foreground='blue', font=('Helvetica', 15))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.operacion = ""

    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    def mostrarPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
