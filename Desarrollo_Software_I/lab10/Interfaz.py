from tkinter import Tk, Text, Button, END
import re

class Interfaz:
    def __init__(self, ventana) -> None:
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.pantalla = Text(ventana, state='disabled', width=40, height=3, background='white', foreground='blue', font=('Helvetica', 15))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.operacion = ""
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
        # Se crea un boton con los atributos por defecto previamente establecidos a consideración de los requerimientos del programa. Se usa el comando "click" como comportamiento para todos los botones, donde se asigna 
        # El atributo escribir sirve para indicar si el boton desencadenará un evento de escritura
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=('Helvetica',15), command=lambda:self.click(valor, escribir))
    
    def click(self,texto,escribir):
        # Si el boton sirve para escribir, o esa es la funcionalidad que se pretende que tenga
        if not escribir:
            # Si el boton es el de igual o uno sin ningún texto entonces se procede a evaluar la operación
            if texto == "=" and self.operacion!="":
                # Reemplaza el símbolo de división ÷ con un /
                self.operacion = re.sub(u"\u00F7", "/", self.operacion)
                # Evalúa la operacion                
                resultado = str(eval(self.operacion))
                # Se vacía el campo de escritura
                self.operacion = ""
                self.limpiarPantalla()
                # Se muestra el resultado en pantalla
                self.mostrarPantalla(resultado)
            elif texto == u"\u232B":
                # Se borra todo el campo de escritura
                self.operacion = ""
                # Se limpia la pantalla
                self.limpiarPantalla()

        else:
            # Si se escribe cualquier número este solo se añade al final de lo que ya está escrito
            self.operacion += str(texto)
            # Se muestra el campo actualizado en pantalla
            self.mostrarPantalla(texto)
        return
    
    def limpiarPantalla(self):
        # El texto puede ser editado después
        self.pantalla.configure(state="normal")
        # Borra el texto de todo el recuadro de inserción
        self.pantalla.delete("1.0", END)
        # Poner el cuadro de texto para que no pueda ser editado de nuevo
        self.pantalla.configure(state="disabled")
        return
    
    def mostrarPantalla(self, valor):
        self.pantalla.configure(state="normal")
        # Insertar texto al final del recuadro
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return 
    
ventanaPrincipal = Tk()
calculadora = Interfaz(ventanaPrincipal)
ventanaPrincipal.mainloop()


