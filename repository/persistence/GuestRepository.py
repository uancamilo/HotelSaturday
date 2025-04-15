

from domain.models.Guest import Guest



class GuestRepository:


    def __init__(self):
        self.guest = Guest


    def create_guest_repository(self, guest, db):
        query = "INSERT INTO guest (id,name,last_name,phone,email,password,status,origin,occupation) VALUES (%s, %s,%s,%s, %s, %s, %s,%s, %s)"
        values = (guest.id, guest.name, guest.last_name , guest.phone, guest.email , guest.password , guest.status , guest.origin , guest.occupation)
        db.execute_query(query , values)