from interface.recipe_details_window import DetailWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from interface.main_window import MainWindow
from controllers.add_window import AddWindowForm
from controllers.edit_window import EditWindowForm
from controllers.recipe_details_window import DetailWindowForm
from interface.general_custom_ui import GeneralCustomUi
from database.proceso import DBProceso
from database.administrador import  DBAdministrador
from interface import components
import os
from interface.login_window import  DetailWindow as LoginWindow
from PyQt5.QtGui import QPixmapCache
from PyQt5 import QtWidgets


class LoginWindowForm(QWidget, LoginWindow):

    def __init__(self, parent=None, recipe_id=None,nombre_proceso="", nombre_pieza = ""):
        super().__init__(parent)
        self.nombre_proceso = nombre_proceso
        self.nombre_pieza = nombre_pieza
        self.parent = parent 
        self.recipe_id = recipe_id

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        self.add_edit_button_3.setText("Confirmar")
        self.add_edit_button_3.clicked.connect(self.finish_recipe)
        self.contrasena_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.fill_widgets()
    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def finish_recipe(self):

        if(self.contrasena_line_edit.text() != "" and  self.administrador_line_edit.text() != ""):
            print(self.contrasena_line_edit.text())
            print(self.administrador_line_edit.text())
            admin = DBAdministrador(mode = "authentication" , nombre = self.administrador_line_edit.text(),
            contrasena= self.contrasena_line_edit.text())
            print("ADDDD nombre")
            print(admin.nombre)
            if( admin.nombre == self.administrador_line_edit.text()):
                print("finish recipe id")
                print(self.recipe_id)
                DBProceso("finish" , id_proceso = self.recipe_id)
                info = DBProceso.select_numero_piezas_merma(self, nombre = self.nombre_proceso, pieza= self.nombre_pieza)
                peso_normal = info[0][0] * info[0][1] 
                print("PESO BASE MERMA")
                print(peso_normal)
                self.parent.set_table_data()
                self.close()
            else:
                print("AUTENTIFICACION FALLIDA  ")

    def set_recipe_budget(self, budget):
        #para darle formato a los numeros
        budget = f"${str(budget)}"
        self.recipe_budget_label.setText(budget)
    
    def set_recipe_url(self, url):
        url = f"<a href={url}>{url}</a>"
        self.recipe_url_label.setOpenExternalLinks(True)
        self.recipe_url_label.setText(url)
    



        

