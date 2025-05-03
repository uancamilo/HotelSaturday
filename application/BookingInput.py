from domain.models.Booking import Booking
from application.BookingService import BookingService
import re

class BookingInput:

    def __init__(self):
        self.booking_service = BookingService()

    def create_booking_interactive(self, db):
        print("\n--- Crear Nueva Reserva ---")

        date_pattern = r"^\d{4}-\d{2}-\d{2}$"

        try:
            user_id = int(input("ID del huésped: ").strip())
            bedroom_id = int(input("ID de la habitación: ").strip())
            check_in = input("Fecha de check-in (YYYY-MM-DD): ").strip()
            if not re.match(date_pattern, check_in):
                print("❌ El formato de la fecha debe ser YYYY-MM-DD.")
                return
            check_out = input("Fecha de check-out (YYYY-MM-DD): ").strip()
            if not re.match(date_pattern, check_out):
                print("❌ El formato de la fecha debe ser YYYY-MM-DD.")
                return

            price_input = input("Precio total (COP): ").strip()
            if not re.match(r"^\d+(\.\d{1,2})?$", price_input):
                print("❌ El precio debe ser un número válido (solo dígitos y opcionalmente decimales).")
                return
            total_price = float(price_input)


            services = []
            while True:
                add_service = input("¿Desea agregar un servicio adicional? (s/n): ").strip().lower()
                if add_service == "s":
                    try:
                        service_id = int(input("ID del servicio a agregar: ").strip())
                        services.append(service_id)
                    except ValueError:
                        print("❌ El ID del servicio debe ser numérico.")
                elif add_service == "n":
                    break
                else:
                    print("❌ Opción inválida. Responda 's' o 'n'.")

            # Crear el objeto Booking
            booking = Booking(
                id=None,
                user_id=user_id,
                bedroom_id=bedroom_id,
                check_in=check_in,
                check_out=check_out,
                total_price=total_price,
                status="confirmed",
                services=services
            )

            success = self.booking_service.create_booking_service(booking, db)
            if success:
                print("✅ Reserva creada exitosamente.")
        except ValueError:
            print("❌ Entrada inválida. Verifique los datos.")

    def view_all_bookings(self, db):
        print("\n--- Listado de Reservas ---")
        self.booking_service.list_all_bookings_service(db)

    def find_booking_interactive(self, db):
        print("\n--- Buscar Reserva por ID ---")
        try:
            booking_id = int(input("Ingrese el ID de la reserva: ").strip())
            self.booking_service.find_booking_by_id_service(booking_id, db)
        except ValueError:
            print("❌ El ID debe ser un número.")

    def cancel_booking_interactive(self, db):
        print("\n--- Cancelar Reserva ---")
        try:
            booking_id = int(input("Ingrese el ID de la reserva a cancelar: ").strip())
            success = self.booking_service.cancel_booking_service(booking_id, db)
            if success:
                print("✅ Reserva cancelada exitosamente.")
        except ValueError:
            print("❌ El ID debe ser un número.")
