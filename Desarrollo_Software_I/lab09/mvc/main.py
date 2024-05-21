from controlador.controller import *
from modelo.model import *
from vista.view import *

class App:
    def __init__(self):
        window = tk.Tk()
        window.title("Prueba MVC")
        window.geometry("370x250")
        app = Controller(window)
        window.mainloop()

if __name__ == "__main__":
    App()

