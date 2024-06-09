import tkinter as tk
# from tkinter import messagebox
from controller.undo_redo import UndoRedo
from view.botones import Botones

class MainWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
            # Vincular el evento de teclado a la entrada
        master.configure(bg="#F5F5F5")
        master.title("Calculadora MVC")
        self.controller = controller
        self.undo_redo = UndoRedo()

        self.default_font = ("Cascadia Code", 12)
        self.option_add("*Font", self.default_font)

        bg_window = "#F5F5F5"
        bg_input ="#000000"
        bg_output = "#000000"

        self.input_output_frame = tk.Frame(master, bg=bg_window)
        self.input_output_frame.grid(row=0, column=0, columnspan=5, pady=2)

        self.input = tk.Entry(self.input_output_frame, width=22, bg=bg_input, fg="white", border=0, font=('Cartograph CF', 14, 'normal'), justify="right")
        self.input.grid(row=0, column=0, columnspan=4, padx=2, pady=2)
        # self.master.bind("<Key>", self.handle_keypress)


        self.output = tk.Label(self.input_output_frame, padx=2, pady=2, width=22, bg=bg_output, fg="white", borderwidth=0, font=('Cartograph CF', 14, 'normal'))
        self.output.grid(row=1, column=0, columnspan=4, padx=2, pady=2)
        self.output.config(justify="right", text="Resultado")
        
        botones = Botones(master, self.undo_redo, controller, self.input, self.output)
