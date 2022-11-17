from cmath import e
#from DBmysql import create_
import numpy as np
import datetime 
from database.connection import create_connection
from random import randrange 


class DBProceso():

    @property
    def id_proceso(self):
        return self._id_proceso
    
    @property 
    def id_maquina(self):
        return self._id_maquina
    
    @property
    def id_pieza(self):
        return self._id_pieza
    
    @property
    def id_nombre(self):
        return self._id_nombre
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def hora_inicio(self):
        return self._hora_inicio
    
    @property
    def observaciones(self):
        return self._observaciones

    @property 
    def hora_inicio(self):
        return self._hora_inicio

    def __init__(self, mode = '', id_maquina= 0 , id_pieza = 0 , id_nombre = 0 ,
     nombre = "",hora_inicio = '', observaciones = '', proceso_terminado = 0,
      numero_piezas = 0, peso_merma = 0,id_proceso = 0):
        self._id_proceso = id_proceso
        self._id_maquina = id_maquina 
        self._id_pieza = id_pieza
        self._id_nombre = id_nombre
        self._nombre = nombre 
        self._hora_inicio = hora_inicio
        self._observaciones = observaciones
        self._proceso_terminado = proceso_terminado
        self._numero_piezas = numero_piezas
        self._peso_merma = peso_merma

        if self._nombre != '' and mode == 'new':
            self._id_pieza = randrange(111111,999999,1)
            sql = 'INSERT INTO proceso(id_maquina,id_pieza,id_nombre ,nombre,hora_inicio,observaciones)VALUES({},{},{},"{}","{}","{}")'.format(id_maquina,id_pieza,id_nombre,nombre,hora_inicio,observaciones)
            try:
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
                cursor.close()
                print("logrado proceso iniciado")
            except Exception as e:
                print(e)
                raise
        elif self._id_proceso != '' and mode == 'select':
            #print("select id proceso  ")
            self.select_proceso()  
        elif self._nombre != '' and mode == 'update':
            self.update_proceso()
        elif self._id_proceso != "" and mode == "finish":
            self.finish_proceso()        
        else:
            print("Objeto proceso vacio")
            

    def select_name_maquinas_enabled(self):
        sql = 'SELECT nombre_maquina from maquina where disponible = 1 '
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()
            return lista
        except Exception as e:
            print(e)
            raise
    
    
    def select_procesos_unfinish(self):
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio,p.numero_piezas , p.peso_merma,p.observaciones FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre  where p.proceso_terminado = 1;'
            try:
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute(sql)
                procesos = cursor.fetchall()
                cursor.close()
                return procesos
            
            except Exception as e:
                print(e)
                raise


    def insertar_monitoreo_proceso(self):
        fecha= datetime.datetime.now()
        print(self._id_proceso)
        print(str(fecha.strftime("%Y-%m-%d %H:%M:%S")))
        sql = "insert into proceso_usuario(id_proceso, id_usuario,hora) values({},{},'{}')".format(self._id_proceso, self.id_nombre, str(fecha.strftime("%H:%M:%S")))
        try:
            connection = create_connection() 
            cursor = connection.cursor() 
            cursor.execute(sql)
            connection.commit()
            print("logrado ")
            cursor.close()
        except Exception as e: 
            raise 


    def actualizar_piezas_proceso(self, contador):
        sql = "update proceso set numero_piezas = {} where id_proceso = {}".format(contador, self._id_proceso)
        try:
            connection = create_connection() 
            cursor = connection.cursor() 
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e: 
            raise 

    
    def actualizar_peso_proceso(self, contador):
        print("EL peso que se metera")
        print(contador)
        sql = "update proceso set peso_merma = {} where id_proceso = {}".format(contador, self._id_proceso)
        try:
            connection = create_connection() 
            cursor = connection.cursor() 
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e: 
            raise 


    def update_proceso(self):
        sql = "UPDATE proceso SET id_maquina = {}, id_pieza = {}, id_nombre = {}, nombre = '{}' WHERE id_proceso = {}".format(self._id_maquina, self._id_pieza, self._id_nombre, self._nombre, self._id_proceso)
        print("idprceosd  ")
        print(self._id_proceso)
        try:
            connection = create_connection() 
            cursor = connection.cursor() 
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e: 
            raise 


    def finish_proceso(self):

        fecha= datetime.datetime.now()
        print(self._id_proceso)
        print(str(fecha.strftime("%Y-%m-%d %H:%M:%S")))


        sql = "UPDATE proceso SET hora_termino = '{}' , proceso_terminado = 0 WHERE id_proceso = {};".format(str(fecha.strftime("%Y-%m-%d %H:%M:%S")),self._id_proceso)
        print("idprceosd  ")
        print(self._id_proceso)
        try:
            connection = create_connection() 
            cursor = connection.cursor() 
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e: 
            raise 




    


    def select_id_proceso(self):
        sql = 'SELECT id_proceso from proceso where nombre = "{}" '.format(self._nombre)
        objeto_usuario = []
        print(self._nombre)
        try: 
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            datoss = cursor.fetchone()
            self._id_proceso = datoss[0]
            user = self._nombre
            print("aasfsgdfg")
            print(self._id_proceso)
            cursor.close()
            return user
        except Exception as e:
            print(e)
            print("Errror al seleccionar proceso")
            raise

    def select_proceso(self):
        sql = 'SELECT * from proceso where id_proceso = {} '.format(self._id_proceso)
        objeto_usuario = []
        try: 
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            self.nombre_proceso = []
            self.nombre_proceso =cursor.fetchall()
            
            user = self.nombre_proceso
            if(user == []): 
                print("no existe nada en la DB")
                
            else:
                self._nombre = user[0][4]
                self._id_proceso = user[0][0] 
                self._id_maquina = user[0][1]
                self._id_pieza = user[0][2]
                self._id_nombre = user[0][3]
                self._hora_inicio = user[0][5]
                #print(self.hora_inicio)
                print(user)
                cursor.close()
                return user
        except Exception as e:
            print(e)
            raise
    




#maquina  = DBProceso(1)
#list = maquina.select_name_maquinas_enabled()
#print(list)

#print(select_procesos_unfinish())
#print(insertar_monitoreo_proceso(43,2))
#print(actualizar_piezas_proceso(1,43))
#print(actualizar_peso_proceso(88,43))
#print(select_id_proceso("proceso00"))
#processs = DBProceso(2,2,2,"proceso00","2020-12-12 12:12:12","observaciones")


