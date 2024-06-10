class Stack:
    def __init__(self):
        self.elem = []

    def push(self, _n):
        self.elem.append(_n)

    def pop(self):
        return self.elem.pop() if not self.isEmpty() else None

    def peek(self):
        return self.elem[-1] if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.elem) == 0

    def dump(self):
        return '\n'.join(map(str, self.elem))
    def size(self):
        return len(self.elem)