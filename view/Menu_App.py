from repository.conexion.Conexion import Conexion
from application.GuestInput import GuestInput
from application.GuestService import GuestService
from application.BedroomInput import BedroomInput
from application.EmployeeInput import EmployeeInput
from application.EmployeeService import EmployeeService

class Menu_App:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user="admin", password="admin", database='hotel_saturday')
        self.db.create_database_if_not_exists()
        self.db.connect()
        self.db.create_tables_if_not_exist()

        self.guest_input = GuestInput()
        self.guest_service = GuestService()
        self.bedroom_input = BedroomInput()
        self.employee_input = EmployeeInput()
        self.employee_service = EmployeeService()

        self.logged_employee = None

    def ensure_superadmin_exists(self):
        """Verifica si existe al menos un superadmin y un empleado, si no, los crea automáticamente."""

        # Verificar si existe algún Superadmin
        query_superadmin = "SELECT COUNT(*) FROM employee WHERE rol = 'superadmin'"
        result_superadmin = self.db.execute_query(query_superadmin)

        if result_superadmin and result_superadmin[0][0] == 0:
            print("\n⚡ No se encontró ningún Superadmin. Creando uno automáticamente...")

            id_superadmin = 1
            name_superadmin = "Super"
            last_name_superadmin = "Admin"
            phone_superadmin = "3000000000"
            email_superadmin = "superadmin@hotel.com"
            password_superadmin = "admin123"

            # Insertar Superadmin en tablas person y employee
            insert_person = """
                INSERT INTO person (id, name, last_name, phone, email)
                VALUES (%s, %s, %s, %s, %s)
            """
            person_values = (id_superadmin, name_superadmin, last_name_superadmin, phone_superadmin, email_superadmin)
            self.db.execute_query(insert_person, person_values)

            insert_employee = """
                INSERT INTO employee (id, password, rol, status)
                VALUES (%s, %s, %s, %s)
            """
            employee_values = (id_superadmin, password_superadmin, "superadmin", "active")
            self.db.execute_query(insert_employee, employee_values)

            print("✅ Superadmin creado exitosamente.")

        # Verificar si existe algún Empleado normal
        query_employee = "SELECT COUNT(*) FROM employee WHERE rol = 'employee'"
        result_employee = self.db.execute_query(query_employee)

        if result_employee and result_employee[0][0] == 0:
            print("\n⚡ No se encontró ningún Empleado normal. Creando uno automáticamente...")

            id_employee = 2
            name_employee = "Empleado"
            last_name_employee = "Normal"
            phone_employee = "3010000000"
            email_employee = "empleado@hotel.com"
            password_employee = "empleado123"

            # Insertar Empleado en tablas person y employee
            insert_person = """
                INSERT INTO person (id, name, last_name, phone, email)
                VALUES (%s, %s, %s, %s, %s)
            """
            person_values = (id_employee, name_employee, last_name_employee, phone_employee, email_employee)
            self.db.execute_query(insert_person, person_values)

            insert_employee = """
                INSERT INTO employee (id, password, rol, status)
                VALUES (%s, %s, %s, %s)
            """
            employee_values = (id_employee, password_employee, "employee", "active")
            self.db.execute_query(insert_employee, employee_values)

            print("✅ Empleado normal creado exitosamente.")

    def init_app(self):
        self.ensure_superadmin_exists()  # 🔥 Esto debe ser LO PRIMERO.

        while True:
            if not self.logged_employee:
                self.login()
                continue

            print(
                f"\n--- Menú Principal Hotel Saturday --- (Usuario: {self.logged_employee.person.name} - Rol: {self.logged_employee.rol})")
            print("1. Registro de Huésped")

            if self.logged_employee.rol == "superadmin":
                print("2. Registro de Empleado")

            print("3. Gestión de Habitaciones")
            print("4. Cerrar Sesión")
            print("5. Salir")
            print("------------------------------------")

            option_str = input("Seleccione una opción: ")
            if not option_str.isdigit():
                print("❌ Opción inválida. Ingrese un número.")
                continue
            try:
                option = int(option_str)
            except ValueError:
                print("❌ Entrada inválida.")
                continue

            if option == 1:
                self.register_guest()
            elif option == 2 and self.logged_employee.rol == "superadmin":
                self.register_employee()
            elif option == 3:
                self.menu_habitaciones()
            elif option == 4:
                self.logout()
            elif option == 5:
                self.exit_app()
                break
            else:
                print("❌ Opción no válida.")

    def login(self):
        print("\n--- Iniciar Sesión ---")
        email = input("Email: ").strip()
        password = input("Contraseña: ").strip()

        employee = self.employee_service.validate_login(email, password, self.db)

        if employee:
            if employee.status == "inactive":
                print("❌ El usuario está inactivo. Contacte al administrador.")
                return
            self.logged_employee = employee
            print(f"✅ Bienvenido {self.logged_employee.person.name} ({self.logged_employee.rol})")
        else:
            print("❌ Email o contraseña incorrectos.")

    def logout(self):
        print(f"\n👋 {self.logged_employee.person.name} ha cerrado sesión.")
        self.logged_employee = None

    def register_guest(self):
        print("\n--- Registro de Nuevo Huésped ---")
        self.guest_input.register(self.db)

    def register_employee(self):
        print("\n--- Registro de Nuevo Empleado ---")

        if self.logged_employee.rol != "superadmin":
            print("❌ Solo un superadmin puede registrar empleados.")
            return

        # Preguntar rol del nuevo empleado
        print("\nSeleccione el rol del nuevo empleado:")
        print("1. Superadmin")
        print("2. Empleado normal")
        rol_option = input("Seleccione una opción: ")

        if rol_option not in ["1", "2"]:
            print("❌ Rol no válido.")
            return

        if rol_option == "1":
            # Verificar si ya existe un superadmin
            query = "SELECT COUNT(*) FROM employee WHERE rol = 'superadmin'"
            result = self.db.execute_query(query)

            if result and result[0][0] >= 1:
                print("❌ Ya existe un Superadmin en el sistema. No se puede crear otro.")
                return

            rol = "superadmin"
        else:
            rol = "employee"

        # Continuar con el registro
        self.employee_input.register(self.db, rol)

    def menu_habitaciones(self):
        while True:
            print("\n--- Gestión de Habitaciones ---")
            print("1. Crear habitación")
            print("2. Listar habitaciones")
            print("3. Volver al menú principal")
            print("-----------------------------")
            option_str = input("Seleccione una opción: ")
            try:
                option = int(option_str)
            except ValueError:
                option = 0

            if option == 1:
                self.create_bedroom()
            elif option == 2:
                self.list_bedrooms()
            elif option == 3:
                print("Volviendo al menú principal...")
                break
            else:
                print("❌ Opción no válida.")

    def create_bedroom(self):
        print("\n--- Crear Nueva Habitación ---")
        self.bedroom_input.create_bedroom(self.db)

    def list_bedrooms(self):
        print("\n--- Listar Habitaciones ---")
        self.bedroom_input.list_bedrooms(self.db)

    def exit_app(self):
        print("\nCerrando la conexión con la base de datos...")
        self.db.disconnect()
        print("¡Hasta luego!")

if __name__ == "__main__":
    print("Iniciando aplicación Hotel Saturday...")
    app = Menu_App()
    try:
        app.init_app()
    except KeyboardInterrupt:
        print("\nSaliendo por solicitud del usuario...")
        app.exit_app()
    except Exception as e:
        print(f"\n❌ Ha ocurrido un error inesperado: {e}")
        if app.db and hasattr(app.db, 'connection') and app.db.connection and app.db.connection.is_connected():
            app.db.disconnect()
    finally:
        print("Aplicación finalizada.")
