
from stack import Stack
from verificarParentesis import llavesCorchetesParentesisBalanceado
from InfijoaPosfijo import InfijaAPostEija
from evaluarExpresion import evalPosfija
while(True):
    expresion = input("\nIngrese su expresión: ")

    #print(llavesCorchetesParentesisBalanceado(expresion))
    if(llavesCorchetesParentesisBalanceado(expresion)):
        print("Balanceo de paréntesis correcto")
        posfija = InfijaAPostEija(expresion)
        print("Expresión posfija: ", posfija)
        resultado = evalPosfija(posfija)
        print("Resultado: ", resultado)
    else:
        print("La expresión es incorrecta (parentesis desbalanceados)")
