from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import re

class MainWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora MVC")
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setFont(QFont("Cascadia Code", 10))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input_output_frame = QGridLayout()
        layout.addLayout(self.input_output_frame)

        self.input = QLineEdit(self)
        self.input.setStyleSheet("background-color: #000000; color: white; border: none; font-family: 'Cartograph CF'; font-size: 14pt;")
        self.input_output_frame.addWidget(self.input, 0, 0, 1, 4)

        self.output = QLabel("Resultado", self)
        self.output.setStyleSheet("background-color: #000000; color: white; border: none; font-family: 'Cartograph CF'; font-size: 14pt;")
        self.input_output_frame.addWidget(self.output, 1, 0, 1, 4)

        self.create_buttons()
        self.input.textChanged.connect(self.validate_expression)
        self.input.setFocus()
        self.input.returnPressed.connect(self.calculate)

    def create_buttons(self):
        button_style = "padding: 15px; font-size: 10pt; border-radius: 10px;"

        buttons = [
            ("(", 0, 0, "#EFBC9B"), (")", 0, 1, "#EFBC9B"), ("{", 0, 2, "#EFBC9B"), ("}", 0, 3, "#EFBC9B"), ("[", 0, 4, "#EFBC9B"), ("]", 0, 5, "#EFBC9B"),
            ("Undo", 1, 0, "#FBF3D5"), ("Redo", 1, 1, "#FBF3D5"), ("Delete", 1, 2, "#FBF3D5"), ("Clear", 1, 3, "#FBF3D5"),
            ("1", 2, 0, "#D6EFC7"), ("2", 2, 1, "#D6EFC7"), ("3", 2, 2, "#D6EFC7"), ("+", 2, 3, "#F8D4D8"),
            ("4", 3, 0, "#D6EFC7"), ("5", 3, 1, "#D6EFC7"), ("6", 3, 2, "#D6EFC7"), ("-", 3, 3, "#F8D4D8"),
            ("7", 4, 0, "#D6EFC7"), ("8", 4, 1, "#D6EFC7"), ("9", 4, 2, "#D6EFC7"), ("*", 4, 3, "#F8D4D8"),
            (".", 5, 0, "#D6EFC7"), ("0", 5, 1, "#D6EFC7"), ("^", 5, 2, "#D6EFC7"), ("/", 5, 3, "#F8D4D8"),
            ("=", 6, 0, "#C8E3D4", 4)
        ]

        for btn_text, row, col, color, colspan in buttons:
            btn = QPushButton(btn_text, self)
            btn.setStyleSheet(f"background-color: {color}; {button_style}")
            self.input_output_frame.addWidget(btn, row, col, 1, colspan if colspan else 1)
            btn.clicked.connect(self.button_clicked)

    def validate_expression(self):
        expression = self.input.text()
        valid = re.match(r'^[\d\.\+\-\*/\^\(\)\[\]\{\} ]*$', expression) is not None
        if not valid:
            self.input.setText(re.sub(r'[^\d\.\+\-\*/\^\(\)\[\]\{\} ]', '', expression))

    def button_clicked(self):
        btn = self.sender()
        text = btn.text()
        
        if text == "=":
            self.calculate()
        elif text == "Clear":
            self.input.clear()
        elif text == "Undo":
            self.controller.undo()
            self.input.setText(self.controller.get_current_expression())
        elif text == "Redo":
            self.controller.redo()
            self.input.setText(self.controller.get_current_expression())
        elif text == "Delete":
            self.controller.delete()
            self.input.setText(self.controller.get_current_expression())
        else:
            current_text = self.input.text()
            self.input.setText(current_text + text)
            self.controller.add_to_undo_redo(text)

    def calculate(self):
        expression = self.input.text()
        if not self.controller.simbolos_agrupacion_balanceado(expression):
            self.output.setText("Error: Símbolos de agrupación no balanceados.")
            return

        posfijo = self.controller.infijo_to_posfijo(expression)
        result = self.controller.process_expression(posfijo)
        if result is not None:
            self.output.setText(str(result))
        else:
            self.output.setText("Error en la expresión.")
