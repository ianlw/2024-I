from modelo.model import Pila
from vista.view import View
import tkinter.messagebox as msg

class Controller:
    def __init__(self, window):
        self.window = window
        self.pila = Pila()
        self.view = View(window, self)

    def add_item(self):
        item = self.view.item_entry.get()
        if item:
            self.pila.push(item)
            self.view.update_list(self.pila.get_items())
            self.view.clear_entry()

    def remove_item(self):
        if not self.pila.is_empty():
            item = self.pila.pop()
            self.view.update_list(self.pila.get_items())
        else:
            msg.showinfo("Pila Vacía", "La pila está vacía. No se puede sacar ningún elemento.")

    def clear_items(self):
        if not self.pila.is_empty():
            self.pila.clear()
            self.view.update_list(self.pila.get_items())
        else:
            msg.showinfo("Pila Vacía", "La pila está vacía. No se puede limpiar.")
