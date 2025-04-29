from domain.models.Person import Person
from domain.models.Employee import Employee
from domain.models.Guest import Guest
from repository.persistence.EmployeeRepository import EmployeeRepository
from repository.persistence.GuestRepository import GuestRepository

class SeedData:

    def __init__(self, db):
        self.db = db
        self.employee_repo = EmployeeRepository()
        self.guest_repo = GuestRepository()

    def run(self):
        self._create_initial_employees()
        self._create_initial_guests()
        self._create_initial_bedrooms()
        self._create_initial_services()

    def _create_initial_employees(self):
        result = self.db.execute_query("SELECT COUNT(*) FROM employee")
        if result and result[0][0] == 0:
            print("✅ Insertando empleado Superadmin y Employee por defecto...")

            superadmin = Employee(
                person=Person(
                    id=9999,
                    name="Super",
                    last_name="Admin",
                    phone="9999999999",
                    email="super@admin.com"
                ),
                password="admin123",
                rol="superadmin",
                status="active"
            )

            employee = Employee(
                person=Person(
                    id=8888,
                    name="Empleado",
                    last_name="Demo",
                    phone="8888888888",
                    email="empleado@demo.com"
                ),
                password="demo123",
                rol="employee",
                status="active"
            )

            self.employee_repo.create_employee_repository(superadmin, self.db)
            self.employee_repo.create_employee_repository(employee, self.db)

    def _create_initial_guests(self):
        result = self.db.execute_query("SELECT COUNT(*) FROM guest")
        if result and result[0][0] == 0:
            print("✅ Insertando huésped de prueba...")

            # Crear primero el objeto Person
            person = Person(
                id=1001,
                name="Juan",
                last_name="Pérez",
                phone="1234567890",
                email="juan@correo.com"
            )

            # Crear ahora el objeto Guest, asignándole el Person
            guest = Guest(
                person=person,
                origin="Bogotá",
                occupation="Estudiante"
            )

            self.guest_repo.create_guest_repository(guest, self.db)

    def _create_initial_bedrooms(self):
        result = self.db.execute_query("SELECT COUNT(*) FROM bedroom")
        if result and result[0][0] == 0:
            print("✅ Insertando 3 habitaciones de prueba...")

            habitaciones = [
                ("101", "single", 150000),
                ("102", "double", 250000),
                ("103", "suite", 400000)
            ]

            for number, tipo, price in habitaciones:
                query = "INSERT INTO bedroom (number, bedroom_type, price) VALUES (%s, %s, %s)"
                self.db.execute_query(query, (number, tipo, price))

    def _create_initial_services(self):
        result = self.db.execute_query("SELECT COUNT(*) FROM services")
        if result and result[0][0] == 0:
            print("✅ Insertando 3 servicios de prueba...")

            servicios = [
                ("Desayuno", "Incluye desayuno buffet", 25000),
                ("Transporte", "Traslado aeropuerto-hotel", 50000),
                ("Spa", "Sesión de relajación de 1 hora", 120000)
            ]

            for nombre, descripcion, precio in servicios:
                query = "INSERT INTO services (name, description, price) VALUES (%s, %s, %s)"
                self.db.execute_query(query, (nombre, descripcion, precio))
