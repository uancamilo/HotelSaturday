import mysql.connector

class DatabaseManager:

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
            print(f"✅ Base de datos '{self.database}' verificada o creada correctamente.")
        except mysql.connector.Error as err:
            print("❌ Error al crear/verificar la base de datos:", err)
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
            print("✅ Conexión a base de datos establecida.")
        except mysql.connector.Error as err:
            print("❌ Error al conectar a la base de datos:", err)
            self.connection = None
        return self.connection

    def create_tables_if_not_exist(self):
        if self.connection is None:
            self.connect()

        cursor = None
        try:
            cursor = self.connection.cursor()

            queries = [
                """
                CREATE TABLE IF NOT EXISTS person (
                    id INT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20),
                    email VARCHAR(100) UNIQUE NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS employee (
                    id INT PRIMARY KEY,
                    password VARCHAR(255) NOT NULL,
                    rol VARCHAR(50) NOT NULL,
                    status ENUM('active', 'inactive') DEFAULT 'active',
                    FOREIGN KEY (id) REFERENCES person(id) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS guest (
                    id INT PRIMARY KEY,
                    origin VARCHAR(100),
                    occupation VARCHAR(100),
                    FOREIGN KEY (id) REFERENCES person(id) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS bedroom (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    number VARCHAR(10) UNIQUE NOT NULL,
                    bedroom_type ENUM('single', 'double', 'suite') NOT NULL,
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
                CREATE TABLE IF NOT EXISTS booking (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    bedroom_id INT NOT NULL,
                    check_in DATE NOT NULL,
                    check_out DATE NOT NULL,
                    total_price DECIMAL(10,2),
                    status ENUM('confirmed', 'cancelled', 'completed') DEFAULT 'confirmed',
                    FOREIGN KEY (user_id) REFERENCES person(id),
                    FOREIGN KEY (bedroom_id) REFERENCES bedroom(id)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS booking_service (
                    booking_id INT NOT NULL,
                    service_id INT NOT NULL,
                    PRIMARY KEY (booking_id, service_id),
                    FOREIGN KEY (booking_id) REFERENCES booking(id) ON DELETE CASCADE,
                    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
                );
                """
            ]

            for query in queries:
                cursor.execute(query)

            print("✅ Tablas creadas o verificadas correctamente.")
        except mysql.connector.Error as err:
            print("❌ Error al crear/verificar las tablas:", err)
        finally:
            if cursor:
                cursor.close()

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("❌ No hay conexión activa con la base de datos.")
            return None

        cursor = None
        try:
            cursor = self.connection.cursor(buffered=True)
            cursor.execute(query, params)
            self.connection.commit()

            if query.strip().lower().startswith('select'):
                return cursor.fetchall()
        except mysql.connector.Error as err:
            print("❌ Error al ejecutar consulta:", err)
            return None
        finally:
            if cursor:
                cursor.close()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("✅ Conexión a base de datos cerrada.")
