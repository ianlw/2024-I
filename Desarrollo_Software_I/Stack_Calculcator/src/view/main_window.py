import tkinter as tk
from tkinter import PhotoImage
from view.botones import Botones

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Etablecer el color predeterminado de la ventana
        master.configure(bg="#F5F5F5")
        # Título de la ventana
        master.title("Calculadora MVC")
        # Ícono de la aplicación
        # icon = PhotoImage(file="$HOME/2024-I/Desarrollo_Software_I/Stack_Calculcator/img/StackCalculatorIcon.png")
        # master.iconphoto(False, icon)

        # Fuente por defecto de la aplicación
        self.default_font = ("Cascadia Code", 12)
        self.option_add("*Font", self.default_font)

        # Colores para los frames y pantallas
        bg_window = "#F5F5F5"
        bg_input ="#000000"
        bg_output = "#000000"

        # Creación del frame donde estarán las pantallas 
        self.input_output_frame = tk.Frame(master, bg=bg_window)
        self.input_output_frame.grid(row=0, column=0, columnspan=5, pady=2)

        # Creación de la pantalla de entrada
        self.input = tk.Entry(self.input_output_frame, width=22, bg=bg_input, fg="white", border=0, font=('Cartograph CF', 14, 'normal'), justify="right")
        self.input.grid(row=0, column=0, columnspan=4, padx=2, pady=2)


        # Creación de la pantalla de resultado o de salida
        self.output = tk.Label(self.input_output_frame, padx=2, pady=2, width=22, bg=bg_output, fg="white", borderwidth=0, font=('Cartograph CF', 14, 'normal'))
        self.output.grid(row=1, column=0, columnspan=4, padx=2, pady=2)
        self.output.config(justify="right", text="Resultado")
        
        # LLamar a la clase Botones para que estos se creen
        botones = Botones(master, self.input, self.output)
