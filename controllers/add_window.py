from string import printable
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from interface.add_edit_window import AddEditWindow
from interface.general_custom_ui import GeneralCustomUi

from database.usuario import DBUsuario
from database.proceso import DBProceso
from database.pieza import DBPieza
from database.maquina import DBMaquina

import shutil
import datetime 

class AddWindowForm(QWidget, AddEditWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.ui.fill_category_cb()
        self.setWindowFlag(Qt.Window)

        self.add_edit_button.setText("Agregar")
        
        self.add_edit_button.clicked.connect(self.add_recipe)
        #self.select_img_button.clicked.connect(self.select_img)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def add_recipe(self):
        proceso = self.nombre_line_edit.text()
        operario = DBUsuario("select",self.operario_combo_box.currentText())
        pieza = DBPieza("select" ,self.pieza_combo_box_2.currentText())
        maquina = DBMaquina("select" ,self.maquina_combo_box_3.currentText())
        hora_inicio = self.inicio_timeEdit.text()
       
        data = ( maquina._id_maquina,pieza._id_pieza, operario._id_usuario,proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),'')
        print(data)


        proceso = DBProceso("new",maquina._id_maquina,pieza._id_pieza, operario._id_usuario,proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),'')

            #self.save_img()
            #print("Recipe Added")
        self.clear_inputs()
        self.parent.set_table_data()

    def select_img(self):
        #retorna una lista con los datos
        self.img_path_from = QFileDialog.getOpenFileName()[0]
        #obtener el nombre de la imagen, divide por / y obtenemos el ultimo 
        img_name = self.img_path_from.split("/")[-1]
        #concatenamos la ruta de la carpeta de imagenes con el nombre de la imagen
        self.img_path_to = f"recipe_images\{img_name}"
         
        self.image_path_line_edit.setText(img_name)

    #funcion que almacenara la imagen en la carpeta de imagenes
    def save_img(self):
        shutil.copy(self.img_path_from, "recipe_images")
    
    #limpiar las entradas de datos
    def clear_inputs(self):
        self.nombre_line_edit.clear()
        self.operario_combo_box.clear()
        self.ui.fill_category_cb()
        self.pieza_combo_box_2.clear()
        self.maquina_combo_box_3.clear()
        self.observaciones_text_edit.clear()
   