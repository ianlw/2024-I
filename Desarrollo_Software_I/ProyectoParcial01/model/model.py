class CalculadoraModel:
    def __init__(self):
        self.expression = ""

    def agregar_numero(self, num):
        self.expression += str(num)

    def evaluar_expresion(self):
        try:
            # Evalúa la expresión y maneja las operaciones de potencia correctamente
            result = eval(self.expression.replace("^", "**"))
        except Exception as e:
            result = "Error"
        return result

    def limpiar_expresion(self):
        result = self.expression = ""
        return result

    def borrar_ultimo_caracter(self):
        self.expression = self.expression[:-1]
        return self.expression
