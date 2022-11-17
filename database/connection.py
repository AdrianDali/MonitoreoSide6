from mysql import connector


config = {
    'user': 'rooot3',
    'password': '1234',
    'host': '192.168.1.109',
    'database': 'monitoreo_trabajo',
}

def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}" )
    return conn