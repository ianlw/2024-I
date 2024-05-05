class Stack:
    def __init__(self):
        self.elem = []

    def push(self, _n):
        #if isinstance(_n, int):
        if isinstance(_n, (int, float)):
            self.elem.insert(0, _n)

    def pop(self):
        return self.elem.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.elem) == 0

    def dump(self):
        text = ""
        for item in self.elem:
            text += f"{item}\n"
        return text
