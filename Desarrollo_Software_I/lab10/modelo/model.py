class Model:
    def __init__(self):
        self.operacion = ""

    def calculate(self, operacion):
        operacion = operacion.replace(u"\u00F7", "/")
        return str(eval(operacion))

    def clear(self):
        self.operacion = ""
