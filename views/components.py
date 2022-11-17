from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QCursor
from PyQt5.QtCore import Qt

#componente que va a mostrar la foto 
class RecipeImg(QLabel):

    def __init__(self, img_path):
        super().__init__()

        #la direccion de la imagen que se requiere mostrar 
        #se le dara un tamano en especifico
        self.img = QPixmap(img_path).scaledToWidth(200)
        self.setPixmap(self.img)


#clase para poder crear botones 
class Button(QPushButton):
    
    def __init__(self, icon, color):
        super().__init__()
        
        self.setMinimumSize(30, 30)
        self.set_cursor()
        self.setIcon(QIcon(f"assets/icons/{icon}.png"))
        self.setStyleSheet(f"border-radius: 15px; background-color: {color};")
    
    def set_cursor(self):
        #cambiar el cursor 
        pointer = QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)