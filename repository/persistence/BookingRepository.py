from domain.models.Booking import Booking

class BookingRepository:

    def __init__(self):
        self.booking = Booking

    def create_booking(self, booking, db):
        """Crea una nueva reserva en la base de datos."""
        query = """
            INSERT INTO booking (user_id, bedroom_id, check_in, check_out, total_price, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            booking.user_id,
            booking.bedroom_id,
            booking.check_in,
            booking.check_out,
            booking.total_price,
            booking.status
        )
        db.execute_query(query, values)

        # Insertar los servicios asociados en booking_service
        if booking.services:
            for service_id in booking.services:
                query_service = """
                    INSERT INTO booking_service (booking_id, service_id)
                    VALUES (LAST_INSERT_ID(), %s)
                """
                db.execute_query(query_service, (service_id,))

        print("✅ Reserva creada exitosamente.")

    def list_all_bookings(self, db):
        """Lista todas las reservas registradas."""
        query = """
            SELECT id, user_id, bedroom_id, check_in, check_out, total_price, status
            FROM booking
        """
        results = db.execute_query(query)
        return results

    def find_booking_by_id(self, booking_id, db):
        """Busca una reserva por su ID."""
        query = """
            SELECT id, user_id, bedroom_id, check_in, check_out, total_price, status
            FROM booking
            WHERE id = %s
        """
        result = db.execute_query(query, (booking_id,))
        return result[0] if result else None

    def cancel_booking(self, booking_id, db):
        """Cancela una reserva existente cambiando su estado."""
        query = """
            UPDATE booking
            SET status = 'cancelled'
            WHERE id = %s
        """
        db.execute_query(query, (booking_id,))
        print("✅ Reserva cancelada correctamente.")

    def is_bedroom_reserved(self, bedroom_id, check_in, check_out, db):
        """Verifica si la habitación ya tiene una reserva activa en el rango de fechas."""
        query = """
            SELECT id FROM booking
            WHERE bedroom_id = %s
            AND status IN ('confirmed', 'completed')
            AND (
                (check_in <= %s AND check_out > %s) OR
                (check_in < %s AND check_out >= %s) OR
                (check_in >= %s AND check_out <= %s)
            )
        """
        params = (
            bedroom_id,
            check_in, check_in,
            check_out, check_out,
            check_in, check_out
        )
        result = db.execute_query(query, params)
        return bool(result)
