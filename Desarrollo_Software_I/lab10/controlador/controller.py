
import re
from modelo.model import Model
from vista.view import View
from tkinter import Button

class Controller:
    def __init__(self, ventana):
        self.model = Model()
        self.view = View(ventana)
        self.create_buttons()

    def create_buttons(self):
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        boton4 = self.crearBoton(u'\u232B', escribir=False)
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u'\u00F7')
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*")
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton("=", escribir=False, ancho=20, alto=2)
        botones = [boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        contador = 0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
        botones[16].grid(row=5, column=0, columnspan=4)

    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.view.ventana, text=valor, width=ancho, height=alto, font=('Helvetica',15), command=lambda:self.click(valor, escribir))

    def click(self, texto, escribir):
        if not escribir:
            if texto == "=" and self.model.operacion != "":
                resultado = self.model.calculate(self.model.operacion)
                self.model.clear()
                self.view.limpiarPantalla()
                self.view.mostrarPantalla(resultado)
            elif texto == u"\u232B":
                self.model.clear()
                self.view.limpiarPantalla()
        else:
            self.model.operacion += str(texto)
            self.view.mostrarPantalla(texto)
