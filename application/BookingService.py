from domain.models.Booking import Booking
from repository.persistence.BookingRepository import BookingRepository

class BookingService:

    def __init__(self):
        self.booking_repository = BookingRepository()

    def create_booking_service(self, booking, db):
        """Lógica para crear una reserva."""
        if booking.check_in >= booking.check_out:
            print("❌ La fecha de check-out debe ser posterior a la fecha de check-in.")
            return False

        if self.booking_repository.is_bedroom_reserved(booking.bedroom_id, booking.check_in, booking.check_out, db):
            print("❌ La habitación ya está reservada en las fechas seleccionadas.")
            return False

        self.booking_repository.create_booking(booking, db)
        return True

    def list_all_bookings_service(self, db):
        """Lógica para listar todas las reservas."""
        bookings = self.booking_repository.list_all_bookings(db)
        if not bookings:
            print("⚠️ No hay reservas registradas.")
        else:
            for b in bookings:
                print(f"[ID: {b[0]}] Huesped ID: {b[1]}, Habitación ID: {b[2]}, "
                      f"Check-in: {b[3]}, Check-out: {b[4]}, Total: {b[5]:,.0f} COP, Estado: {b[6]}")

    def find_booking_by_id_service(self, booking_id, db):
        """Lógica para buscar una reserva por su ID."""
        booking = self.booking_repository.find_booking_by_id(booking_id, db)
        if booking:
            print(f"\n[Reserva ID: {booking[0]}] Huesped ID: {booking[1]}, Habitación ID: {booking[2]}, "
                  f"Check-in: {booking[3]}, Check-out: {booking[4]}, Total: {booking[5]:,.0f} COP, Estado: {booking[6]}")
        else:
            print("⚠️ Reserva no encontrada.")

    def cancel_booking_service(self, booking_id, db):
        """Lógica para cancelar una reserva."""
        booking = self.booking_repository.find_booking_by_id(booking_id, db)
        if not booking:
            print("⚠️ No se encontró la reserva especificada.")
            return False

        if booking[6] == "cancelled":
            print("⚠️ La reserva ya estaba cancelada previamente.")
            return False

        self.booking_repository.cancel_booking(booking_id, db)
        return True
