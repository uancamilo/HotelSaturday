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

    def listar_huespedes(self, db):
        query = """
            SELECT u.id, u.name, u.last_name, u.phone, u.email, g.origin, g.occupation
            FROM user u
            INNER JOIN guest g ON u.id = g.id
        """
        resultados = db.execute_query(query)

        if not resultados:
            print("No hay huéspedes registrados.")
        else:
            print("Lista de huéspedes:")
            for r in resultados:
                print(
                    f"Cédula: {r[0]}, Nombre: {r[1]} {r[2]}, Tel: {r[3]}, Email: {r[4]}, Origen: {r[5]}, Ocupación: {r[6]}")
