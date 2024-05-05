class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0






def parentesisBalanceado(expression):
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')' and stack.pop() != '(':
            return False

    return stack.isEmpty()


while(True):
    expresion = input("Ingrese la expresión: ")
    print(parentesisBalanceado(expresion))

