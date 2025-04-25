class Bedroom:
    def __init__(self, number, bedroom_type, price, status=True):
        self.number = number
        self.bedroom_type = bedroom_type
        self.price = price
        self.status = status

    @property
    def get_number(self):
        return self.number

    @property
    def get_bedroom_type(self):
        return self.bedroom_type

    @property
    def get_price(self):
        return self.price

    def mark_status(self, status):
        self.status = status

    def __str__(self):
        availability = "Disponible" if self.status else "No disponible"
        return f"Número {self.number}, Tipo: {self.bedroom_type}, Precio: ${self.price}, Estado: {availability}"
