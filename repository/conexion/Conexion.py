import mysql
from mysql import connector

class Conexion:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def create_database_if_not_exists(self):
        connection = None
        cursor = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print(f"Base de datos '{self.database}' verificada/creada")
        except mysql.connector.Error as err:
            print("Error al crear la base de datos:", err)
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def create_tables_if_not_exist(self):
        if self.connection is None:
            self.connection = self.connect()

        cursor = None
        try:
            cursor = self.connection.cursor()
            tabla_usuarios = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                correo VARCHAR(100),
                creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(tabla_usuarios)
            print("Tablas verificadas/creadas correctamente")
        except mysql.connector.Error as err:
            print("Error al crear las tablas:", err)
        finally:
            if cursor:
                cursor.close()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión Establecida")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)
            self.connection = None

        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión Cerrada")

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("No hay conexión a la base de datos.")
            return None

        cursor = None
        try:
            cursor = self.connection.cursor(buffered=True)
            cursor.execute(query, params)
            self.connection.commit()
            print("Registro se guardó exitosamente")
            if query.lower().startswith('select'):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None
        finally:
            if cursor:
                cursor.close()
