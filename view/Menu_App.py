from domain.models.Guest import Guest
from application.GuestService import GuestService
from application.GuestInput import GuestInput
from repository.conexion.Conexion import Conexion
from domain.models.Bedroom import Bedroom
from application.BedroomInput import BedroomInput
from application.EmployeeService import EmployeeService
from application.UserService import UserService

class Menu_App:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_saturday')
        self.db.create_database_if_not_exists()
        self.db.connect()
        self.db.create_tables_if_not_exist()

        self.guest_service = GuestService()
        self.guest_input = GuestInput()
        self.bedroom_input = BedroomInput()

    def init_app(self):
        while True:
            option = int(input("Seleccione una opción:\n1. Login\n2. Registro\n3. Reservas\n4. Salir\n"))
            if option == 1:
                self.login()
            elif option == 2:
                self.register_guest()
            elif option == 3:
                self.menu_reservas()
            elif option == 4:
                self.exit_app()
                break

    def login(self):
        print("Login")

    def register_guest(self):
        print("Registro de huésped")
        guest = Guest(None, None, None, None, None, None, None, None, None)
        self.guest_input.register(guest, self.db)

    def list_guests(self):
        print("Listar huéspedes")
        self.guest_service.listar_huespedes(self.db)

    def menu_reservas(self):
        while True:
            option = int(input("Seleccione una opción:\n1. Crear habitación\n2. Listar habitaciones\n3. Volver\n"))
            if option == 1:
                self.create_bedroom()
            elif option == 2:
                self.list_bedrooms()
            elif option == 3:
                print("Volviendo al menú principal...")
                break

    def create_bedroom(self):
        print("Crear habitación")
        bedroom = Bedroom(None, None, None)
        self.bedroom_input.create_bedroom(self.db)

    def list_bedrooms(self):
        print("Listar habitaciones")
        self.bedroom_input.list_bedrooms(self.db)

    def exit_app(self):
        print("Cerrando la conexión con la base de datos...")
        self.db.disconnect()
        print("Hasta luego.")

    def __init__(self):
        self.employee_service = EmployeeService()
        self.user_service = UserService()

    def mostrar_menu_admin(self):
        while True:
            print("\n--- Menú de Administración ---")
            print("1. Gestión de Empleados")
            print("2. Gestión de Usuarios")
            print("3. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.gestionar_empleados()
            elif opcion == '2':
                self.gestionar_usuarios()
            elif opcion == '3':
                break
            else:
                print("Opción no válida.")

    def gestionar_empleados(self):
        while True:
            print("\n--- Gestión de Empleados ---")
            print("1. Agregar Empleado")
            print("2. Ver Empleado por ID")
            print("3. Ver Todos los Empleados")
            print("4. Actualizar Empleado")
            print("5. Eliminar Empleado")
            print("6. Volver al Menú de Administración")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                employee_id = input("ID del empleado: ")
                name = input("Nombre del empleado: ")
                email = input("Email del empleado: ")
                role = input("Rol del empleado: ")
                if self.employee_service.add_employee(employee_id, name, email, role):
                    print("Empleado agregado correctamente.")
                else:
                    print("Error al agregar empleado.")
            elif opcion == '2':
                employee_id = input("Ingrese el ID del empleado a buscar: ")
                employee = self.employee_service.get_employee_by_id(employee_id)
                if employee:
                    print(employee)
                else:
                    print("Empleado no encontrado.")
            elif opcion == '3':
                employees = self.employee_service.get_all_employees()
                if employees:
                    for emp in employees:
                        print(emp)
                else:
                    print("No hay empleados registrados.")
            elif opcion == '4':
                employee_id = input("Ingrese el ID del empleado a actualizar: ")
                name = input("Nuevo nombre del empleado: ")
                email = input("Nuevo email del empleado: ")
                role = input("Nuevo rol del empleado: ")
                if self.employee_service.update_employee(employee_id, name, email, role):
                    print("Empleado actualizado correctamente.")
                else:
                    print("Error al actualizar empleado.")
            elif opcion == '5':
                employee_id = input("Ingrese el ID del empleado a eliminar: ")
                if self.employee_service.delete_employee(employee_id):
                    print("Empleado eliminado correctamente.")
                else:
                    print("Error al eliminar empleado.")
            elif opcion == '6':
                break
            else:
                print("Opción no válida.")

    def gestionar_usuarios(self):
        while True:
            print("\n--- Gestión de Usuarios ---")
            print("1. Agregar Usuario")
            print("2. Ver Usuario por ID")
            print("3. Ver Usuario por Nombre de Usuario")
            print("4. Ver Todos los Usuarios")
            print("5. Actualizar Usuario")
            print("6. Eliminar Usuario")
            print("7. Volver al Menú de Administración")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                user_id = input("ID del usuario: ")
                username = input("Nombre de usuario: ")
                password = input("Contraseña: ") 
                employee_id = input("ID del empleado asociado (opcional, dejar vacío si no aplica): ") or None
                if self.user_service.add_user(user_id, username, password, employee_id):
                    print("Usuario agregado correctamente.")
                else:
                    print("Error al agregar usuario.")
            elif opcion == '2':
                user_id = input("Ingrese el ID del usuario a buscar: ")
                user = self.user_service.get_user_by_id(user_id)
                if user:
                    print(user)