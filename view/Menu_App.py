from repository.conexion.Conexion import Conexion
from application.GuestInput import GuestInput
from application.GuestService import GuestService
from application.BedroomInput import BedroomInput
from application.BookingInput import BookingInput

class Menu_App:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_saturday')
        self.db.create_database_if_not_exists()
        self.db.connect()
        self.db.create_tables_if_not_exist() 

        self.guest_input = GuestInput()
        self.guest_service = GuestService()
        self.bedroom_input = BedroomInput()
        self.booking_input = BookingInput() 

    def init_app(self):
        while True:
            print("\n--- Menú Principal Hotel Saturday ---")
            print("1. Login")
            print("2. Registro de Huésped")
            print("3. Gestión de Habitaciones")
            print("4. Gestión de Reservas (Booking)") 
            print("5. Salir")
            print("------------------------------------")

            option_str = input("Seleccione una opción: ")
            if not option_str.isdigit():
                print("Opción inválida. Por favor ingrese un número.")
                continue
            try:
                option = int(option_str)
            except ValueError:
                 print("Entrada inválida.")
                 continue

            if option == 1:
                self.login()
            elif option == 2:
                self.register_guest()
            elif option == 3:
                self.menu_habitaciones()
            elif option == 4:
                self.menu_gestion_reservas() 
            elif option == 5:
                self.exit_app()
                break
            else:
                print("Opción no válida.")

    def login(self):
        print("Funcionalidad de Login no implementada.")

    def register_guest(self):
        print("\n--- Registro de Nuevo Huésped ---")
        self.guest_input.register(self.db)

    def menu_habitaciones(self):
        while True:
            print("\n--- Gestión de Habitaciones ---")
            print("1. Crear habitación")
            print("2. Listar habitaciones")
            print("3. Volver al menú principal")
            print("-----------------------------")
            option_str = input("Seleccione una opción: ")
            try: option = int(option_str)
            except: option = 0 

            if option == 1:
                self.create_bedroom()
            elif option == 2:
                self.list_bedrooms()
            elif option == 3:
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida.")

    def create_bedroom(self):
        print("\n--- Crear Nueva Habitación ---")
        self.bedroom_input.create_bedroom(self.db)

    def list_bedrooms(self):
        print("\n--- Listar Habitaciones ---")
        self.bedroom_input.list_bedrooms(self.db) 

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
                print("Opción inválida.")
                continue
            try: option = int(option_str)
            except ValueError: option = 0

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
                print("Opción no válida.")

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
         print(f"\nHa ocurrido un error inesperado: {e}")
         if app.db and hasattr(app.db, 'connection') and app.db.connection and app.db.connection.is_connected():
              app.db.disconnect()
     finally:
         print("Aplicación finalizada.")