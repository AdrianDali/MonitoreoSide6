
from database.connection import create_connection
from random import randrange

class DBUsuario():
    def __init__(self, mode = '',nombre = '', id_usuario = 0):
        self._id_usuario = id_usuario
        self._fecha_ingreso = ''
        self._nombre = nombre
        self._edad = 0
        self._disponible = 0 
        if self._nombre != '' and mode == 'new': 
            self._id_usuario = randrange(1111,9999,1)
            sql = 'INSERT INTO usuarios(id_usuario,fecha_ingreso,nombre,edad,disponible)VALUES("{}",<{fecha_ingreso: }>,,,0);'.format(self._id_usuario, self._nombre)
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
            self.select_id_usuario()  

        elif self._id_usuario != 0 and mode == 'select':
            
            #print("select usuarioggggg")
            self.select_usuario_info()   

        else:
            print("Objeto vacio")
        

    def select_usuario_info(self):
        print("select 222")
        sql = 'SELECT id_usuario, nombre, disponible from usuarios where id_usuario = {}'.format(self._id_usuario)
        objeto_usuario = []
        try: 
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            usuario = cur.fetchone()
            #print(usuario)
            objeto_usuario = [usuario[0],usuario[1],usuario[2]]
            print("objeto usuario",objeto_usuario)
           
            self._nombre = usuario[1]
            #print("self nombre")
            #print(self._nombre)
            cur.close()
            return objeto_usuario
        except Exception as e:
            print(e)
            raise
        
    
    def select_name_usuario_enabled(self):
        sql = 'SELECT nombre from usuarios where disponible = 1 '
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            maquinas = cursor.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise
        finally:
            connection.close()

    def select_usuario(param):
        #sql = """select """
        pass
                

    def select_id_usuario(self):
        sql = 'SELECT id_usuario from usuarios where nombre = "{}" '.format(self._nombre)
        objeto_usuario = []
        try: 
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            usuario = cursor.fetchone()
            user = usuario[0]
            self._id_usuario = user
            print(user)
            cursor.close()
            return user
        except Exception as e:
            print(e)
            raise
        finally:
            #cursor.close()
            connection.close()
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def nombre(self):
        return self._nombre

    


#usuario  = DBUsuario("select","Adrian Dali")
#print(usuario.id_usuario)
#print(usuario.nombre)

#usuario.select_usuario(2)
#print(usuario.select_name_usuario_enabled())