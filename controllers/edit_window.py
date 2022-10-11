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
        print(self.recipe_id)
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
        data = ( maquina._id_maquina,pieza._id_pieza, operario._id_usuario,proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),'')
        print("data")
        print(data)

        proc = DBProceso( mode = "update" , id_proceso= self.recipe_id ,id_maquina =  maquina._id_maquina,  id_pieza = pieza._id_pieza, id_nombre =  operario._id_usuario, nombre =  proceso, observaciones = ' ')
       
        self.parent.set_table_data()


    def set_current_text_cb(self, text):
        text_index = self.category_combo_box.findText(text)
        self.category_combo_box.setCurrentIndex(text_index)
    
    def fill_inputs(self):
        #data = recipes.select_by_id(self.recipe_id)
        proceso = DBProceso("select", id_proceso = self.recipe_id)
        print("idproceos")
        print(proceso.id_nombre)
        self.nombre_line_edit.setText(proceso.nombre)
        usuario = DBUsuario("select", id_usuario=  proceso.id_nombre)
        pieza = DBPieza("select", id_pieza=  proceso.id_pieza)
        maquina = DBMaquina("select", id_maquina=  proceso.id_maquina)
        self.operario_combo_box.setCurrentText(usuario.nombre)
        self.pieza_combo_box_2.setCurrentText(pieza.nombre)
        self.maquina_combo_box_3.setCurrentText(maquina.nombre)
       
        
    def clear_inputs(self):
        self.ui.fill_category_cb()

