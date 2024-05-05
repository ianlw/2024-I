import re
class Stack:
    def __init__(self):
        self.elem = []

    def push(self, _n):
        self.elem.append(_n)

    def pop(self):
        return self.elem.pop() if not self.isEmpty() else None

    def peek(self):
        return self.elem[-1] if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.elem) == 0

    def dump(self):
        return '\n'.join(map(str, self.elem))


def valPreced(s):
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

def parentesisAbierto(s):
    if s == ")":
        return "("
    elif s == "]":
        return "["
    elif s == "}":
        return "{"
    else:
        return ""


def InfijaAPostEija(expresion):
    pila = Stack()

    infijo = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\[\]\{\}\^\+\*\-\/])", expresion)
    # infijo = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", expresion)
    print(infijo)
    salida = ""

    for s in infijo:
        if s in ["+", "-", "*", "/", "^"]:
            while (not pila.isEmpty() and valPreced(s) <= valPreced(pila.peek())):
                salida += pila.pop() + " "
            pila.push(s)
        elif s in ["(", "[", "{"]:
            pila.push(s)
        elif s in [")", "]", "}"]:
            while not pila.isEmpty() and pila.peek() != parentesisAbierto(s):
                salida += pila.pop() + " "
            if not pila.isEmpty() and pila.peek() == parentesisAbierto(s):
                pila.pop()
        else:
            salida += s + " "

    while not pila.isEmpty():
        salida += pila.pop() + " "

    return salida


print("Expresiones infijas a posfijas")
# print(InfijaAPostEija("45000/{12*(23+3)^2}"))
# print(InfijaAPostEija("2 ^ (3 + 4)"))
# print(InfijaAPostEija("2 + 3 * 4)"))
print(InfijaAPostEija("[{2*(1+3)^2}+{(1+2)*3}]"))
print(InfijaAPostEija("[{2*(1+3)^2}+{(1+2)*3}]"))
