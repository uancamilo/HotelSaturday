from repository.persistence.EmployeeRepository import EmployeeRepository
from domain.models.Employee import Employee

class EmployeeService:
    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def add_employee(self, employee_id, name, email, role):
        employee = Employee(employee_id, name, email, role)
        return self.employee_repository.add_employee(employee)

    def get_employee_by_id(self, employee_id):
        return self.employee_repository.get_employee_by_id(employee_id)

    def get_all_employees(self):
        return self.employee_repository.get_all_employees()

    def update_employee(self, employee_id, name, email, role):
        employee = Employee(employee_id, name, email, role)
        return self.employee_repository.update_employee(employee)

    def delete_employee(self, employee_id):
        return self.employee_repository.delete_employee(employee_id)