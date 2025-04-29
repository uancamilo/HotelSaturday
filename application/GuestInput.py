

from application.GuestService import GuestService
from domain.models.Guest import  Guest
from repository.persistence.GuestRepository import GuestRepository

class GuestInput:


    def __init__(self):
        self.guest = Guest(None,None,None,None ,None,None, None,None,None )
        self.guest_repository = GuestRepository()


    def register(self, db):
        id = int(input("Ingrese su documento de identidad: "))
        self.guest.id = id
        name = input("Ingrese su nombre: ")
        self.guest.name = name
        last_name = input("Ingrese su apellido: ")
        self.guest.last_name = last_name
        phone = input("Ingrese su teléfono: ")
        self.guest.phone = phone
        email = input("Ingrese su correo: ")
        self.guest.email = email
        password = input("Ingrese su contraseña: ")
        self.guest.password = password
        status = input("Seleccione el estado: ")
        self.guest.status = status
        origin = input("Ingrese su ciudad de origen: ")
        self.guest.origin = origin
        occupation = input("Ingrese su ocupacion: ")
        self.guest.occupation = occupation
        self.guest_repository.create_guest_repository(self.guest, db)



    def print_data(self):
        self.guest_service.print_data_service()