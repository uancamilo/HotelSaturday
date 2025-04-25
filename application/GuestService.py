from domain.models.Guest import Guest
from repository.persistence.GuestRepository import GuestRepository

class GuestService:

    register_data = []

    def __init__(self):
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.repo = GuestRepository()

    def createGuest(self, guest):
        guest.id = self.register_data[0]
        guest.name = self.register_data[1]
        guest.last_name = self.register_data[2]
        guest.phone = self.register_data[3]
        guest.email = self.register_data[4]
        guest.password = self.register_data[5]
        guest.status = self.register_data[6]

    def listar_huespedes(self, db):
        self.repo.listar_huespedes(db)

    def print_data_service(self):
        for data in self.register_data:
            print(data)
