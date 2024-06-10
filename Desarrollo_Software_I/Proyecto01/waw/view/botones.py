import tkinter as tk
from tkinter import messagebox
import re

class Botones():
    def __init__(self, master, undo_redo, controller,  input, output):
        # super().__init__(master)
        self.master = master
        self.undo_redo = undo_redo
        self.controller = controller
        self.input = input
        self.output = output

        bg_window = "#F5F5F5"
        foreground = "#000000"
        bg_simbolos_agrupacion = "#EFBC9B"
        bg_accion = "#FBF3D5"
        bg_numeros = "#D6DAC8"
        bg_operaciones= "#9CAFAA"

        padx_simbolos_agrupacion = 24
        pady_simbolos_agrupacion = 15

        padx_operaciones = 40
        pady_operaciones = 17

        botonesSAgrupamientoFrame = tk.Frame(master, bg=bg_window)
        botonesSAgrupamientoFrame.grid(row=1, column=0, columnspan=5, pady=2)

        # Crear y colocar los botones en el marco
        botonParentesisIzquierdo = tk.Button(botonesSAgrupamientoFrame, text="(", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.add_to_expression("("))
        botonParentesisIzquierdo.grid(row=0, column=0, padx=2)

        botonParentesisDerecho = tk.Button(botonesSAgrupamientoFrame, text=")", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.add_to_expression(")"))
        botonParentesisDerecho.grid(row=0, column=1, padx=2)

        botonLlaveIzquierda = tk.Button(botonesSAgrupamientoFrame, text="{", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.add_to_expression("{"))
        botonLlaveIzquierda.grid(row=0, column=2, padx=2)

        botonLlaveDerecha = tk.Button(botonesSAgrupamientoFrame, text="}", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.add_to_expression("}"))
        botonLlaveDerecha.grid(row=0, column=3, padx=2)

        botonCorcheteIzquierdo = tk.Button(botonesSAgrupamientoFrame, text="[", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.add_to_expression("["))
        botonCorcheteIzquierdo.grid(row=0, column=4, padx=2)

        botonCorcheteIzquierdo = tk.Button(botonesSAgrupamientoFrame, text="]", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.add_to_expression("]"))
        botonCorcheteIzquierdo.grid(row=0, column=5, padx=2)


        botonesAccionFrame = tk.Frame(master, bg=bg_window)
        botonesAccionFrame.grid(row=2, column=0, columnspan=5, pady=2)

        self.botonUndo = tk.Button(botonesAccionFrame,state="disabled", text="⟲", font=('Cartograph CF', 21, 'normal'), bg=bg_accion, fg=foreground, padx=27, pady=16, borderwidth=0, command=self.undo_operation)
        self.botonUndo.grid(row=0, column=0, padx=2, pady=2)

        self.botonRedo = tk.Button(botonesAccionFrame, state="disabled", text="⟳", font=('Cartograph CF', 21, 'normal'), bg=bg_accion, fg=foreground, padx=27, pady=16, borderwidth=0, command=self.redo_operation)
        self.botonRedo.grid(row=0, column=1, padx=2, pady=2)

        botonDelete = tk.Button(botonesAccionFrame, text="Delete", bg=bg_accion, fg=foreground, padx=25, pady=22, borderwidth=0, command=self.delete_last_digit)
        botonDelete.grid(row=0, column=2, padx=2, pady=2)

        botonClear = tk.Button(botonesAccionFrame, text="Clear", bg=bg_accion, fg=foreground, padx=28, pady=22, borderwidth=0, command=self.clear_all)
        botonClear.grid(row=0, column=3, padx=2, pady=2)

        botonesNumerosFrame = tk.Frame(master, bg=bg_window)                                                                  
        botonesNumerosFrame.grid(row=3, column=0, columnspan=3, pady=2)      


        boton1 = tk.Button(botonesNumerosFrame, text="1", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("1"))
        boton1.grid(row=0, column=0, padx=2, pady=2)

        boton2 = tk.Button(botonesNumerosFrame, text="2", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("2"))
        boton2.grid(row=0, column=1, padx=2, pady=2)

        boton3 = tk.Button(botonesNumerosFrame, text="3", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("3"))
        boton3.grid(row=0, column=2, padx=2, pady=2)

        boton4 = tk.Button(botonesNumerosFrame, text="4", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("4"))
        boton4.grid(row=1, column=0, padx=2, pady=2)

        boton5 = tk.Button(botonesNumerosFrame, text="5", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("5"))
        boton5.grid(row=1, column=1, padx=2, pady=2)

        boton6 = tk.Button(botonesNumerosFrame, text="6", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("6"))
        boton6.grid(row=1, column=2, padx=2, pady=2)

        boton7 = tk.Button(botonesNumerosFrame, text="7", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("7"))
        boton7.grid(row=2, column=0, padx=2, pady=2)

        boton8 = tk.Button(botonesNumerosFrame, text="8", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("8"))
        boton8.grid(row=2, column=1, padx=2, pady=2)

        boton9 = tk.Button(botonesNumerosFrame, text="9", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("9"))
        boton9.grid(row=2, column=2, padx=2, pady=2)


        # Boton Igual
        botonIgual = tk.Button(botonesNumerosFrame, text="=", bg=foreground, fg="white", padx=40, pady=25, borderwidth=0, command= self.calculate)
        botonIgual.grid(row=3, column=0, padx=2, pady=2)
        #Boton Cero
        boton0 = tk.Button(botonesNumerosFrame, text="0", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("0"))
        boton0.grid(row=3, column=1, padx=2, pady=2)
        #Boton .
        botonPunto = tk.Button(botonesNumerosFrame, text=".", bg=bg_numeros, fg="black", padx=40, pady=25, borderwidth=0, command=lambda: self.add_to_expression("."))
        botonPunto.grid(row=3, column=2, padx=2, pady=2)

        operacionesFrame = tk.Frame(master, bg=bg_window)
        operacionesFrame.grid(row=3, column=4, columnspan=5, pady=2)

        #Botones de operacion
        botonMas = tk.Button(operacionesFrame, text="+", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.add_to_expression("+"))
        botonMas.grid(row=1, column=0, padx=2, pady=2)

        botonMenos = tk.Button(operacionesFrame, text="-", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.add_to_expression("-"))
        botonMenos.grid(row=2, column=0, padx=2, pady=2)

        botonMul = tk.Button(operacionesFrame, text="*", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.add_to_expression("*"))
        botonMul.grid(row=3, column=0, padx=2, pady=2)

        botonDiv = tk.Button(operacionesFrame, text="/", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.add_to_expression("/"))
        botonDiv.grid(row=4, column=0, padx=2, pady=2)

        botonPotencia = tk.Button(operacionesFrame, text="^", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.add_to_expression("^"))
        botonPotencia.grid(row=5, column=0, padx=2, pady=2)
        self.master.bind("<Key>", self.handle_keypress)

        self.master.bind("<Control-z>", self.undo_operation)
        self.master.bind("<Control-y>", self.redo_operation)

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

            if (re.search(r'[\+\-\*/]{2,}', expression) or 
                re.search(r'^[\+\*/]', expression) or 
                re.search(r'[\+\-\*/]$', expression) or 
                re.search(r'\(\)', expression) or 
                re.search(r'[\+\-\*/]\(\)', expression) or 
                re.search(r'\(\)[\+\-\*/]', expression) or 
                re.search(r'\{\}', expression) or 
                re.search(r'\[\]', expression) or 
                re.search(r'\d\(', expression) or 
                re.search(r'\)\d', expression)):
                # self.output.config(text="Expresion erronea")
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
