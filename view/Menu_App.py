from domain.models.Guest import Guest
from application.GuestService import GuestService
from application.GuestInput import GuestInput
from repository.conexion.Conexion import Conexion
from domain.models.Bedroom import Bedroom
from application.BedroomInput import BedroomInput

class Menu_App:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3307, user='root', password="", database='hotel_saturday')
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
