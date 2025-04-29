class SecurityService:

    def __init__(self, db):
        self.db = db

    def ensure_initial_users(self):
        """Verifica si existen usuarios iniciales (Superadmin y Employee), si no los crea."""

        # Verificar si existe Superadmin
        query_superadmin = "SELECT COUNT(*) FROM employee WHERE rol = 'superadmin'"
        result_superadmin = self.db.execute_query(query_superadmin)

        if result_superadmin and result_superadmin[0][0] == 0:
            self.create_superadmin()

        # Verificar si existe al menos un empleado normal
        query_employee = "SELECT COUNT(*) FROM employee WHERE rol = 'employee'"
        result_employee = self.db.execute_query(query_employee)

        if result_employee and result_employee[0][0] == 0:
            self.create_employee()

    def create_superadmin(self):
        """Crea automáticamente un Superadmin inicial."""
        print("\n⚡ No se encontró ningún Superadmin. Creando uno automáticamente...")

        insert_person = """
            INSERT INTO person (id, name, last_name, phone, email)
            VALUES (%s, %s, %s, %s, %s)
        """
        person_values = (1, "Super", "Admin", "3000000000", "superadmin@hotel.com")
        self.db.execute_query(insert_person, person_values)

        insert_employee = """
            INSERT INTO employee (id, password, rol, status)
            VALUES (%s, %s, %s, %s)
        """
        employee_values = (1, "admin123", "superadmin", "active")
        self.db.execute_query(insert_employee, employee_values)

        print("✅ Superadmin creado exitosamente.")

    def create_employee(self):
        """Crea automáticamente un Empleado de prueba inicial."""
        print("\n⚡ No se encontró ningún Empleado normal. Creando uno automáticamente...")

        insert_person = """
            INSERT INTO person (id, name, last_name, phone, email)
            VALUES (%s, %s, %s, %s, %s)
        """
        person_values = (2, "Empleado", "Normal", "3010000000", "empleado@hotel.com")
        self.db.execute_query(insert_person, person_values)

        insert_employee = """
            INSERT INTO employee (id, password, rol, status)
            VALUES (%s, %s, %s, %s)
        """
        employee_values = (2, "empleado123", "employee", "active")
        self.db.execute_query(insert_employee, employee_values)

        print("✅ Empleado normal creado exitosamente.")
