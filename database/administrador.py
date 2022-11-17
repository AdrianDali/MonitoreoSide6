from cmath import e
#from DBmysql import create_
import numpy as np
import datetime 
from database.connection import create_connection
from random import randrange 



class DBAdministrador(): 

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def contrasena(self):
        return self._contrasena

    def __init__(self , mode = "" , nombre = "" , contrasena = ""):
        self._nombre = nombre 
        self._contrasena = contrasena  
        
        if(self._nombre != "" and self._contrasena != "" and mode == "authentication"):
            self.authentication()
    

    def authentication(self):
        sql = 'SELECT nombre, contrasena  from administrador where nombre = "{}" and contrasena = "{}"'.format(self._nombre,self._contrasena)

        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            
            print("Lista autentificacion")
            print(maquinas)
            print("nombre")
            self._nombre = maquinas[0][0]
            
            print(self._nombre)
            self._contrasena = maquinas[0][1]
            print(self.contrasena)
            return True
        except Exception as e:
            print("Lista de autentificacion mal")
            return False 
            