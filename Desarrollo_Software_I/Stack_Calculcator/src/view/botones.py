import tkinter as tk
from model.infijo_a_posfijo import InfijoAPosfijo
from model.simbolos_agrupacion_balanceados import SimbolosAgrupacionBalanceados
from controller.app_controller import AppController
from controller.undo_redo import UndoRedo
from controller.botones_controller import BotonesController

class Botones():
    def __init__(self, master, input, output):
        # super().__init__(master)
        self.master = master
        self.infijo_a_posfijo = InfijoAPosfijo()
        self.simbolos_agrupacion_balanceados = SimbolosAgrupacionBalanceados()
        self.controller = AppController()
        self.undo_redo = UndoRedo()
        self.input = input
        self.output = output

        self.botones_controller = BotonesController(self.infijo_a_posfijo, self.simbolos_agrupacion_balanceados, self.controller, self.undo_redo, self.input, self.output, None, None)

        # Colores y configuraciones que se usarán en los botones
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

        # Creación del frame de los símbolos de agrupamiento
        botonesSAgrupamientoFrame = tk.Frame(master, bg=bg_window)
        botonesSAgrupamientoFrame.grid(row=1, column=0, columnspan=5, pady=2)

        # Crear y colocar los botones de símbolos de agrupamiento 
        botonParentesisIzquierdo = tk.Button(botonesSAgrupamientoFrame, text="(", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("("))
        botonParentesisIzquierdo.grid(row=0, column=0, padx=2)

        botonParentesisDerecho = tk.Button(botonesSAgrupamientoFrame, text=")", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.botones_controller.add_to_expression(")"))
        botonParentesisDerecho.grid(row=0, column=1, padx=2)

        botonLlaveIzquierda = tk.Button(botonesSAgrupamientoFrame, text="{", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("{"))
        botonLlaveIzquierda.grid(row=0, column=2, padx=2)

        botonLlaveDerecha = tk.Button(botonesSAgrupamientoFrame, text="}", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("}"))
        botonLlaveDerecha.grid(row=0, column=3, padx=2)

        botonCorcheteIzquierdo = tk.Button(botonesSAgrupamientoFrame, text="[", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("["))
        botonCorcheteIzquierdo.grid(row=0, column=4, padx=2)

        botonCorcheteIzquierdo = tk.Button(botonesSAgrupamientoFrame, text="]", bg=bg_simbolos_agrupacion, fg=foreground, padx=padx_simbolos_agrupacion, pady=pady_simbolos_agrupacion, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("]"))
        botonCorcheteIzquierdo.grid(row=0, column=5, padx=2)

        # Creación del frame de los botones de acción 
        botonesAccionFrame = tk.Frame(master, bg=bg_window)
        botonesAccionFrame.grid(row=2, column=0, columnspan=5, pady=2)

        # Crear los botones de Undo y Redo después de inicializar el controlador
        self.botonUndo = tk.Button(botonesAccionFrame,state="disabled", text="⟲", font=('Cartograph CF', 21, 'normal'), bg=bg_accion, fg=foreground, padx=27, pady=16, borderwidth=0, command=self.botones_controller.undo_operation)
        self.botonRedo = tk.Button(botonesAccionFrame,state="disabled", text="⟳", font=('Cartograph CF', 21, 'normal'), bg=bg_accion, fg=foreground, padx=27, pady=16, borderwidth=0, command=self.botones_controller.redo_operation)
        # Asignar los botones al controlador de expresiones
        self.botones_controller.botonUndo = self.botonUndo
        self.botones_controller.botonRedo = self.botonRedo
        # Colocar los botones en su posición
        self.botonUndo.grid(row=0, column=0, padx=2, pady=2)
        self.botonRedo.grid(row=0, column=1, padx=2, pady=2)

        botonDelete = tk.Button(botonesAccionFrame, text="Delete", bg=bg_accion, fg=foreground, padx=25, pady=22, borderwidth=0, command=self.botones_controller.delete_last_digit)
        botonDelete.grid(row=0, column=2, padx=2, pady=2)

        botonClear = tk.Button(botonesAccionFrame, text="Clear", bg=bg_accion, fg=foreground, padx=28, pady=22, borderwidth=0, command=self.botones_controller.clear_all)
        botonClear.grid(row=0, column=3, padx=2, pady=2)

        # Creación del frame de los botones de numeración 
        botonesNumerosFrame = tk.Frame(master, bg=bg_window)                                                                  
        botonesNumerosFrame.grid(row=3, column=0, columnspan=3, pady=2)      

        boton1 = tk.Button(botonesNumerosFrame, text="1", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("1"))
        boton1.grid(row=0, column=0, padx=2, pady=2)

        boton2 = tk.Button(botonesNumerosFrame, text="2", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("2"))
        boton2.grid(row=0, column=1, padx=2, pady=2)

        boton3 = tk.Button(botonesNumerosFrame, text="3", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("3"))
        boton3.grid(row=0, column=2, padx=2, pady=2)

        boton4 = tk.Button(botonesNumerosFrame, text="4", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("4"))
        boton4.grid(row=1, column=0, padx=2, pady=2)

        boton5 = tk.Button(botonesNumerosFrame, text="5", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("5"))
        boton5.grid(row=1, column=1, padx=2, pady=2)

        boton6 = tk.Button(botonesNumerosFrame, text="6", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("6"))
        boton6.grid(row=1, column=2, padx=2, pady=2)

        boton7 = tk.Button(botonesNumerosFrame, text="7", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("7"))
        boton7.grid(row=2, column=0, padx=2, pady=2)

        boton8 = tk.Button(botonesNumerosFrame, text="8", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("8"))
        boton8.grid(row=2, column=1, padx=2, pady=2)

        boton9 = tk.Button(botonesNumerosFrame, text="9", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("9"))
        boton9.grid(row=2, column=2, padx=2, pady=2)

        # Boton Igual
        botonIgual = tk.Button(botonesNumerosFrame, text="=", bg=foreground, fg="white", padx=40, pady=25, borderwidth=0, command= self.botones_controller.calculate)
        botonIgual.grid(row=3, column=0, padx=2, pady=2)

        #Boton Cero
        boton0 = tk.Button(botonesNumerosFrame, text="0", bg=bg_numeros, fg=foreground, padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("0"))
        boton0.grid(row=3, column=1, padx=2, pady=2)

        #Boton punto
        botonPunto = tk.Button(botonesNumerosFrame, text=".", bg=bg_numeros, fg="black", padx=40, pady=25, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("."))
        botonPunto.grid(row=3, column=2, padx=2, pady=2)

        # Creación del frame de los botones de las operaciones 
        operacionesFrame = tk.Frame(master, bg=bg_window)
        operacionesFrame.grid(row=3, column=4, columnspan=5, pady=2)

        #Botones de operacion
        botonMas = tk.Button(operacionesFrame, text="+", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("+"))
        botonMas.grid(row=1, column=0, padx=2, pady=2)

        botonMenos = tk.Button(operacionesFrame, text="-", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("-"))
        botonMenos.grid(row=2, column=0, padx=2, pady=2)

        botonMul = tk.Button(operacionesFrame, text="*", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("*"))
        botonMul.grid(row=3, column=0, padx=2, pady=2)

        botonDiv = tk.Button(operacionesFrame, text="/", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("/"))
        botonDiv.grid(row=4, column=0, padx=2, pady=2)

        botonPotencia = tk.Button(operacionesFrame, text="^", bg=bg_operaciones, fg="black", padx=padx_operaciones, pady=pady_operaciones, borderwidth=0, command=lambda: self.botones_controller.add_to_expression("^"))
        botonPotencia.grid(row=5, column=0, padx=2, pady=2)

        # Bindear las teclas respectivas para acciones específicas 
        self.master.bind("<Key>", self.botones_controller.handle_keypress)
        self.master.bind("<Control-z>", self.botones_controller.undo_operation)
        self.master.bind("<Control-y>", self.botones_controller.redo_operation)
