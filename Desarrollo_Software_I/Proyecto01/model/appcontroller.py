from rpncalc import RPNcalc
from posfijo import InfijaAPostEija

class AppController:
    def __init__(self):
        self.rpn = RPNcalc()

    def process_expression(self, expression):
        # print("WAWA")
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
                    return
            # print("--------------- \n" + self.rpn.stack.dump() + "---------------\n")
        print(self.rpn.stack.dump())

    def loop(self, expresion):
        # while True:
            # print("Ingrese la expresión posfija o 'q' para salir: \n")
        # expression = InfijaAPostEija("[{2*(1+3)^2}+{(1+2)*3}]")
        # if expression == 'q':
            # break
        self.process_expression(expresion)

# if __name__ == '__main__':
    # ctrl = AppController()
    # ctrl.loop()
