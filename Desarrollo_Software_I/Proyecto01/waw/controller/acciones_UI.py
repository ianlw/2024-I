from controller.app_controller import AppController  # Importa la clase Controlador desde el módulo controller
from view.main_window import MainWindow
# from view.botones import Botones
import tkinter as tk
from tkinter import messagebox
import re

class AcionesUI:
    def __init__(self):
        self.controlador = AppController()  # Crea una instancia del controlador
        self.master = tk.Tk()
        self.controlador = AppController()  # Crea una instancia del controlador
        self.main_window = MainWindow(self.master, self.controlador)  # Pasa el controlador a MainWindow
        # self.botones_frame = Botones(self.main_window, self.controlador)  # Pasa el controlador a Botones

    def mensaje(self, titulo, contenido):
        messagebox.showerror(titulo,contenido)

    def add_to_expression(self, value):
        self.insert_char(value)
        current_expression = self.main_window.input.get()
        print(value)
        self.main_window.input.delete(0, tk.END)
        self.main_window.input.insert(tk.END, current_expression + str(value))
    
    def delete_last_digit(self):
        print("WAW")
        current_expression = self.main_window.input.get()
        new_expression = current_expression[:-1]  # Eliminar el último dígito
        self.main_window.input.delete(0, tk.END)
        self.main_window.input.insert(tk.END, new_expression)
        self.undo_operation()

    def clear_all(self):
        print("WAW")
        self.main_window.input.delete(0, tk.END)
        self.main_window.output.config(text="-")
        self.clear_action()

    def calculate(self):
        print("WAW")
        expression = self.main_window.input.get()
        if (self.main_window.controller.simbolos_agrupacion_balanceado(expression)):

            if re.search(r'[\+\-\*/]{2,}', expression) or re.search(r'^[\+\*/]', expression) or re.search(r'[\+\-\*/]$', expression) or re.search(r'\(\)', expression) or re.search(r'[\+\-\*/]\(\)', expression) or re.search(r'\(\)[\+\-\*/]', expression) or re.search(r'[\{\}]', expression) or re.search(r'[\[\]]', expression) or re.search(r'\d\(', expression) or re.search(r'\)\d', expression):
                self.main_window.output.config(text="Expresion erronea")
                # self.mensaje("Error en la expresion", "La expresion escrita no es correcta")

                
            else:
                posfijo = self.main_window.controller.infijo_to_posfijo(expression)
                result = self.main_window.controller.process_expression(posfijo)
                self.main_window.output.config(text=str(result))
        else:
            # self.output.config(text="Expresion no balanceada")
            self.mensaje("Error en la expresion","La expresion no está balanceada en los símbolos de agrupación")

    def validar_expresion(self):
        expression = self.main_window.input.get()
        if re.search(r'[\+\-\*/]{2,}', expression) or re.search(r'^[\+\*/]', expression) or re.search(r'[\+\-\*/]$', expression) or re.search(r'\(\)', expression) or re.search(r'[\+\-\*/]\(\)', expression) or re.search(r'\(\)[\+\-\*/]', expression):
            self.main_window.output.config(text="Expresion erronea")

    def handle_keypress(self, event):
        # Obtener el carácter presionado
        character = event.char
        # Si es un carácter válido (números, operadores, paréntesis)
        if character.isdigit() or character in "+-*/().{}[]":
            self.add_to_expression(character)

    def undo_operation(self):
        if self.main_window.undo_redo.undo():
            self.main_window.input.delete(0, tk.END)
            self.main_window.input.insert(tk.END, self.main_window.undo_redo.show()) 

    def redo_operation(self):
        if self.main_window.undo_redo.redo():
            self.main_window.input.delete(0, tk.END)
            self.main_window.input.insert(tk.END, self.main_window.undo_redo.show()) 

    def delete_operation(self):
        if self.main_window.controller.delete():
            self.update_input_field()

    def insert_char(self, char):
        self.main_window.undo_redo.input_char(char)

    def clear_action(self):
        self.main_window.undo_redo.clear()



    def update_input_field(self):
        expression = self.main_window.controller.get_current_expression()
        self.main_window.input.delete(0, tk.END)
        self.main_window.input.insert(tk.END, expression)

