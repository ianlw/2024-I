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
        elif s == "*":
            opn2 = pila.pop()
            opn1 = pila.pop()
            pila.push(opn1 * opn2)
        elif s == "/":
            opn2 = pila.pop()
            opn1 = pila.pop()
            pila.push(opn1 / opn2)
        elif s == "^":
            opn2 = pila.pop()
            opn1 = pila.pop()
            pila.push(opn1 ** opn2)
        else:
            pila.push(float(s))
    
    return pila.peek()

# Ejemplo de uso:
# expresion = "5 3 +"
# print("Expresion:", expresion)
# print("Resultado:", evalPosfija(expresion))
#
# expresion = "10 4 - 3 * 8 /"
# print("\nExpresion:", expresion)
# print("Resultado:", evalPosfija(expresion))
#
# expresion = "6 2 * 7 + 3 / 4 -"
# print("\nExpresion:", expresion)
# print("Resultado:", evalPosfija(expresion))
#
# expresion = "9 3 / 2 * 4 5 + *"
# print("\nExpresion:", expresion)
# print("Resultado:", evalPosfija(expresion))
#
# expresion = "2 4 ^ 3 2 ^ + 6 -"
# print("\nExpresion:", expresion)
#
# print("Resultado:", evalPosfija(expresion))
