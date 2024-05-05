import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setGeometry(100, 100, 300, 300)
        self.setupUI()

    def setupUI(self):
        self.layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        self.buttons = {}
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            button.clicked.connect(self.buttonClicked)
            self.buttons[text] = button
            self.layout.addWidget(button, row, col, 1, 1)  # Agregar 1, 1 para establecer el tamaño del widget en la cuadrícula

        self.layout.addWidget(self.display)
        self.setLayout(self.layout)

    def buttonClicked(self):
        button = self.sender()
        if button:
            if button.text() == '=':
                try:
                    result = eval(self.display.text())
                    self.display.setText(str(result))
                except Exception as e:
                    self.display.setText('Error')
            else:
                self.display.setText(self.display.text() + button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
