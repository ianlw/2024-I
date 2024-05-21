from tkinter import *

def muestra_ventana():
    pass

def agregar_numero(numero):
    pantalla.insert(END, numero)

root = Tk()

root.title("Calculadora básica")

try:
    root.iconphoto(False, PhotoImage(file='./img/calculator.png'))
except Exception as e:
    print(f"Error setting icon: {e}")

pantalla = Entry(root, width=22, bg="black", fg="white",
                 borderwidth=0, font=('arial', 18, 'bold'))
pantalla.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

pantalla = Entry(root, width=22, bg="black", fg="white",
                 borderwidth=0, font=('arial', 18, 'bold'))
pantalla.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

# Pantalla de resultados no editable por el usuario
resultado = Label(root, width=22, bg="gray", fg="white",
                  borderwidth=0, font=('arial', 18, 'bold'))
resultado.grid(row=1, column=0, columnspan=4, padx=2, pady=2)
resultado.config(state='disabled')

# Agregar un marco para los botones
boton_frame = Frame(root)
boton_frame.grid(row=1, column=0, columnspan=5, pady=2)

# Crear y colocar los botones en el marco
botonParentesisIzquierdo = Button(boton_frame, text="(", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("("))
botonParentesisIzquierdo.grid(row=0, column=0, padx=2)

botonParentesisDerecho = Button(boton_frame, text=")", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero(")"))
botonParentesisDerecho.grid(row=0, column=1, padx=2)

botonLlaveIzquierda = Button(boton_frame, text="{", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("{"))
botonLlaveIzquierda.grid(row=0, column=2, padx=2)

botonLlaveDerecha = Button(boton_frame, text="}", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("}"))
botonLlaveDerecha.grid(row=0, column=3, padx=2)

botonCorcheteIzquierdo = Button(boton_frame, text="[", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("["))
botonCorcheteIzquierdo.grid(row=0, column=4, padx=2)

botonCorcheteIzquierdo = Button(boton_frame, text="[", bg="white", fg="red", padx=25, pady=15, borderwidth=0, command=lambda: agregar_numero("["))
botonCorcheteIzquierdo.grid(row=0, column=5, padx=2)


botonUndo = Button(root, text="Undo", bg="white", fg="red", padx=28, pady=25, borderwidth=0, command=lambda: agregar_numero("1"))
botonUndo.grid(row=3, column=0, padx=2, pady=2)

botonRedo = Button(root, text="Redo", bg="white", fg="red", padx=28, pady=25, borderwidth=0, command=lambda: agregar_numero("1"))
botonRedo.grid(row=3, column=1, padx=2, pady=2)

botonDelete = Button(root, text="Delete", bg="white", fg="red", padx=25, pady=25, borderwidth=0, command=lambda: agregar_numero("1"))
botonDelete.grid(row=3, column=2, padx=2, pady=2)

botonClear = Button(root, text="Clear", bg="white", fg="red", padx=28, pady=25, borderwidth=0, command=lambda: agregar_numero("1"))
botonClear.grid(row=3, column=3, padx=2, pady=2)

boton1 = Button(root, text="1", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("1"))
boton1.grid(row=4, column=0, padx=2, pady=2)

boton2 = Button(root, text="2", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("2"))
boton2.grid(row=4, column=1, padx=2, pady=2)

boton3 = Button(root, text="3", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("3"))
boton3.grid(row=4, column=2, padx=2, pady=2)

boton4 = Button(root, text="4", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("4"))
boton4.grid(row=5, column=0, padx=2, pady=2)

boton5 = Button(root, text="5", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("5"))
boton5.grid(row=5, column=1, padx=2, pady=2)

boton6 = Button(root, text="6", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("6"))
boton6.grid(row=5, column=2, padx=2, pady=2)

boton7 = Button(root, text="7", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("7"))
boton7.grid(row=6, column=0, padx=2, pady=2)

boton8 = Button(root, text="8", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("8"))
boton8.grid(row=6, column=1, padx=2, pady=2)

boton9 = Button(root, text="9", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("9"))
boton9.grid(row=6, column=2, padx=2, pady=2)

# Boton Igual
botonIgual = Button(root, text="=", bg="red", fg="white", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("="))
botonIgual.grid(row=7, column=0, padx=2, pady=2)
#Boton Cero
boton0 = Button(root, text="0", bg="white", fg="red", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("0"))
boton0.grid(row=7, column=1, padx=2, pady=2)
#Boton .
botonPunto = Button(root, text=".", bg="#A9FF53", fg="black", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("."))
botonPunto.grid(row=7, column=2, padx=2, pady=2)
#Botones de operacion
botonMas = Button(root, text="+", bg="#32C8FF", fg="black", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("+"))
botonMas.grid(row=4, column=3, padx=2, pady=2)

botonMenos = Button(root, text="-", bg="#32C8FF", fg="black", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("-"))
botonMenos.grid(row=5, column=3, padx=2, pady=2)

botonMul = Button(root, text="*", bg="#32C8FF", fg="black", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("*"))
botonMul.grid(row=6, column=3, padx=2, pady=2)

botonDiv = Button(root, text="/", bg="#32C8FF", fg="black", padx=40, pady=25, borderwidth=0, command=lambda: agregar_numero("/"))
botonDiv.grid(row=7, column=3, padx=2, pady=2)
root.mainloop()
