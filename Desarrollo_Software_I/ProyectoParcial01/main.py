from PyQt6.QtWidgets import QApplication
from controller.controller import AppController
from view.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    main_window = MainWindow(controller)
    main_window.show()
    sys.exit(app.exec())
