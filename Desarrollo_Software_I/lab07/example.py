
from tkinter import *
root = Tk()
boton1 = Button(root, text=" Botón 1", bg="red", padx=100, pady=25, state=DISABLED).grid(row=1, column=0)
boton2 = Button(root, text=" Botón 2", bg="white", padx=100, pady=25, state=DISABLED).grid(row=1, column=1)
boton3 = Button(root, text=" Botón 3", bg="green", padx=100, pady=25, state=DISABLED).grid(row=1, column=2)
boton4 = Button(root, text=" Botón 4", bg="black", padx=100, pady=25, state=DISABLED).grid(row=2, column=0)
boton5 = Button(root, text=" Botón 5", bg="blue", padx=100, pady=25, state=DISABLED).grid(row=2, column=1)
boton6 = Button(root, text=" Botón 6", bg="yellow", padx=100, pady=25, state=DISABLED).grid(row=2, column=2)
boton7 = Button(root, text=" Botón 7", bg="cyan", padx=100, pady=25, state=DISABLED).grid(row=3, column=0)
boton8 = Button(root, text=" Botón 8", bg="magenta", padx=100, pady=25, state=DISABLED).grid(row=3, column=1)
boton9 = Button(root, text=" Botón 9", bg="purple", padx=100, pady=25, state=DISABLED).grid(row=3, column=2)

root.mainloop()
