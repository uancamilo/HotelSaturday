from domain.models.Booking import Booking
from decimal import Decimal 

class BookingRepository:

    def check_room_availability(self, bedroom_id, check_in, check_out, db, exclude_booking_id=None):
        """Verifica si una habitación está disponible en las fechas dadas, excluyendo opcionalmente una reserva."""
        query = """
            SELECT 1 FROM booking
            WHERE bedroom_id = %s
            AND status = 'confirmed'
            AND check_in < %s
            AND check_out > %s
        """
        values = [bedroom_id, check_out, check_in] 

        if exclude_booking_id is not None:
            query += " AND id != %s"
            values.append(exclude_booking_id)

        query += " LIMIT 1" 

        cursor = None
        try:
            cursor = db.execute_query(query, tuple(values))
            result = cursor.fetchone() if cursor else None
            return result is None 
        finally:
             pass

    def create_booking(self, booking, db):
        """Inserta una nueva reserva en la base de datos."""
        query = """
            INSERT INTO booking (user_id, bedroom_id, service_id, check_in, check_out, total_price, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            booking.user_id, booking.bedroom_id, booking.service_id,
            booking.check_in, booking.check_out,
            booking.total_price, booking.status
        )
        cursor = None
        try:
            cursor = db.execute_query(query, values)
            booking_id = cursor.lastrowid if cursor else None
            if booking_id:
                booking.id = booking_id
            print(f"Reserva ID {booking_id} creada correctamente.")
            return booking_id
        except Exception as e:
            print(f"Error al crear la reserva: {e}")
            return None

    def find_booking_by_id(self, booking_id, db):
        """Busca una reserva por ID, uniendo datos de usuario y habitación."""
        query = """
            SELECT
                b.id, b.user_id, b.bedroom_id, b.service_id, b.check_in, b.check_out,
                b.total_price, b.status,
                u.name AS user_name, u.last_name AS user_last_name,
                br.number AS bedroom_number
            FROM booking b
            JOIN user u ON b.user_id = u.id
            JOIN bedroom br ON b.bedroom_id = br.id
            WHERE b.id = %s
        """
        values = (booking_id,)
        cursor = None
        try:
            cursor = db.execute_query(query, values)
            result = cursor.fetchone() if cursor else None
            if result:
                booking_obj = Booking(
                    id=result[0], user_id=result[1], bedroom_id=result[2], service_id=result[3],
                    check_in=result[4], check_out=result[5], 
                    total_price=Decimal(result[6]), 
                    status=result[7]
                )
                booking_obj.user_name = f"{result[8]} {result[9]}"
                booking_obj.bedroom_number = result[10]
                return booking_obj
            return None
        finally:
            pass

    def get_all_bookings(self, db):
        """Obtiene todas las reservas con datos de usuario y habitación."""
        query = """
            SELECT
                b.id, b.user_id, b.bedroom_id, b.service_id, b.check_in, b.check_out,
                b.total_price, b.status,
                u.name AS user_name, u.last_name AS user_last_name,
                br.number AS bedroom_number
            FROM booking b
            JOIN user u ON b.user_id = u.id
            JOIN bedroom br ON b.bedroom_id = br.id
            ORDER BY b.check_in DESC, b.id DESC
        """
        bookings = []
        cursor = None
        try:
            cursor = db.execute_query(query)
            results = cursor.fetchall() if cursor else []
            for row in results:
                 booking_obj = Booking(
                    id=row[0], user_id=row[1], bedroom_id=row[2], service_id=row[3],
                    check_in=row[4], check_out=row[5],
                    total_price=Decimal(row[6]), status=row[7]
                 )
                 booking_obj.user_name = f"{row[8]} {row[9]}"
                 booking_obj.bedroom_number = row[10]
                 bookings.append(booking_obj)
            return bookings
        finally:
            pass

    def update_booking_status(self, booking_id, new_status, db):
        """Actualiza el estado de una reserva (ej. para cancelar)."""
        allowed_statuses = ['confirmed', 'cancelled', 'completed']
        if new_status not in allowed_statuses:
            print(f"Error: Estado '{new_status}' no válido.")
            return False

        query = "UPDATE booking SET status = %s WHERE id = %s"
        values = (new_status, booking_id)
        try:
            db.execute_query(query, values)
            print(f"Estado de la reserva ID {booking_id} actualizado a '{new_status}'.")
            return True
        except Exception as e:
            print(f"Error al actualizar estado de la reserva ID {booking_id}: {e}")
            return False