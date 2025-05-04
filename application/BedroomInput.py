import re
from repository.persistence.BedroomRepository import BedroomRepository
from domain.models.Bedroom import Bedroom 

class BedroomInput:

    def __init__(self):
        self.bedroom_repository = BedroomRepository()

    def create_bedroom(self, db):
        print("\n--- Crear Nueva Habitación ---")

        while True:
            number = input("Número de habitación: ").strip()
            if re.match(r'^\d+$', number):
                break
            else:
                print("❌ El número de habitación debe contener solo dígitos.")

        while True:
            print("Tipo de habitación:")
            print("1. Single")
            print("2. Double")
            print("3. Suite")
            tipo_input = input("Seleccione el tipo de habitación (1-3): ").strip()

            if tipo_input == "1":
                bedroom_type = "single"
                break
            elif tipo_input == "2":
                bedroom_type = "double"
                break
            elif tipo_input == "3":
                bedroom_type = "suite"
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")

        while True:
            price_input = input("Precio por noche (COP): ").strip()
            if re.match(r'^\d+(\.\d{1,2})?$', price_input):
                price = float(price_input)
                break
            else:
                print("❌ El precio debe ser un número válido (puede incluir decimales).")

        bedroom = Bedroom(number=number, bedroom_type=bedroom_type, price=price) 

        self.bedroom_repository.create_bedroom(bedroom, db) 
        print("✅ Habitación registrada correctamente.")

    def list_bedrooms(self, db):
        print("\n--- Listado de Habitaciones ---")
        results = self.bedroom_repository.list_bedrooms(db)

        if not results:
            print("⚠️ No hay habitaciones registradas.")
        else:
            for r in results:
                print(f"[ID: {r[0]}] Habitación {r[1]} - Tipo: {r[2]} - Precio: {r[3]:,.0f} - Estado: {r[4]}")