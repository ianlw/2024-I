from stack import Stack

def llavesCorchetesParentesisBalanceado(expression):
    opening_brackets = {'(': ')', '{': '}', '[': ']'}
    pila = []

    for c in expression:
        if c in opening_brackets:
            pila.append(c)
        elif c in opening_brackets.values():
            if not pila or opening_brackets[pila.pop()] != c:
                return False

    return not pila

#while(True):
#    expresion = input("Ingrese la expresión: ")
#    print(llavesCorchetesParentesisBalanceado(expresion))