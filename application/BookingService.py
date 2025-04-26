import datetime
from decimal import Decimal
from repository.persistence.BookingRepository import BookingRepository
from repository.persistence.BedroomRepository import BedroomRepository 
from repository.persistence.UserRepository import UserRepository
from domain.models.Booking import Booking

class BookingService:
    def __init__(self):
        self.booking_repository = BookingRepository()
        self.bedroom_repository = BedroomRepository()
        self.user_repository = UserRepository()    

    def check_availability_and_get_price(self, bedroom_id, check_in, check_out, db):
        """Verifica disponibilidad y obtiene precio por noche."""
        bedroom = self.bedroom_repository.find_bedroom_by_id(bedroom_id, db) 
        if not bedroom:
            print(f"Error: La habitación con ID {bedroom_id} no existe.")
            return None, False

        is_available = self.booking_repository.check_room_availability(bedroom_id, check_in, check_out, db)
        if not is_available:
            print(f"Error: La habitación {bedroom.number} no está disponible entre {check_in} y {check_out}.")
            return None, False

        return Decimal(bedroom.price), True 

    def create_new_booking(self, user_id, bedroom_id, service_id, check_in, check_out, db):
        """Crea una nueva reserva validando datos y disponibilidad."""
        if not isinstance(check_in, datetime.date) or not isinstance(check_out, datetime.date):
            print("Error: Las fechas deben ser objetos date válidos.")
            return None
        if check_out <= check_in:
            print("Error: La fecha de check-out debe ser posterior a la fecha de check-in.")
            return None

        if not self.user_repository.check_user_exists(user_id, db): 
             print(f"Error: El usuario con ID {user_id} no existe.")
             return None

        price_per_night, is_available = self.check_availability_and_get_price(bedroom_id, check_in, check_out, db)
        if not is_available:
            return None 
        
        num_nights = (check_out - check_in).days
        if num_nights <= 0: 
             print("Error: Número de noches inválido.")
             return None
        total_price = price_per_night * num_nights

        new_booking = Booking(
            id=None, user_id=user_id, bedroom_id=bedroom_id, service_id=service_id,
            check_in=check_in, check_out=check_out,
            total_price=total_price, status='confirmed'
        )
        booking_id = self.booking_repository.create_booking(new_booking, db)

        if booking_id:
            print(f"Reserva creada exitosamente. ID: {booking_id}, Precio Total: ${total_price:,.2f}")
            return new_booking 
        else:
            print("No se pudo crear la reserva en la base de datos.")
            return None

    def get_booking_details(self, booking_id, db):
        """Obtiene los detalles de una reserva por ID."""
        return self.booking_repository.find_booking_by_id(booking_id, db)

    def get_all_bookings_list(self, db):
        """Obtiene una lista de todas las reservas."""
        return self.booking_repository.get_all_bookings(db)

    def cancel_booking(self, booking_id, db):
        """Cancela una reserva cambiando su estado."""
    
        booking = self.get_booking_details(booking_id, db)
        if not booking:
            print(f"Error: No se encontró la reserva con ID {booking_id}.")
            return False
        if booking.status in ['cancelled', 'completed']:
            print(f"La reserva ID {booking_id} ya está {booking.status} y no puede ser cancelada de nuevo.")
            return False


        return self.booking_repository.update_booking_status(booking_id, 'cancelled', db)