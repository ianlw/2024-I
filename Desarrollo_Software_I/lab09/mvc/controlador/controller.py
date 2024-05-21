from modelo.model import Model
from vista.view import View

class Controller:
    def __init__(self, window):
        self.window = window
        self.model = Model()
        self.view = View(window, self)

    def add_item(self):
        item = self.view.item_entry.get()
        if item:
            self.model.add_item(item)
            self.view.update_list(self.model.get_items())
            self.view.clear_entry()


