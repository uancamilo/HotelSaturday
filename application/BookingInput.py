import datetime
from application.BookingService import BookingService

class BookingInput:
    def __init__(self):
        self.booking_service = BookingService()

    def _get_date_input(self, prompt):
        """Helper para obtener y validar entrada de fecha."""
        while True:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            try:
                return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                print("Formato de fecha inválido. Use YYYY-MM-DD.")

    def _get_int_input(self, prompt):
         """Helper para obtener y validar entrada de entero."""
         while True:
            id_str = input(prompt + ": ")
            try:
                return int(id_str)
            except ValueError:
                print("Entrada inválida. Debe ser un número entero.")

    def create_booking_interactive(self, db):
        """Maneja la entrada del usuario para crear una nueva reserva."""
        print("\n--- Crear Nueva Reserva ---")
        user_id = self._get_int_input("Ingrese el ID del Usuario")
        bedroom_id = self._get_int_input("Ingrese el ID de la Habitación")
        check_in_date = self._get_date_input("Ingrese la fecha de Check-in")
        check_out_date = self._get_date_input("Ingrese la fecha de Check-out")

        service_id = None

        self.booking_service.create_new_booking(
            user_id, bedroom_id, service_id, check_in_date, check_out_date, db
        )

    def view_all_bookings(self, db):
        """Muestra todas las reservas registradas."""
        print("\n--- Todas las Reservas ---")
        bookings = self.booking_service.get_all_bookings_list(db)
        if not bookings:
            print("No hay reservas registradas.")
            return
        for booking in bookings:
            print(booking) 
        print("------------------------")

    def find_booking_interactive(self, db):
        """Busca y muestra una reserva específica por ID."""
        print("\n--- Buscar Reserva por ID ---")
        booking_id = self._get_int_input("Ingrese el ID de la Reserva a buscar")
        booking = self.booking_service.get_booking_details(booking_id, db)
        if booking:
            print("Reserva encontrada:")
            print(booking)
        else:
            print(f"No se encontró ninguna reserva con el ID {booking_id}.")

    def cancel_booking_interactive(self, db):
        """Maneja la entrada para cancelar una reserva."""
        print("\n--- Cancelar Reserva ---")
        booking_id = self._get_int_input("Ingrese el ID de la Reserva a cancelar")

        booking = self.booking_service.get_booking_details(booking_id, db)
        if not booking:
            print(f"No se encontró ninguna reserva con el ID {booking_id}.")
            return
        if booking.status == 'cancelled':
             print(f"La reserva ID {booking_id} ya está cancelada.")
             return
        if booking.status == 'completed':
             print(f"La reserva ID {booking_id} ya está completada y no puede cancelarse.")
             return

        print("Reserva a cancelar:")
        print(booking)
        confirm = input("¿Está seguro que desea cancelar esta reserva? (s/N): ").lower()
        if confirm == 's':
            success = self.booking_service.cancel_booking(booking_id, db)
        else:
            print("Cancelación de reserva abortada.")