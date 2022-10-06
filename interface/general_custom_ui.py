#remover marcos de las ventanas


from PySide6.QtCore import Qt


from PySide6.QtWidgets import QGraphicsDropShadowEffect
from database.usuario import DBUsuario 
from database.pieza import DBPieza 
from database.maquina import DBMaquina 


#recibe el objeto de la clase que tiene esas caracteristicas
class GeneralCustomUi():
    def __init__(self, ui):
        self.ui = ui

        self.remove_defult_title_bar()
        
        self.ui.top_bar_frame.mouseMoveEvent = self.move_window

        self.set_window_shadow()

        self.set_title_bar_buttons_actions()
    
    #MAXIMIZAR VENTANA
    def maximize_window(self):
        self.ui.showMaximized()
        self.ui.maximize_button.setVisible(False)
        self.ui.shadow_layout.setContentsMargins(0, 0, 0, 0)
    
    #RESTAURAR VENTANA
    def restore_window(self):
        self.ui.showNormal()
        self.ui.maximize_button.setVisible(True)
        self.ui.shadow_layout.setContentsMargins(10, 10, 10, 10)
    

    def set_title_bar_buttons_actions(self):
        self.ui.close_button.clicked.connect(self.ui.close)
        self.ui.minimize_button.clicked.connect(self.ui.showMinimized)
        self.ui.maximize_button.clicked.connect(self.maximize_window)
        self.ui.restore_button.clicked.connect(self.restore_window)

    def remove_defult_title_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
    
    def mouse_press_event(self, event):
        self.drag_pos = event.globalPos()
    
    def move_window(self, event):
        #SI SE PRECIONA BOTON IZQUIERDO DEL MOUSE
        if event.buttons() == Qt.LeftButton:
            #MOVER VENTANA
            #SELF.UI.POS ES LA POSICION ACTUAL DE LA VENTANA
            #GLOBALPOS ES LA POSICION DEL MOUSE
            #DRAG POS ES LA POSICION DE DONDE ESTA SIENDO ARRASTRADA LA VENTANA

            self.ui.move(self.ui.pos() + event.globalPos() - self.drag_pos)
            #IGUALAMOS POSICIONES
            self.drag_pos = event.globalPos()
    
    #SOMBRA DE LA VENTANA
    def set_window_shadow(self):
        shadow = QGraphicsDropShadowEffect(self.ui)
        #QUE TAN BORROSA SE VERA LA SOMBRA
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        # SE LO ENVIAMOS AL FRAME QUE LO CONTIENE
        self.ui.background_frame.setGraphicsEffect(shadow)

     
    def fill_category_cb(self):
        self.ui.operario_combo_box.addItems(DBUsuario().select_name_usuario_enabled())
        self.ui.pieza_combo_box_2.addItems(DBPieza().select_name_piezas())
        self.ui.maquina_combo_box_3.addItems(DBMaquina().select_name_maquinas_enabled())