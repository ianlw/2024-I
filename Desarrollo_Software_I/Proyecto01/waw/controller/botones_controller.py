import tkinter as tk
import re
from tkinter import messagebox

class BotonesController():
    def __init__(self, master, undo_redo, controller,  input, output, botonUndo, botonRedo):
        self.master = master
        self.undo_redo = undo_redo
        self.controller = controller
        self.input = input
        self.output = output
        self.botonUndo = botonUndo
        self.botonRedo =botonRedo

    def mensaje(self, titulo, contenido):
        messagebox.showerror(titulo,contenido)

    def actualizar_boton_undo(self):

        if not self.undo_redo.undo_one_element():
            self.botonUndo.configure(state="normal")
        else:
            self.botonUndo.configure(state="disabled")

        if not self.undo_redo.redo_one_element():
            self.botonRedo.configure(state="normal")
        # else:
            # self.botonRedo.configure(state="disabled")

    def actualizar_boton_redo(self):
        if not self.undo_redo.redo_one_element():
            self.botonRedo.configure(state="normal")
        else:
            self.botonRedo.configure(state="disabled")

        if not self.undo_redo.undo_one_element():
            self.botonUndo.configure(state="normal")
        # else:
            # self.botonRedo.configure(state="disabled")

    def actualizar_botones(self):
        if not self.undo_redo.undo_one_element():
            self.botonUndo.configure(state="normal")
        else:
            self.botonUndo.configure(state="disabled")

        if not self.undo_redo.redo_one_element():
            self.botonRedo.configure(state="normal")
        else:
            self.botonRedo.configure(state="disabled")

    def add_to_expression(self, value):
        self.insert_char(value)
        print("WAWA")
        # self.actualizar_botones()
        self.botonUndo.configure(state="normal")
        current_expression = self.input.get()
        self.input.delete(0, tk.END)
        self.input.insert(tk.END, current_expression + str(value))
    
    def delete_last_digit(self):
        current_expression = self.input.get()
        new_expression = current_expression[:-1]  # Eliminar el último dígito
        self.input.delete(0, tk.END)
        self.input.insert(tk.END, new_expression)
        # self.undo_redo.input_char_redo(current_expression[-1])
        self.undo_operation()
        # self.undo_redo.Redo.pop()

    def clear_all(self):
        print("WAW")
        self.botonRedo.configure(state="disabled")
        self.botonUndo.configure(state="disabled")
        self.input.delete(0, tk.END)
        self.output.config(text="-")
        self.clear_action()

    def calculate(self):
        print("WAW")
        expression = self.input.get()
        if (self.controller.simbolos_agrupacion_balanceado(expression)):

            if re.search(r'[\+\-\*/]{2,}', expression) or re.search(r'^[\+\*/]', expression) or re.search(r'[\+\-\*/]$', expression) or re.search(r'\(\)', expression) or re.search(r'[\+\-\*/]\(\)', expression) or re.search(r'\(\)[\+\-\*/]', expression) or re.search(r'[\{\}]', expression) or re.search(r'[\[\]]', expression) or re.search(r'\d\(', expression) or re.search(r'\)\d', expression):
                self.output.config(text="Expresion erronea")
                self.mensaje("Error en la expresion", "La expresion escrita no es correcta")

                
            else:
                posfijo = self.controller.infijo_to_posfijo(expression)
                result = self.controller.process_expression(posfijo)
                self.output.config(text=str(result))
        else:
            # self.output.config(text="Expresion no balanceada")
            self.mensaje("Error en la expresion","La expresion no está balanceada en los símbolos de agrupación")

    def validar_expresion(self):
        expression = self.input.get()
        if re.search(r'[\+\-\*/]{2,}', expression) or re.search(r'^[\+\*/]', expression) or re.search(r'[\+\-\*/]$', expression) or re.search(r'\(\)', expression) or re.search(r'[\+\-\*/]\(\)', expression) or re.search(r'\(\)[\+\-\*/]', expression):
            self.output.config(text="Expresion erronea")

    def handle_keypress(self, event):
        # Obtener el carácter presionado
        key = event.char
        # Si es un carácter válido (números, operadores, paréntesis)
        if len(key) == 1 and key.isprintable() and (key.isdigit() or key in "+-*/().{}[]"):
            self.add_to_expression(key)
        elif key == '\b':  # Manejar la tecla de retroceso
            self.delete_last_digit()
        elif key == '\r':  # Manejar la tecla Enter
            self.calculate()
        # elif len(key) == 1 and not key.isprintable():
            # return

    def undo_operation(self, event=None):
        self.actualizar_boton_undo()
        if self.undo_redo.undo():
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, self.undo_redo.show()) 

    def redo_operation(self, event=None):
        self.actualizar_boton_redo()
        if self.undo_redo.redo():
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, self.undo_redo.show()) 

    def insert_char(self, char):
        self.undo_redo.input_char(char)

    def insert_char_redo(self, char):
        self.undo_redo.input_char_redo(char)

    def clear_action(self):
        self.undo_redo.clear()

