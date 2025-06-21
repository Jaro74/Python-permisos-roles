import pymysql

class CConexion:
    
    @staticmethod
    def conexion_base_datos():
        # Conexión a la base de datos MySQL
        conn = pymysql.connect(
                user='root',
                password='Rafter+123',
                host='127.0.0.1',
                database='userdb',
                port=3306
            )
        return conn
    
    @staticmethod
    def get_users():
        conn = CConexion.conexion_base_datos()
        cursor = conn.cursor()  
        cursor.execute("SELECT nombre, password FROM usuarios")
        usuarios = cursor.fetchall()  # Recuperar la información de la consulta
        conn.close()  # Cerrar la conexión
        return usuarios
    
    @staticmethod
    def insert_user(name, surname, email, password):
        conn = CConexion.conexion_base_datos()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)", (name, surname, email, password))
        conn.commit()
        conn.close()
    
    @staticmethod
    def insert_user_surname(user):
        conn = CConexion.conexion_base_datos()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO usuarios (apellidos) VALUES (%s)", (user.surname,))
        conn.commit()
        conn.close()
    
    @staticmethod
    def insert_user_email(user):
        conn = CConexion.conexion_base_datos()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO usuarios (email) VALUES (%s)", (user.email,))
        conn.commit()
        conn.close()
    
    @staticmethod
    def insert_user_password(user):
        conn = CConexion.conexion_base_datos()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO usuarios (password) VALUES (%s)", (user.password,))
        conn.commit()
        conn.close()

# Intentar conectar y verificar el resultado
if __name__ == '__main__':
    conexion = CConexion.conexion_base_datos()
    if conexion:
        print("Operaciones con la base de datos")
        conexion.close()
        print("Conexión cerrada")
    else:
        print("No se pudo establecer la conexión a la base de datos")