from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from database.maquina import DBMaquina

from interface.recipe_details_window import DetailWindow
from interface.general_custom_ui import GeneralCustomUi
from database.proceso import DBProceso
from database.usuario import DBUsuario
from database.maquina import DBMaquina
from database.pieza import DBPieza


class DetailWindowForm(QWidget, DetailWindow):

    def __init__(self, parent=None, recipe_id=None):
        super().__init__(parent)

        self.recipe_id = recipe_id

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_widgets()
    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def fill_widgets(self):
        data = DBProceso("select", id_proceso = self.recipe_id)
        #print(data.id_nombre)
        operario = DBUsuario("select", id_usuario = data.id_nombre)
        maquina = DBMaquina("select" , id_maquina = data.id_maquina)
        pieza = DBPieza("select", id_pieza = data.id_pieza)
        #print("dsfsdfsdf")
        #print(self.recipe_id)
        #print("data fill ")
        #data = recipes.select_by_id(self.recipe_id)
        #print(data.nombre)
        #print("data fill2 ")
        self.nombre_label.setText(data.nombre)
        self.hora_inicio_label.setText(str(data.hora_inicio))
        self.operario_label.setText(operario.nombre)
        self.maquina_label.setText(maquina.nombre)
        self.pieza_label.setText(pieza.nombre)
        #title = data[1]
        #category = data[2]
        #url = data[3]
        #budget = data[4]
        #img_path = data[5]
        #ingredients = data[6]
        #directions = data[7]

        #self.recipe_title_label.setText(title)
        #self.recipe_category_label.setText(category)
        #self.ingredients_text_edit.setPlainText(ingredients)
        #self.directions_text_edit.setPlainText(directions)
        #self.set_recipe_budget(budget)
        #self.set_recipe_url(url)
        #self.set_recipe_image(img_path)
        pass

    def set_recipe_budget(self, budget):
        #para darle formato a los numeros
        budget = f"${str(budget)}"
        self.recipe_budget_label.setText(budget)
    
    def set_recipe_url(self, url):
        url = f"<a href={url}>{url}</a>"
        self.recipe_url_label.setOpenExternalLinks(True)
        self.recipe_url_label.setText(url)
    
    def set_recipe_image(self, img_path):
        pix_map = QPixmap(img_path)

        self.recipe_pic_label.setPixmap(pix_map)
        self.recipe_pic_label.setScaledContents(True)
