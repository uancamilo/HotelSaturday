

from domain.service.GuestService import GuestService

class GuestInput:


    def __init__(self):
        self.guest_service = GuestService()


    def register(self):
        id = int(input("Ingrese su documento de identidad"))
        self.guest_service.register_data.append(id)
        name = input("Ingrese su nombre")
        self.guest_service.register_data.append(name)
        last_name = input("Ingrese su apellido")
        self.guest_service.register_data.append(last_name)
        phone = input("Ingrese su teléfono")
        self.guest_service.register_data.append(phone)
        email = input("Ingrese su correo")
        self.guest_service.register_data.append(email)
        password = input("Ingrese su contraseña")
        self.guest_service.register_data.append(password)
        status = input("Seleccione el estado")
        self.guest_service.register_data.append(status)


    def print_data(self):
        self.guest_service.print_data_service()




