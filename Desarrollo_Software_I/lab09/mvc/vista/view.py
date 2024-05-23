
import tkinter as tk

class View:
    def __init__(self, window, controller):
        self.controller = controller

        self.item_entry = tk.Entry(window)
        self.item_entry.pack(pady=10)

        self.add_button = tk.Button(window, text="Agregar item", command=self.controller.add_item)
        self.add_button.pack()

        self.pop_button = tk.Button(window, text="Sacar item", command=self.controller.remove_item)
        self.pop_button.pack()

        self.clear_button = tk.Button(window, text="Limpiar lista", command=self.controller.clear_items)
        self.clear_button.pack()

        self.item_listbox = tk.Listbox(window)
        self.item_listbox.pack()
        self.item_listbox.insert(tk.END, "Lista de actuales:")

    def update_list(self, items):
        self.item_listbox.delete(1, tk.END)
        for item in items:
            self.item_listbox.insert(tk.END, item)

    def clear_entry(self):
        self.item_entry.delete(0, tk.END)
