from application.BedroomService import BedroomService
from domain.models.Bedroom import Bedroom
from repository.persistence.BedroomRepository import BedroomRepository

class BedroomInput:
    def __init__(self):
        self.bedroom = Bedroom(None, None, None)
        self.bedroom_repository = BedroomRepository()
        self.bedroom_service = BedroomService()

    def create_bedroom(self, db):
        number = input("Ingrese su número de habitación: ")
        self.bedroom.number = number

        bedroom_type = input("Ingrese tipo de habitación: ")
        self.bedroom.bedroom_type = bedroom_type

        price = input("Ingrese el precio de la habitación: ")
        self.bedroom.price = float(price)

        available = input("¿Está disponible? (Sí/No): ")
        self.bedroom.available = True if available.lower() == 'sí' else False

        self.bedroom_repository.create_bedroom(self.bedroom, db)
        print(f"Habicación {self.bedroom.number} registrada correctamente.")

    def list_bedrooms(self, db):
        self.bedroom_service.print_all_rooms()

    def print_data(self):
        self.bedroom_service.print_all_rooms()
