from model.stack import Stack
class UndoRedo:
    def __init__(self):
        self.Undo = Stack()
        self.Redo = Stack()

    def input_char(self, c):
        self.Undo.push(c)

    def undo(self):
        if not self.Undo.isEmpty():
            X = self.Undo.pop()
            self.Redo.push(X)
            return True
        else:
            print("undo: (pila Undo vacía)")
            return False

    def redo(self):
        if not self.Redo.isEmpty():
            X = self.Redo.pop()
            self.Undo.push(X)
            return True
        else:
            print("redo: (pila Redo vacía)")
            return False

    def clear(self):
        self.Undo = Stack()
        self.Redo = Stack()

    def show(self):
        values = ""
        for item in self.Undo.elem:
            values += item
        return values


def simulate(op):
    undo_redo = UndoRedo()
    for operation in op:
        if operation == "UNDO":
            if undo_redo.undo():
                print("undo:", undo_redo.show())
        elif operation == "REDO":
            if undo_redo.redo():
                print("redo:", undo_redo.show())
        else:
            undo_redo.input_char(operation.strip())
            print("inserta:", undo_redo.show())


