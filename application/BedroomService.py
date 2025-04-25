from domain.models.Bedroom import Bedroom

class BedroomService:

    def __init__(self):
        self.registered_bedroom = []

    def create_bedroom(self, number, room_type, available):
        new_bedroom = Bedroom(number, room_type, available)
        self.registered_bedroom.append(new_bedroom)

    def book_bedroom(self, number):
        for bedroom in self.registered_bedroom:
            if bedroom.number == number:
                bedroom.mark_available(False)
                return True
        return False

    def print_all_bedrooms(self):
        for bedroom in self.registered_bedroom:
            print(f"Bedroom Number: {bedroom.number}, Type: {bedroom.room_type}, Available: {bedroom.available}")
