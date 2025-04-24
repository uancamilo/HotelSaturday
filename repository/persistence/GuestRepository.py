from domain.models.Guest import Guest

class GuestRepository:

    def __init__(self):
        self.guest = Guest

    def create_guest_repository(self, guest, db):
        query_user = """
            INSERT INTO user (id, name, last_name, phone, email, password, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values_user = (
            guest.id, guest.name, guest.last_name,
            guest.phone, guest.email, guest.password, guest.status
        )
        db.execute_query(query_user, values_user)

        query_guest = """
            INSERT INTO guest (id, origin, occupation)
            VALUES (%s, %s, %s)
        """
        values_guest = (guest.id, guest.origin, guest.occupation)
        db.execute_query(query_guest, values_guest)
