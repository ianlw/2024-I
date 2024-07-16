# from view.botones import Botones
import tkinter as tk
import re
from tkinter import messagebox

class BotonesController():
    def __init__(self, infijo_a_posfijo, simbolos_agrupacion_balanceados, controller, undo_redo, input, output, boton_undo, boton_redo):
        self.infijo_a_posfijo = infijo_a_posfijo
        self.simbolos_agrupacion_balanceados = simbolos_agrupacion_balanceados
        self.controller = controller
        self.undo_redo = undo_redo
        self.input = input
        self.output = output
        self.botonUndo = boton_undo
        self.botonRedo = boton_redo

    # Función que informa sobre un error a través de una ventana emerjente 
    def mensaje(self, titulo, contenido):
        messagebox.showerror(titulo,contenido)

    # Función que añade el valor de cada botón a la pantalla de entrada
    def add_to_expression(self, value):
        self.insert_char(value)
        self.botonUndo.configure(state="normal")
        current_expression = self.input.get()
        self.input.delete(0, tk.END)
        self.input.insert(tk.END, current_expression + str(value))
    
    #Función que borra el último elemento de la expresión que se muestra en pantalla
    def delete_last_digit(self):
        current_expression = self.input.get()
        new_expression = current_expression[:-1]  # Eliminar el último dígito
        self.input.delete(0, tk.END)
        self.input.insert(tk.END, new_expression)
        self.undo_operation()

    # Función que elimina o limpia el contenido de las pantallas input y output
    def clear_all(self):
        self.botonRedo.configure(state="disabled")
        self.botonUndo.configure(state="disabled")
        self.input.delete(0, tk.END)
        self.output.config(text="-")
        self.clear_action()

    # Función que calcula la expresión de la pantalla de entrada
    def calculate(self):
        expression = self.input.get()
        # Verificar si la expresión está balanceada
        if (self.simbolos_agrupacion_balanceados.simbolos_agrupacion_balanceados(expression)):
            # Verificar que la expresión no presente errores de inconsistencia o lógica
            if (re.search(r'[\+\-\*/]{2,}', expression) or 
                re.search(r'^[\+\*/]', expression) or 
                re.search(r'[\+\-\*/]$', expression) or 
                re.search(r'\(\)', expression) or 
                re.search(r'[\+\-\*/]\(\)', expression) or 
                re.search(r'\(\)[\+\-\*/]', expression) or 
                re.search(r'[\{\}]', expression) or 
                re.search(r'[\[\]]', expression) or 
                re.search(r'\d\(', expression) or 
                re.search(r'\)\d', expression)):

                self.mensaje("Error en la expresion", "La expresion escrita no es correcta")
            else:
                # Transformar la expresión infija a posfija
                posfijo = self.infijo_a_posfijo.infijo_to_posfijo(expression)
                # Procesar la expresión posfija 
                result = self.controller.process_expression(posfijo)
                self.output.config(text=str(result))
        else:
            self.mensaje("Error en la expresion","La expresion no está balanceada en los símbolos de agrupación")


    # Función para permitir el ingreso de elementos y acciones desde el teclado 
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

    # Operación de deshacer
    def undo_operation(self, event=None):
        self.actualizar_boton_undo()
        if self.undo_redo.undo():
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, self.undo_redo.show()) 

    # Operación de rehacer
    def redo_operation(self, event=None):
        self.actualizar_boton_redo()
        if self.undo_redo.redo():
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, self.undo_redo.show()) 

    # Funció que actualiza el estado del botón undo
    def actualizar_boton_undo(self):
        if not self.undo_redo.undo_one_element():
            self.botonUndo.configure(state="normal")
        else:
            self.botonUndo.configure(state="disabled")

        if not self.undo_redo.redo_one_element():
            self.botonRedo.configure(state="normal")

    # Funció que actualiza el estado del botón redo 
    def actualizar_boton_redo(self):
        if not self.undo_redo.redo_one_element():
            self.botonRedo.configure(state="normal")
        else:
            self.botonRedo.configure(state="disabled")

        if not self.undo_redo.undo_one_element():
            self.botonUndo.configure(state="normal")

    # Funció que actualiza el estado del botón undo y redo 
    def actualizar_botones(self):
        if not self.undo_redo.undo_one_element():
            self.botonUndo.configure(state="normal")
        else:
            self.botonUndo.configure(state="disabled")

        if not self.undo_redo.redo_one_element():
            self.botonRedo.configure(state="normal")
        else:
            self.botonRedo.configure(state="disabled")

    # Función que inserta el valor en la pila input
    def insert_char(self, char):
        self.undo_redo.input_char(char)

    # Función que inserta el valor en la pila redo 
    def insert_char_redo(self, char):
        self.undo_redo.input_char_redo(char)

    # Limpiar las pilas
    def clear_action(self):
        self.undo_redo.clear()

