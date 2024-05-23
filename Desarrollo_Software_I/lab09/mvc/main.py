
import tkinter as tk
from controlador.controller import Controller

class App:
    def __init__(self):
        window = tk.Tk()
        window.title("Prueba MVC con Pila")
        window.geometry("370x250")
        app = Controller(window)
        window.mainloop()

if __name__ == "__main__":
    App()
