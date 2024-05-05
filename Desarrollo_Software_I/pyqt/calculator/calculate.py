import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(0, 0, 255, 50);")

        self.layout = QGridLayout()
        self.display = QPushButton("")
        self.display.setFixedSize(200, 50)
        self.display.setStyleSheet("background-color: white;")
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"
        ]

        row = 1
        col = 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("border-radius: 10px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 1);")
            button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))
            self.layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.setLayout(self.layout)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif text == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.setGeometry(100, 100, 400, 600)
    window.show()
    sys.exit(app.exec_())
