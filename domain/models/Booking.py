import datetime

class Booking:
    def __init__(self, id, user_id, bedroom_id, service_id, check_in, check_out, total_price, status):
        """
        Inicializa un objeto Reserva (Booking).
        Args:
            id (int | None): ID de la reserva (None si es nueva).
            user_id (int): ID del usuario que reserva.
            bedroom_id (int): ID de la habitación reservada.
            service_id (int | None): ID del servicio adicional (opcional).
            check_in (datetime.date): Fecha de entrada.
            check_out (datetime.date): Fecha de salida.
            total_price (float | decimal.Decimal): Precio total calculado.
            status (str): Estado ('confirmed', 'cancelled', 'completed').
        """
        self._id = id
        self.user_id = user_id
        self.bedroom_id = bedroom_id
        self.service_id = service_id
        self.check_in = check_in
        self.check_out = check_out
        self.total_price = total_price
        self.status = status
        self.user_name = None
        self.bedroom_number = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
         if value is not None and not isinstance(value, int):
             raise ValueError("El ID de la reserva debe ser un entero o None.")
         self._id = value

    def __str__(self):
        """Representación en string de la Reserva."""
        check_in_str = self.check_in.strftime('%Y-%m-%d') if isinstance(self.check_in, datetime.date) else str(self.check_in)
        check_out_str = self.check_out.strftime('%Y-%m-%d') if isinstance(self.check_out, datetime.date) else str(self.check_out)

        user_info = f"(Usuario ID: {self.user_id})"
        if self.user_name:
            user_info = f"(Usuario: {self.user_name})"

        bedroom_info = f"(Habitación ID: {self.bedroom_id})"
        if self.bedroom_number:
            bedroom_info = f"(Habitación: {self.bedroom_number})"

        service_info = f", Servicio ID: {self.service_id}" if self.service_id else ""

        return (f"Reserva ID: {self.id if self.id else 'N/A'} {user_info} {bedroom_info}{service_info} | "
                f"Check-in: {check_in_str}, Check-out: {check_out_str} | "
                f"Precio: ${self.total_price:,.2f}, Estado: {self.status.upper()}")