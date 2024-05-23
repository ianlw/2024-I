
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  

    def clear(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def get_items(self):
        return self.items
