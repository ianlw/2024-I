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
    else:
        return "{"

def infijo_a_posfijo(expresion):
    stack_operadores = Stack()
    resultado = []
    num_actual = []

    for caracter in expresion:
        if caracter.isdigit():
            num_actual.append(caracter)
        elif num_actual:
            resultado.extend(num_actual)
            resultado.append(' ')
            num_actual = []

        if caracter in "+-*/^":
            resultado.append(caracter)
            resultado.append(' ')  # Agregar un espacio después de cada operando u operador
        elif caracter in "([{":
            stack_operadores.push(caracter)
        elif caracter in ")]}":
            while not stack_operadores.isEmpty() and stack_operadores.peek() != parentesisAbierto(caracter):
                resultado.append(stack_operadores.pop())
                resultado.append(' ')  # Agregar un espacio después de cada operador
            stack_operadores.pop()

    if num_actual:
        resultado.extend(num_actual)
        resultado.append(' ')

    while not stack_operadores.isEmpty():
        resultado.append(stack_operadores.pop())
        resultado.append(' ')  # Agregar un espacio después de cada operador

    return ''.join(resultado)

expresion_infija = "[45000/{12*(23+3)^2}]"
expresion_posfija = infijo_a_posfijo(expresion_infija)
print("Expresión posfija:", expresion_posfija)
