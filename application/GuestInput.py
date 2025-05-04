from domain.models.Guest import Guest
from domain.models.Person import Person
from repository.persistence.GuestRepository import GuestRepository
import re

class GuestInput:

    def __init__(self):
        self.guest_repository = GuestRepository()

    def register(self, db):
        print("\n--- Registro de Nuevo Huésped ---")

        # Capturar ID (debe ser un número)
        while True:
            id_input = input("Cédula del huésped: ").strip()
            if id_input.isdigit():
                id = int(id_input)
                break
            else:
                print("❌ La cédula debe ser numérica.")

        # Capturar nombre
        name = input("Nombre del huésped: ").strip()
        # Capturar apellido
        last_name = input("Apellido del huésped: ").strip()
        # Capturar teléfono
        while True:
            phone = input("Teléfono del huésped: ").strip()
            if re.match(r"^\d{7,10}$", phone):
                break
            else:
                print("❌ Teléfono inválido. Debe tener entre 7 y 10 dígitos.")

        # Capturar email con validación
        while True:
            email = input("Correo electrónico del huésped: ").strip()
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                break
            else:
                print("❌ Formato de correo inválido. Intente nuevamente.")

        # Capturar ciudad de origen
        origin = input("Ciudad de origen del huésped: ").strip()
        # Capturar ocupación
        occupation = input("Ocupación del huésped: ").strip()

        # Crear el objeto Person
        person = Person(
            id=id,
            name=name,
            last_name=last_name,
            phone=phone,
            email=email
        )

        # Crear el objeto Guest (anidando Person)
        guest = Guest(
            person=person,
            origin=origin,
            occupation=occupation
        )

        # Registrar en la base de datos
        self.guest_repository.create_guest_repository(guest, db)
