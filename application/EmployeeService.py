from domain.models.Employee import Employee
from domain.models.Person import Person
from repository.persistence.EmployeeRepository import EmployeeRepository

class EmployeeService:

    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def find_employee_by_email(self, email, db):
        """Busca un empleado por su email usando el repositorio."""
        result = self.employee_repository.find_by_email(email, db)

        if result:
            data = result[0]
            person = Person(
                id=data[0],
                name=data[1],
                last_name=data[2],
                phone=data[3],
                email=data[4]
            )
            employee = Employee(
                person=person,
                password=data[5],
                rol=data[6],
                status=data[7]
            )
            return employee
        else:
            return None

    def validate_login(self, email, password, db):
        """Valida las credenciales de login."""
        employee = self.find_employee_by_email(email, db)
        if employee and employee.password == password:
            return employee
        else:
            return None
