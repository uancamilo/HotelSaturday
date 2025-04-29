from application.SecurityService import SecurityService
from application.SeedData import SeedData
from repository.conexion.DatabaseManager import DatabaseManager
from application.GuestInput import GuestInput
from application.GuestService import GuestService
from application.BedroomInput import BedroomInput
from application.EmployeeInput import EmployeeInput
from application.EmployeeService import EmployeeService
from application.BookingInput import BookingInput

class Menu_App:

    def __init__(self):
        self.db = DatabaseManager(host="localhost", port=3306, user="admin", password="admin", database="hotel_saturday")
        self.db.create_database_if_not_exists()
        self.db.connect()
        self.db.create_tables_if_not_exist()

        seeder = SeedData(self.db)
        seeder.run()

        # Nuevo: inicializar seguridad
        self.security_service = SecurityService(self.db)
        self.security_service.ensure_initial_users()

        # Instanciar inputs
        self.guest_input = GuestInput()
        self.guest_service = GuestService()
        self.bedroom_input = BedroomInput()
        self.employee_input = EmployeeInput()
        self.employee_service = EmployeeService()
        self.booking_input = BookingInput()

        self.logged_employee = None

    def init_app(self):
        while True:
            if not self.logged_employee:
                self.login()
                continue

            print(
                f"\n--- Menú Principal Hotel Saturday --- (Usuario: {self.logged_employee.person.name} - Rol: {self.logged_employee.rol})")
            print("1. Gestión de Huéspedes")

            if self.logged_employee.rol == "superadmin":
                print("2. Registro de Empleado")

            print("3. Gestión de Habitaciones")
            print("4. Gestión de Reservas")
            print("5. Cerrar Sesión")
            print("6. Salir")
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
                self.menu_huespedes()
            elif option == 2 and self.logged_employee.rol == "superadmin":
                self.register_employee()
            elif option == 3:
                self.menu_habitaciones()
            elif option == 4:
                self.menu_gestion_reservas()
            elif option == 5:
                self.logout()
            elif option == 6:
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

    def menu_huespedes(self):
        while True:
            print("\n--- Gestión de Huéspedes ---")
            print("1. Registrar Nuevo Huésped")
            print("2. Listar Huéspedes")
            print("3. Volver al menú principal")
            option_str = input("Seleccione una opción: ").strip()

            if not option_str.isdigit():
                print("❌ Opción inválida.")
                continue

            option = int(option_str)

            if option == 1:
                self.register_guest()
            elif option == 2:
                self.list_guests()
            elif option == 3:
                print("Volviendo al menú principal...")
                break
            else:
                print("❌ Opción no válida.")

    def register_guest(self):
        print("\n--- Registro de Nuevo Huésped ---")
        self.guest_input.register(self.db)

    def list_guests(self):
        print("\n--- Lista de Huéspedes ---")
        self.guest_service.listar_huespedes(self.db)

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

    def menu_gestion_reservas(self):
        while True:
            print("\n--- Gestión de Reservas (Booking) ---")
            print("1. Crear Nueva Reserva")
            print("2. Ver Todas las Reservas")
            print("3. Buscar Reserva por ID")
            print("4. Cancelar Reserva")
            print("5. Volver al menú principal")
            print("------------------------------------")
            option_str = input("Seleccione una opción: ")
            if not option_str.isdigit():
                print("❌ Opción inválida.")
                continue
            try:
                option = int(option_str)
            except ValueError:
                print("❌ Entrada inválida.")
                continue

            if option == 1:
                self.booking_input.create_booking_interactive(self.db)
            elif option == 2:
                self.booking_input.view_all_bookings(self.db)
            elif option == 3:
                self.booking_input.find_booking_interactive(self.db)
            elif option == 4:
                self.booking_input.cancel_booking_interactive(self.db)
            elif option == 5:
                print("Volviendo al menú principal...")
                break
            else:
                print("❌ Opción no válida.")

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
