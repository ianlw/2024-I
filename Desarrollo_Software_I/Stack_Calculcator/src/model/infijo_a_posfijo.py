from model.stack import Stack 
import re

class InfijoAPosfijo:
    def __init__(self) -> None:
        pass

    # Función que devuelve la precedencia de cada operación
    def valPreced(self, s):
        if s == "^":
            return 4
        elif s == "*" or s == "/":
            return 3
        elif s == "+" or s == "-":
            return 2
        elif s == "(":
            return 1
        else:
            return 0

    # Función que devuelve la cerradura de cada símbolo de agrupamiento
    def parentesisAbierto(self, s):
        if s == ")":
            return "("
        elif s == "]":
            return "["
        elif s == "}":
            return "{"
        else:
            return ""

    # Función que transforma una expresion infija a posfija
    def infijo_to_posfijo(self, expression):
        pila = Stack()

        infijo = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\[\]\{\}\^\+\*\-\/])", expression)
        salida = ""

        for s in infijo:
            if s in ["+", "-", "*", "/", "^"]:
                while (not pila.isEmpty() and self.valPreced(s) <= self.valPreced(pila.peek())):
                    salida += pila.pop() + " "
                pila.push(s)
            elif s in ["(", "[", "{"]:
                pila.push(s)
            elif s in [")", "]", "}"]:
                while not pila.isEmpty() and pila.peek() != self.parentesisAbierto(s):
                    salida += pila.pop() + " "
                if not pila.isEmpty() and pila.peek() == self.parentesisAbierto(s):
                    pila.pop()
            else:
                salida += s + " "

        while not pila.isEmpty():
            salida += pila.pop() + " "

        return salida

