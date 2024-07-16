from model.rpncalc import RPNcalc
from controller.undo_redo import UndoRedo

class AppController:
    def __init__(self):
        self.rpn = RPNcalc()
        self.undo_redo = UndoRedo()

    # Función que procesa cada operación en una expresión aritmética
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
