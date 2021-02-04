from PyQt5.QtWidgets import QPushButton

class Button:
    def __init__(self, parent):
        self.parent = parent
    
    def mountButton(self, text, ax, ay, aw, ah):
        button = QPushButton(text, self.parent)
        button.setGeometry(ax, ay, aw, ah)
