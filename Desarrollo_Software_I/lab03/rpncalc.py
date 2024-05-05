from stack import Stack 

class RPNcalc:
    def __init__(self):
        # Inicializa una instancia de la clase `Stack` como el atributo `stack`.
        self.stack = Stack() 

    def getOperands(self):
        # Verifica si la pila está vacía.
        if self.stack.isEmpty():
            print("¡Pila vacía! Ingrese un número\n")
            return False, 0, 0 

        # Saca un número de la pila y lo guarda en `n1`.
        n1 = self.stack.pop()
        # Verifica nuevamente si la pila está vacía después de sacar un elemento.
        if self.stack.isEmpty():
            print("Se requieren dos números!\n")
            # Si solo había un número, vuelve a insertarlo en la pila.
            self.stack.push(n1)
            return False, 0, 0 

        # Saca un segundo número de la pila y lo guarda en `n2`.
        n2 = self.stack.pop()
        # Devuelve los dos números como valores flotantes.
        return True, float(n1), float(n2) 

    def enterNumber(self, _n):
        # Inserta un número en la pila.
        self.stack.push(_n) 

    def selectOp_sum(self):
        # Obtiene dos operandos de la pila.
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        # Realiza la suma de `n2` y `n1`, y devuelve el resultado a la pila.
        self.stack.push(n2 + n1) 

    def selectOp_diff(self):
        # Obtiene dos operandos de la pila.
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        # Realiza la resta (`n2` menos `n1`) y devuelve el resultado a la pila.
        self.stack.push(n2 - n1)
    
    # Métodos de funcionalidades adicionales
    # Multiplicación
    def selectOp_mul(self):
        # Obtiene dos operandos de la pila.
        check, n1, n2 = self.getOperands()
        if not check:
            return
        # Realiza la multiplicación de `n2` y `n1` y devuelve el resultado a la pila.
        self.stack.push(n2 * n1)

    # División
    def selectOp_div(self):
        # Obtiene dos operandos de la pila.
        check, n1, n2 = self.getOperands()
        if not check:
            return
        # Realiza la división (`n2` entre `n1`) y devuelve el resultado a la pila.
        self.stack.push(n2 / n1)

    # Potenciación
    def selectOp_pot(self):
        # Obtiene dos operandos de la pila.
        check, n1, n2 = self.getOperands()
        if not check:
            return
        # Realiza la potenciación (`n2` elevado a `n1`) y devuelve el resultado a la pila.
        self.stack.push(n2 ** n1)

    # Raíz
    def selectOp_raiz(self):
        # Obtiene dos operandos de la pila.
        check, n1, n2 = self.getOperands()
        if not check:
            return 
        # Calcula la raíz (`n2` elevado a la inversa de `n1`) y devuelve el resultado a la pila.
        self.stack.push(n2 ** (1 / n1))