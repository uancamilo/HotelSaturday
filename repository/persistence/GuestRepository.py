from domain.models.Guest import Guest
from domain.models.Person import Person

class GuestRepository:

    def __init__(self):
        self.guest = Guest

    def create_guest_repository(self, guest, db):
        """ Crea un nuevo huésped registrándolo en las tablas person y guest """

        # Validar si el ID ya existe en person
        query_check_id = "SELECT id FROM person WHERE id = %s"
        result_id = db.execute_query(query_check_id, (guest.person.id,))
        if result_id:
            print(f"⚠️ Ya existe una persona con la cédula {guest.person.id}. Registro cancelado.")
            return

        # Validar si el email ya existe en person
        query_check_email = "SELECT email FROM person WHERE email = %s"
        result_email = db.execute_query(query_check_email, (guest.person.email,))
        if result_email:
            print(f"⚠️ Ya existe una persona con el correo {guest.person.email}. Registro cancelado.")
            return

        # Insertar en tabla person
        query_person = """
            INSERT INTO person (id, name, last_name, phone, email)
            VALUES (%s, %s, %s, %s, %s)
        """
        values_person = (
            guest.person.id,
            guest.person.name,
            guest.person.last_name,
            guest.person.phone,
            guest.person.email
        )
        db.execute_query(query_person, values_person)

        # Insertar en tabla guest
        query_guest = """
            INSERT INTO guest (id, origin, occupation)
            VALUES (%s, %s, %s)
        """
        values_guest = (
            guest.person.id,
            guest.origin,
            guest.occupation
        )
        db.execute_query(query_guest, values_guest)

        print("✅ Huésped registrado correctamente.")

    def listar_huespedes(self, db):
        """ Lista todos los huéspedes en formato ordenado """

        query = """
            SELECT p.id, p.name, p.last_name, p.phone, p.email, g.origin, g.occupation
            FROM person p
            INNER JOIN guest g ON p.id = g.id
        """
        resultados = db.execute_query(query)

        if not resultados:
            print("\n📭 No hay huéspedes registrados.")
            return

        print("\n📋 Lista de Huéspedes Registrados:\n")
        print("-" * 100)
        print(f"{'Cédula':<12} {'Nombre':<20} {'Teléfono':<15} {'Email':<25} {'Origen':<15} {'Ocupación':<15}")
        print("-" * 100)

        for r in resultados:
            cedula, nombre, apellido, telefono, email, origen, ocupacion = r
            nombre_completo = f"{nombre} {apellido}"
            print(f"{cedula:<12} {nombre_completo:<20} {telefono:<15} {email:<25} {origen:<15} {ocupacion:<15}")

        print("-" * 100)
        print(f"Total de huéspedes registrados: {len(resultados)}")
