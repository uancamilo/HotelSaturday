import mysql.connector

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
            print(f"Base de datos '{self.database}' verificada/creada correctamente")
        except mysql.connector.Error as err:
            print("Error al crear la base de datos:", err)
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión a base de datos establecida")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)
            self.connection = None
        return self.connection

    def create_tables_if_not_exist(self):
        if self.connection is None:
            self.connection = self.connect()

        cursor = None
        try:
            cursor = self.connection.cursor()

            queries = [
                """
                CREATE TABLE IF NOT EXISTS user (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20),
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    status ENUM('active', 'inactive') DEFAULT 'active'
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS employee (
                    id INT PRIMARY KEY,
                    rol VARCHAR(50) NOT NULL,
                    FOREIGN KEY (id) REFERENCES user(id) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS guest (
                    id INT PRIMARY KEY,
                    origin VARCHAR(100),
                    occupation VARCHAR(100),
                    FOREIGN KEY (id) REFERENCES user(id) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS bedrooms (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    number VARCHAR(10) UNIQUE NOT NULL,
                    type ENUM('single', 'double', 'suite') NOT NULL,
                    price DECIMAL(10,2) NOT NULL,
                    status ENUM('available', 'occupied', 'maintenance') DEFAULT 'available'
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS services (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    price DECIMAL(10,2) NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS bookings (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    bedroom_id INT NOT NULL,
                    service_id INT,
                    check_in DATE NOT NULL,
                    check_out DATE NOT NULL,
                    total_price DECIMAL(10,2),
                    status ENUM('confirmed', 'cancelled', 'completed') DEFAULT 'confirmed',
                    FOREIGN KEY (user_id) REFERENCES user(id),
                    FOREIGN KEY (bedroom_id) REFERENCES bedrooms(id),
                    FOREIGN KEY (service_id) REFERENCES services(id)
                );
                """
            ]

            for query in queries:
                cursor.execute(query)

            print("Tablas creadas o verificadas correctamente.")

        except mysql.connector.Error as err:
            print("Error al crear las tablas:", err)
        finally:
            if cursor:
                cursor.close()

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
            print("Consulta ejecutada exitosamente")
            if query.strip().lower().startswith('select'):
                return cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None
        finally:
            if cursor:
                cursor.close()
