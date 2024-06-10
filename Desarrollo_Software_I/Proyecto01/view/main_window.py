from tkinter import *
from model.appcontroller import AppController 

def agregar_numero(numero):
    pantalla.insert(END, numero)
    pantalla.xview_moveto(1.0)

def borrar_ultimo_digito():
    contenido_pantalla = pantalla.get()
    if contenido_pantalla:
        nueva_pantalla = contenido_pantalla[:-1]
        pantalla.delete(0, END)
        pantalla.insert(0, nueva_pantalla)

def limpiar_pantallas():
    pantalla.delete(0, END)
    pantallaResultado.config(text="")

def evaluar_expresion():
    expresion = pantalla.get()
    app = AppController()
    resultado = app.loop(expresion)
    pantallaResultado.config(text=str(resultado))
    # return resultado


root = Tk()

root.title("Calculadora básica")

try:
    root.iconphoto(False, PhotoImage(file='./../img/light_calculator.png'))
except Exception as e:
    print(f"Error setting icon: {e}")

pantallasFrame = Frame(root)
pantallasFrame.grid(row=0, column=0, columnspan=5, pady=2)

pantalla = Entry(pantallasFrame, width=22, bg="black", fg="white",
                 borderwidth=0, font=('arial', 18, 'bold'))
pantalla.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

pantallaResultado = Label(pantallasFrame, width=22, bg="black", fg="white",
                          borderwidth=0, font=('arial', 18, 'bold'))
pantallaResultado.grid(row=1, column=0, columnspan=4, padx=2, pady=2)
pantallaResultado.config(text="Resultado")

botonesSAgrupamientoFrame = Frame(root)
botonesSAgrupamientoFrame.grid(row=1, column=0, columnspan=5, pady=2)

botonParentesisIzquierdo = Button(botonesSAgrupamientoFrame, text="(", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("("))
botonParentesisIzquierdo.grid(row=0, column=0, padx=2)

botonParentesisDerecho = Button(botonesSAgrupamientoFrame, text=")", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero(")"))
botonParentesisDerecho.grid(row=0, column=1, padx=2)

botonLlaveIzquierda = Button(botonesSAgrupamientoFrame, text="{", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("{"))
botonLlaveIzquierda.grid(row=0, column=2, padx=2)

botonLlaveDerecha = Button(botonesSAgrupamientoFrame, text="}", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("}"))
botonLlaveDerecha.grid(row=0, column=3, padx=2)

botonCorcheteIzquierdo = Button(botonesSAgrupamientoFrame, text="[", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("["))
botonCorcheteIzquierdo.grid(row=0, column=4, padx=2)

botonCorcheteDerecho = Button(botonesSAgrupamientoFrame, text="]", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("]"))
botonCorcheteDerecho.grid(row=0, column=5, padx=2)

botonesAccionFrame = Frame(root)
botonesAccionFrame.grid(row=2, column=0, columnspan=5, pady=2)

botonUndo = Button(botonesAccionFrame, text="Undo", bg="white", fg="red", padx=28, pady=25, borderwidth=0, command=lambda: agregar_numero("U"))
botonUndo.grid(row=0, column=0, padx=2, pady=2)

botonRedo = Button(botonesAccionFrame, text="Redo", bg="white", fg="red", padx=28, pady=25, borderwidth=0, command=lambda: agregar_numero("R"))
botonRedo.grid(row=0, column=1, padx=2, pady=2)

botonDelete = Button(botonesAccionFrame, text="Delete", bg="white", fg="red", padx=25, pady=25, borderwidth=0, command=borrar_ultimo_digito)
botonDelete.grid(row=0, column=2, padx=2, pady=2)

botonClear = Button(botonesAccionFrame, text="Clear", bg="white", fg="red", padx=28, pady=25, borderwidth=0, command=limpiar_pantallas)
botonClear.grid(row=0, column=3, padx=2, pady=2)

botonesNumerosFrame = Frame(root)
botonesNumerosFrame.grid(row=3, column=0, columnspan=3, pady=2)

boton1 = Button(botonesNumerosFrame, text="1", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("1"))
boton1.grid(row=0, column=0, padx=2, pady=2)

boton2 = Button(botonesNumerosFrame, text="2", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("2"))
boton2.grid(row=0, column=1, padx=2, pady=2)

boton3 = Button(botonesNumerosFrame, text="3", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("3"))
boton3.grid(row=0, column=2, padx=2, pady=2)

boton4 = Button(botonesNumerosFrame, text="4", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("4"))
boton4.grid(row=1, column=0, padx=2, pady=2)

boton5 = Button(botonesNumerosFrame, text="5", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("5"))
boton5.grid(row=1, column=1, padx=2, pady=2)

boton6 = Button(botonesNumerosFrame, text="6", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("6"))
boton6.grid(row=1, column=2, padx=2, pady=2)

boton7 = Button(botonesNumerosFrame, text="7", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("7"))
boton7.grid(row=2, column=0, padx=2, pady=2)

boton8 = Button(botonesNumerosFrame, text="8", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("8"))
boton8.grid(row=2, column=1, padx=2, pady=2)

boton9 = Button(botonesNumerosFrame, text="9", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("9"))
boton9.grid(row=2, column=2, padx=2, pady=2)

botonIgual = Button(botonesNumerosFrame, text="=", bg="red", fg="white", padx=40, pady=25, borderwidth=0, command=lambda: evaluar_expresion)
botonIgual.grid(row=3, column=0, padx=2, pady=2)

boton0 = Button(botonesNumerosFrame, text="0", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("0"))
boton0.grid(row=3, column=1, padx=2, pady=2)

botonPunto = Button(botonesNumerosFrame, text=".", bg="#A9FF53", fg="black", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("."))
botonPunto.grid(row=3, column=2, padx=2, pady=2)

operacionesFrame = Frame(root)
operacionesFrame.grid(row=3, column=4, columnspan=5, pady=2)

botonMas = Button(operacionesFrame, text="+", bg="#32C8FF", fg="black", padx=40, pady=17, borderwidth=0, command=lambda: agregar_numero("+"))
botonMas.grid(row=1, column=0, padx=2, pady=2)

botonMenos = Button(operacionesFrame, text="-", bg="#32C8FF", fg="black", padx=40, pady=17, borderwidth=0, command=lambda: agregar_numero("-"))
botonMenos.grid(row=2, column=0, padx=2, pady=2)

botonMul = Button(operacionesFrame, text="*", bg="#32C8FF", fg="black", padx=40, pady=17, borderwidth=0, command=lambda: agregar_numero("*"))
botonMul.grid(row=3, column=0, padx=2, pady=2)

botonDiv = Button(operacionesFrame, text="/", bg="#32C8FF", fg="black", padx=40, pady=17, borderwidth=0, command=lambda: agregar_numero("/"))
botonDiv.grid(row=4, column=0, padx=2, pady=2)

botonPotencia = Button(operacionesFrame, text="^", bg="#32C8FF", fg="black", padx=40, pady=17, borderwidth=0, command=lambda: agregar_numero("^"))
botonPotencia.grid(row=5, column=0, padx=2, pady=2)

root.mainloop()
