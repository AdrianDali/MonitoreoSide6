from string import printable
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import Qt

from interface.add_edit_window import AddEditWindow
from interface.general_custom_ui import GeneralCustomUi

from database.usuario import DBUsuario
from database.proceso import DBProceso
from database.pieza import DBPieza
from database.maquina import DBMaquina
import threading
import shutil
import serial 
import datetime 
#import RPi.GPIO as GPIO
import time



class AddWindowForm(QWidget, AddEditWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.parent = parent

        #self.ser = serial.Serial("/dev/ttyACM0" , 9600)
        #self.ser.flushInput()
        self.contadorM1 = 0 
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
        self.proceso = self.nombre_line_edit.text()
        operario = DBUsuario("select",self.operario_combo_box.currentText())
        pieza = DBPieza("select" ,self.pieza_combo_box_2.currentText())
        maquina = DBMaquina("select" ,self.maquina_combo_box_3.currentText())
        observaciones = self.observaciones_text_edit.toPlainText()
        print("observaciones")
        print(observaciones)
       
        data = ( maquina._id_maquina,pieza._id_pieza, operario._id_usuario,self.proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),'')
        print(data)


        self.proceso = DBProceso("new",maquina._id_maquina,pieza._id_pieza, operario._id_usuario,self.proceso,str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),observaciones)
        
        
        print("SELECT ID PROCESO ")
        
        datos  = self.proceso.select_id_proceso()
        
        print("------------------")
            #self.save_img()
            #print("Recipe Added")
        self.clear_inputs()
        self.parent.set_table_data()
        self.inicioProceso(operario._id_usuario , self.proceso.select_id_proceso())
        print("cool")
        self.close()

    
    def inicioProceso(self,idUsuario,idProceso):
       
        thread = threading.Thread(target= self.monitoreoProceso , args=(idProceso,idUsuario))
        thread.start()
        print("HILO INICIALIZADO")


    def monitoreoProceso(self,idProceso,idUsuario):
        
        while(True):
            #if GPIO.input(10) == GPIO.HIGH:
             #   self.contadorM1 = self.contadorM1 +1  
                #print("linesss")
                #lineBytes = self.ser.readline()
                #print("line antes decode ")
                #print(lineBytes)
                #print("LINE ")
                #line = lineBytes.decode("utf-8").strip()
                #print("LINEEEEEEE  pesooooooooooo")
                #print(line)

                #print("line peso")

                #global self.contadorM1 
                #self.contadorM1 = self.contadorM1 + 1 
                #self.proceso.insertar_monitoreo_proceso()
                #print("monitoreo_proceos")
                #print(self.contadorM1)
                #self.proceso.actualizar_piezas_proceso(self.contadorM1)
                #if(line != "..."):
                #    self.proceso.actualizar_peso_proceso(line)
                #
                # actualizar_piezas_proceso(contadorM1, idProceso)
                #actualizar_peso_proceso(line, idProceso)
                #self.tabla_peliculas()
                #self.actualizar_tabla()
                #self.parent.actualizar_grafica(self.contadorM1)
                #time.sleep(2)
            pass
    
    def actualizar_tabla(self):
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
   