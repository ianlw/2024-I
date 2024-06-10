from stack import Stack
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


if __name__ == "__main__":
#     print("Expresion 1")
#     op = ["(", "1", "+", "2", ")", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO", "REDO", "REDO", "REDO", "REDO", "REDO", "REDO"]
#     simulate(op)
#     
#     
#     print("\nExpresion 2")
#     op = ["(", "28", "/", "7", ")", "-", "12", "*", "14", "UNDO", "UNDO", "UNDO", "UNDO","+", "REDO", "REDO", "10"]
#     simulate(op)
#     
#     
#     print("\nExpresion 3")
#     op = ["{", "(", "10", "-", "5", ")", "+", "10", "*", "14", "UNDO", "UNDO", "}", "REDO", "REDO"]
#     simulate(op)
#     
#     
#     print("\nExpresion 4")
#     op = ["15", "+", "25", "*", "5", ")", "+", "10", "}", "*", "15", "+", "20", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO",
#           "UNDO", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO","UNDO","[", "REDO", "REDO", "{", "(", "REDO", "REDO", 
#           "REDO", "REDO", "REDO", "REDO", "REDO", "REDO", "REDO", "]", "REDO", "REDO"]
#     simulate(op)
#     
#     
    print("\nExpresion 5")
    op = ["2", "^", "(", "2", "/", "7", ")", "UNDO", "UNDO", "UNDO", "*", "4", ")"]
    simulate(op)
