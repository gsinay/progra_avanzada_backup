from PyQt5.QtCore import pyqtSignal, QObject
from parametros import (MIN_CARACTERES, MAX_CARACTERES)

class Procesador(QObject):
    senal_username_verificado = pyqtSignal(str)
    senal_username_malo = pyqtSignal(str)
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
    
    def verificar_username(self, username):
        if len(username) < MIN_CARACTERES:
            self.senal_username_malo.emit(f"username menor a {MIN_CARACTERES} caracteres")
        elif len(username) > MAX_CARACTERES:
            self.senal_username_malo.emit(f"username mayor a {MAX_CARACTERES} caracteres")
        elif username == "":
            self.senal_username_malo.emit("username vacío")
        elif not username.isalnum():
            self.senal_username_malo.emit("username no alfanumérico")
        else:
            self.senal_username_verificado.emit(username)

        
        
    
