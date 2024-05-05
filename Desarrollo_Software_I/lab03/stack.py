class Stack:
    def __init__(self):
        # Inicializa una lista vacía que se usará para almacenar los elementos de la pila.
        self.elem = []

    def push(self, _n):
        # Comprueba si el elemento es de tipo entero o flotante.
        if isinstance(_n, (int, float)):
            # Inserta el elemento `_n` al principio de la lista `elem`.
            self.elem.insert(0, _n)

    def pop(self):
        # Elimina y devuelve el primer elemento de la lista `elem` si no está vacía.
        # Si la lista `elem` está vacía, devuelve `None`.
        return self.elem.pop() if not self.isEmpty() else None
        # return self.elem.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        # Devuelve `True` si la lista `elem` está vacía, de lo contrario devuelve `False`.
        return len(self.elem) == 0

    def dump(self):
        # Inicializa una cadena de texto vacía para almacenar los elementos de la pila.
        text = ""
        # Itera sobre los elementos de la lista `elem` y los concatena a la cadena `text`.
        for item in self.elem:
            text += f"{item}\n"
        # Devuelve la cadena `text` que contiene los elementos de la pila, separados por saltos de línea.
        return text
