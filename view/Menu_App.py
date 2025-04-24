from domain.models.Guest import Guest
from application.GuestService import GuestService
from application.GuestInput import GuestInput
from repository.conexion.Conexion import Conexion

class Menu_App:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3307, user='root', password="", database='hotel_saturday')
        self.db.create_database_if_not_exists()
        self.db.connect()
        self.db.create_tables_if_not_exist()

        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.guest_service = GuestService()
        self.guest_input = GuestInput()

    def init_app(self):
        init = int(input("Presione 1 para inicializar: "))

        while init != 0:
            option = int(input("1. Login  2. Registro  3. Salir: "))

            if option == 1:
                print("Login")
            elif option == 2:
                print("Registro")
                self.guest_input.register(self.guest, self.db)
            elif option == 3:
                self.db.disconnect()
                print("Hasta luego")
                break
