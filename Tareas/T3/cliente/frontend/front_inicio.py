from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import os
import sys

class WaitingRoom(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(200, 200, 600, 750)
        self.setFixedSize(600, 750)
        self.setWindowTitle('Sala de espera')
        self.setFixedSize(600, 750)
        
        #foto de background
        self.label_background = QLabel(self)
        self.label_background.setGeometry(0, 0, 600, 600)
        pixeles = QPixmap(os.path.join("Sprites", "background", "background_inicio"))
        self.label_background.setPixmap(pixeles)
        self.label_background.setMaximumSize(1000, 1000)
        self.label_background.setScaledContents(True)


        self.show()

if __name__ == '__main__':
    app = QApplication([])
    gabo = WaitingRoom()
    sys.exit(app.exec())
        