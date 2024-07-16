class SimbolosAgrupacionBalanceados:
    def __init__(self) -> None:
        pass

    # función que verifica una expresión tiene los símbolos de agrupación balanceados
    def simbolos_agrupacion_balanceados(self, expression):
        opening_brackets = {'(': ')', '{': '}', '[': ']'}
        pila = []

        for c in expression:
            if c in opening_brackets:
                pila.append(c)
            elif c in opening_brackets.values():
                if not pila or opening_brackets[pila.pop()] != c:
                    return False

        return not pila

