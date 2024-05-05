from rpncalc import RPNcalc

class AppController:
    def __init__(self):
        # Inicializa una instancia de la clase `RPNcalc` como el atributo `rpn`.
        self.rpn = RPNcalc()

    def loop(self):
        while True:
            # Solicita al usuario que ingrese un número o un operador.
            print("Ingrese un número o un operador ('q' para salir): \n")
            string = input()

            # Intenta convertir la entrada del usuario en un número entero.
            try:
                n = int(string)
                # Si la conversión tiene éxito, inserta el número en la calculadora.
                self.rpn.enterNumber(n)
            except ValueError:
                # Si la entrada no es un número, verifica si es una cadena especial.
                if string == 'q':
                    # Si el usuario ingresa 'q', sale del bucle y finaliza el programa.
                    break
                # Verifica si la entrada es un operador válido y realiza la operación correspondiente.
                elif string == '+':
                    self.rpn.selectOp_sum()
                elif string == '-':
                    self.rpn.selectOp_diff()

                # Funcionalidades adicionales:
                # Multiplicación
                elif string == '*':
                    self.rpn.selectOp_mul()
                # División
                elif string == '/':
                    self.rpn.selectOp_div()
                # Potencia
                elif string == '^':
                    self.rpn.selectOp_pot()
                # Raíz
                elif string == 'raiz':
                    self.rpn.selectOp_raiz()
                else:
                    # Si la entrada no es un operador válido, muestra un mensaje de error.
                    print("Error: Ingrese un operador válido!\n")

            # Imprime el estado actual de la pila de la calculadora.
            print("--------------- \n" + self.rpn.stack.dump() + "---------------\n")
