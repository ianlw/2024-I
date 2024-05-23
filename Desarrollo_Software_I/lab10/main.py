from tkinter import Tk
from controlador.controller import Controller

ventanaPrincipal = Tk()
calculadora = Controller(ventanaPrincipal)
ventanaPrincipal.mainloop()
