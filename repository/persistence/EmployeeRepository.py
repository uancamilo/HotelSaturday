from domain.models.Employee import Employee

class EmployeeRepository:

    def __init__(self):
        self.employee = Employee

    def create_employee_repository(self, employee, db):
        """ Crea un nuevo empleado registrándolo en las tablas person y employee """

        # Validar si el ID ya existe en person
        query_check_id = "SELECT id FROM person WHERE id = %s"
        result_id = db.execute_query(query_check_id, (employee.person.id,))
        if result_id:
            print(f"⚠️ Ya existe una persona con la cédula {employee.person.id}. Registro cancelado.")
            return

        # Validar si el email ya existe en person
        query_check_email = "SELECT email FROM person WHERE email = %s"
        result_email = db.execute_query(query_check_email, (employee.person.email,))
        if result_email:
            print(f"⚠️ Ya existe una persona con el correo {employee.person.email}. Registro cancelado.")
            return

        # Insertar en tabla person
        query_person = """
            INSERT INTO person (id, name, last_name, phone, email)
            VALUES (%s, %s, %s, %s, %s)
        """
        values_person = (
            employee.person.id,
            employee.person.name,
            employee.person.last_name,
            employee.person.phone,
            employee.person.email
        )
        db.execute_query(query_person, values_person)

        # Insertar en tabla employee
        query_employee = """
            INSERT INTO employee (id, password, rol, status)
            VALUES (%s, %s, %s, %s)
        """
        values_employee = (
            employee.person.id,
            employee.password,
            employee.rol,
            employee.status
        )
        db.execute_query(query_employee, values_employee)

        print("✅ Empleado registrado correctamente.")

    def find_by_email(self, email, db):
        """Busca un empleado por su email."""
        query = """
            SELECT 
                p.id, p.name, p.last_name, p.phone, p.email,
                e.password, e.rol, e.status
            FROM person p
            INNER JOIN employee e ON p.id = e.id
            WHERE p.email = %s
        """
        result = db.execute_query(query, (email,))
        return result
