from stack import Stack 

class RPNcalc:
    def __init__(self):
        self.stack = Stack() 

    def getOperands(self):
        if self.stack.isEmpty():
            print("Pila vacia! Ingrese un numero\n")
            return False, 0, 0 

        n1 = self.stack.pop()
        if self.stack.isEmpty():
            print("Se requiere dos numeros!\n")
            self.stack.push(n1)
            return False, 0, 0 

        n2 = self.stack.pop()
        #return True, int(n1), int(n2) 
        return True, float(n1), float(n2) 

    def enterNumber(self, _n):
        self.stack.push(_n) 

    def selectOp_sum(self):
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        self.stack.push(n2 + n1) 

    def selectOp_diff(self):
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        self.stack.push(n2 - n1)
# Operaciones añadidas
    def selectOp_mul(self):
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        self.stack.push(n2 * n1)

    def selectOp_div(self):
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        self.stack.push(n2 / n1)

    def selectOp_pot(self):
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        self.stack.push(n2 ** n1)
