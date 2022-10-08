from database.connection import create_connection
from random import randrange, choice

class DBPieza():

    def __init__(self, mode = '' ,nombre = '', id_pieza = 0):
        self._id_pieza = id_pieza
        self._nombre = nombre

        if self._nombre != '' and mode == 'new':
            self._id_pieza = randrange(1111,9999,1)
            sql = 'INSERT INTO pieza(id_pieza,nombre_pieza) VALUES("{}","{}")'.format(self._id_pieza, self._nombre)
            try:
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
                cursor.close()
                print("logrado")
            except Exception as e:
                print(e)
                raise
        elif self._nombre != '' and mode == 'select':
            self.select_id_pieza()  
        elif self._id_pieza != 0 and mode == 'select':
            self.select_pieza()
                
        else:
            print("Objeto vacio")

    def select_pieza(self):
        sql = 'SELECT id_pieza, nombre_pieza from pieza where id_pieza = {}'.format(self._id_pieza)
        objeto_pieza = []
        try: 
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            pieza = cursor.fetchone()
            objeto_pieza = [pieza[0],pieza[1]]
            self._nombre = pieza[1]
            cursor.close()
            return objeto_pieza
        except Exception as e:
            print(e)
            raise
            
    def select_name_piezas(self):
        sql = 'SELECT nombre_pieza from pieza '
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            piezas = cursor.fetchall()
            lista  = []
            for pieza in piezas:
                lista.append(pieza[0])
            cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise
    
    def select_id_pieza(self):
        sql = 'SELECT id_pieza from pieza where nombre_pieza = "{}"'.format(self._nombre)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            id= cursor.fetchone()
            self._id_pieza = id[0]
            #cursor.close()          
        except Exception as e: 
            print("error")
            print(e)
            raise

    @property
    def id_pieza(self):
            return(self._id_pieza)
    
    @property
    def nombre(self):
        return(self._nombre)




    

#pieza = DBPieza('select','pieza1')
#print(pieza.id_pieza)    
#print(pieza.nombre)
#list = pieza.select_name_piezas()
#print(list)
#print(select_name_piezas())
#print(select_id_pieza('Socket'))
#pza = DBPieza(3)
#pza.select_pieza(3)























































