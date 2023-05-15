import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)



class Luigi(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label  = QLabel()
        self.setGeometry(100,100, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = Luigi()
    sys.exit(app.exec())