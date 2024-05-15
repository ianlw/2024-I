from stack import Stack

def evalPosfija(expresion):
    expresion = expresion.strip()
    posfijo = expresion.split(" ")
    pila = Stack()

    for s in posfijo:
        if s == "+":
            opn2 = pila.pop()
            opn1 = pila.pop()
            pila.push(opn1 + opn2)
        elif s == "-":
            opn2 = pila.pop()
            opn1 = pila.pop()
            pila.push(opn1 - opn2)
        else:
            pila.push(float(s))
    return pila.peek()

# Expresión 1
expresion = "2 5 + 3 - 1 +"
print("\nExpresion:", expresion)
print("Resultado:", evalPosfija(expresion))

# Expresión 2
expresion = "2 5 3 - + 1 +"
print("\nExpresion:", expresion)
print("Resultado:", evalPosfija(expresion))

# Expresión 3
expresion = "2 3 + 5 3 1 - + +"
print("\nExpresion:", expresion)
print("Resultado:", evalPosfija(expresion))

# Expresión 4
expresion = "2 3 + 5 2 1 + - + 4 5 - 2 1 - - -"
print("\nExpresion:", expresion)
print("Resultado:", evalPosfija(expresion))

