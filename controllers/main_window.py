from interface.recipe_details_window import DetailWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.main_window import MainWindow
from controllers.add_window import AddWindowForm
from controllers.edit_window import EditWindowForm
from controllers.recipe_details_window import DetailWindowForm
from interface.general_custom_ui import GeneralCustomUi
from database.proceso import DBProceso
from interface import components
import os

class MainWindowForm(QWidget, MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
        self.config_table()
        self.set_table_data()

        self.new_recipe_button.clicked.connect(self.open_add_window)
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_line_edit.textChanged.connect(self.restore_table_data)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def open_add_window(self):
        window = AddWindowForm(self)
        window.show()
    
    def open_edit_window(self, recipe_id):
        window = EditWindowForm(self, recipe_id)
        window.show()
    
    #configuracion de la tabla
    def config_table(self):
        column_labels = ("ID", "NOMBRE USUARIO", "PROCESO","MAQUINA", "PIEZA", "HORA INICIO", "NUMERO PIEZAS", "PESO MERMA", "OBSERVACIONES", "OPCIONES")

        self.recipes_table.setColumnCount(len(column_labels))
        self.recipes_table.setHorizontalHeaderLabels(column_labels)
        #cambiar de tamano a la celda 
        self.recipes_table.setColumnWidth(1, 200)

        self.recipes_table.setColumnWidth(9, 120)
        #cambiar alto de la celda 
        self.recipes_table.verticalHeader().setDefaultSectionSize(150)
        #ocultar columna 
        self.recipes_table.setColumnHidden(0, True)
        # para que cuando selecciones una celda no se seleccione toda la fila

        self.recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    

    def populate_table(self, data):
        self.recipes_table.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                
                self.recipes_table.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell))
                )
            #agregar los botones a la tabla
            self.recipes_table.setCellWidget(
                index_row, 9, self.build_action_buttons()
            )

    #LE MANDAMOS LOS DATOS A LA TABLA QUE VIENEN DESDE LA BASE DE DATOS
    def set_table_data(self):
        data = DBProceso.select_procesos_unfinish(self)
        self.populate_table(data)
    
    def restore_table_data(self):
        param = self.search_line_edit.text()
        if param == "":
            self.set_table_data()
    
    def search(self):
        param = self.search_line_edit.text()
        if param != "":
            pass
            #data = recipes.select_by_parameter(param)
            #self.populate_table(data)
    
    def build_action_buttons(self):
        view_button = components.Button("view", "#17A2B8")
        edit_button = components.Button("edit", "#007BFF")
        delete_button = components.Button("delete", "#DC3545")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)

        view_button.clicked.connect(self.view_recipe)
        edit_button.clicked.connect(self.edit_recipe)
        delete_button.clicked.connect(self.delete_recipe)

        return buttons_frame
    
    def open_detail_window(self, recipe_id):
        window = DetailWindowForm(self, recipe_id)
        window.show()
    
    def view_recipe(self):
        button = self.sender()
        table = self.recipes_table

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            self.open_detail_window(recipe_id)
    
    def edit_recipe(self):
        button = self.sender()
        table = self.recipes_table

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            self.open_edit_window(recipe_id)
    
    def delete_recipe(self):
        button = self.sender()
        table = self.recipes_table

        if button:
            #recipe_id = self.get_recipe_id_from_table(table, button)
            #data = recipes.select_by_id(recipe_id)
            print("boton presionado")
            
            #if recipes.delete(recipe_id):
            #    self.remove_img(data[5])
            #    self.set_table_data()
    
    def remove_img(self, img_path):
        os.remove(img_path)
            
    def get_recipe_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        recipe_id = table.model().data(cell_id_index)
        return recipe_id