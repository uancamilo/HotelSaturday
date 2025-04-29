from domain.models.Guest import Guest
from domain.models.Person import Person
from repository.persistence.GuestRepository import GuestRepository

class GuestService:

    register_data = []

    def __init__(self):
        self.repo = GuestRepository()

    def createGuest(self):
        # Crear el objeto Person
        person = Person(
            id=self.register_data[0],
            name=self.register_data[1],
            last_name=self.register_data[2],
            phone=self.register_data[3],
            email=self.register_data[4]
        )

        # Crear el objeto Guest
        guest = Guest(
            person=person,
            origin=self.register_data[5],   # Ciudad de origen
            occupation=self.register_data[6] # Ocupación
        )

        return guest  # Devolvemos el Guest creado

    def listar_huespedes(self, db):
        self.repo.listar_huespedes(db)

    def print_data_service(self):
        for data in self.register_data:
            print(data)
