from model.rpncalc import RPNcalc

from model.stack import Stack 
from controller.undo_redo import UndoRedo
# from undo_redo import UndoRedo
import re
class AppController:
    def __init__(self):
        self.rpn = RPNcalc()
        self.undo_redo = UndoRedo()

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

    def parentesisAbierto(self, s):
        if s == ")":
            return "("
        elif s == "]":
            return "["
        elif s == "}":
            return "{"
        else:
            return ""


    def infijo_to_posfijo(self, expression):
        pila = Stack()

        infijo = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\[\]\{\}\^\+\*\-\/])", expression)
        # infijo = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", expresion)
        print(infijo)
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

    def simbolos_agrupacion_balanceado(self, expression):
        opening_brackets = {'(': ')', '{': '}', '[': ']'}
        pila = []

        for c in expression:
            if c in opening_brackets:
                pila.append(c)
            elif c in opening_brackets.values():
                if not pila or opening_brackets[pila.pop()] != c:
                    return False

        return not pila

    def process_expression(self, expression):
        for char in expression.split():
            try:
                n = float(char)
                self.rpn.enterNumber(n)
            except ValueError:
                if char == '+':
                    self.rpn.selectOp_sum()
                elif char == '-':
                    self.rpn.selectOp_diff()
                elif char == '*':
                    self.rpn.selectOp_mul()
                elif char == '/':
                    self.rpn.selectOp_div()
                elif char == '^':
                    self.rpn.selectOp_pot()
                else:
                    print("Error: Carácter no reconocido en la expresión.")
                    return None
        return self.rpn.stack.peek() if not self.rpn.stack.isEmpty() else None

    # def undo(self):
    #     return self.undo_redo.undo()
    #
    # def redo(self):
    #     return self.undo_redo.redo()
    def add_to_undo_redo(self, char):
        self.undo_redo.input_char(char)


    def undo_one_element(self):
        return self.undo_redo.undo_one_element()

    def delete(self):
        if not self.input_expression:
            return False
        deleted_char = self.input_expression[-1]
        self.input_expression = self.input_expression[:-1]
        self.undo_redo.input_char(deleted_char)
        return True

    def get_current_expression(self):
        return self.input_expression
