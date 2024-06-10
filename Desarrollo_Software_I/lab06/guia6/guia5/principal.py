from stack import Stack
from verificarParentesis import llavesCorchetesParentesisBalanceado
from InfijoaPosfijo import InfijaAPostEija
from evaluarExpresion import evalPosfija
while(True):
    expresion = input("\nIngrese su expresión: ")

    #print(llavesCorchetesParentesisBalanceado(expresion))
    if(llavesCorchetesParentesisBalanceado(expresion)):
        posfija = InfijaAPostEija(expresion)
        print(posfija)
        resultado = evalPosfija(posfija)
        print(resultado)
    else:
        print("La expresión es incorrecta (parentesis desbalanceados)")
        
       