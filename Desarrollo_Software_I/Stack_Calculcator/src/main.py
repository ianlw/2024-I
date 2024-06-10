from tkinter import Tk
from controller.app_controller import AppController
from view.main_window import MainWindow

if __name__ == "__main__":
    controller = AppController()
    root = Tk()
    app = MainWindow(root, controller)
    root.mainloop()
