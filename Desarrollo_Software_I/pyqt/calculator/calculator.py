from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        resultados = QLineEdit()

        botones = ["7", "8", "9", "/",
                   "4", "5", "6", "*",
                   "1", "2", "3", "-",
                   "0", ".", "=", "+"]

        grid.addWidget(resultados, 0, 0, 1, 4)

        fila = 1
        columna = 0

        for boton in botones:
            if columna > 3:
                columna = 0
                fila += 1

            btn = QPushButton(boton)
            if boton == "=":
                btn.clicked.connect(lambda: self.evaluar(resultados))
                grid.addWidget(btn, fila, columna, 1, 2)
                columna += 1
            else:
                btn.clicked.connect(lambda btn=btn: resultados.setText(resultados.text() + btn.text()))
                grid.addWidget(btn, fila, columna, 1, 1)

            columna += 1

        self.setLayout(grid)
        self.setWindowTitle('Calculadora')
        self.show()

    def evaluar(self, resultados):
        try:
            resultados.setText(str(eval(resultados.text())))
        except Exception:
            resultados.setText("Error")

if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora()
    app.exec_()
