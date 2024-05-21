from controlador.controller import *
from modelo.model import *
import tkinter as tk

class View:
    def __init__(self, window, controller):
        self.controller = controller

        self.item_entry = tk.Entry(window)
        self.item_entry.pack(pady = 10)

        self.add_button = tk.Button(window, text = "Agregar iten", command=self.controller.add_item)
        self.add_button.pack()

        self.item_listbox = tk.Listbox(window)
        self.item_listbox.pack()
        self.item_listbox.insert(tk.END, "Lista de actuales:")

    def update_list(self, items):
        self.item_listbox.delete(1, tk.END)
        for item in items:
            self.item_listbox.insert(tk.END, item)

    def clear_entry(self):
        self.item_entry.delete(0, tk.END)


