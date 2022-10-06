from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from interface.add_edit_window import AddEditWindow
from interface.general_custom_ui import GeneralCustomUi
import datetime
from database.usuario import DBUsuario
from database.proceso import DBProceso
from database.pieza import DBPieza
from database.maquina import DBMaquina
import os
import shutil


class EditWindowForm(QWidget, AddEditWindow):

    def __init__(self, parent=None, recipe_id=None):
        self.recipe_id = recipe_id
        self.parent = parent

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
        self.ui.fill_category_cb()
        self.fill_inputs()
        
        self.add_edit_button.setText("Editar")
        self.add_edit_button.clicked.connect(self.update_recipe)
        #self.select_img_button.clicked.connect(self.select_img)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def update_recipe(self):
        proceso = self.nombre_line_edit.text()
        operario = DBUsuario("select",self.operario_combo_box.currentText())
        pieza = DBPieza("select" ,self.pieza_combo_box_2.currentText())
        maquina = DBMaquina("select" ,self.maquina_combo_box_3.currentText())
        hora_inicio = self.inicio_timeEdit.text()
        data = ( maquina._id_maquina,pieza._id_pieza, operario._id_usuario,proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),'')
        print(data)
        proceso = DBProceso(maquina._id_maquina,pieza._id_pieza, operario._id_usuario,proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),'')
        self.parent.set_table_data()


    def set_current_text_cb(self, text):
        text_index = self.category_combo_box.findText(text)
        self.category_combo_box.setCurrentIndex(text_index)
    
    def fill_inputs(self):
        #data = recipes.select_by_id(self.recipe_id)

        #self.title_line_edit.setText(data[1])
        #self.set_current_text_cb(data[2])
        #self.url_line_edit.setText(data[3])
        #self.budget_line_edit.setText(str(data[4]))

        #img_name = data[5].split("\\")[-1]

        #self.old_image = img_name
        #self.new_img = img_name

        #self.image_path_line_edit.setText(img_name)
        #self.ingredients_text_edit.setPlainText(data[6])
        #self.directions_text_edit.setPlainText(data[7])
        pass
    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]

        if self.img_path_from:
            self.new_img = self.img_path_from.split("/")[-1]
            self.image_path_line_edit.setText(self.new_img)
    
    def replace_img(self):
        if self.old_image != self.new_img:
            os.remove("recipe_images\\" + self.old_image)
            shutil.copy(self.img_path_from, "recipe_images")
    
    def clear_inputs(self):
        self.title_line_edit.clear()
        self.category_combo_box.clear()
        self.ui.fill_category_cb()
        self.url_line_edit.clear()
        self.budget_line_edit.clear()
        self.image_path_line_edit.clear()
        self.ingredients_text_edit.clear()
        self.directions_text_edit.clear()
