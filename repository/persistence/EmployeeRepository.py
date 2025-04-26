from repository.conexion.Conexion import Conexion
from domain.models.Employee import Employee

class EmployeeRepository:
    def __init__(self):
        self.conexion = Conexion()

    def add_employee(self, employee):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "INSERT INTO employees (employee_id, name, email, role) VALUES (%s, %s, %s, %s)"
            values = (employee.employee_id, employee.name, employee.email, employee.role)
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al agregar empleado: {e}")
            connection.rollback()
            return False
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def get_employee_by_id(self, employee_id):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "SELECT employee_id, name, email, role FROM employees WHERE employee_id = %s"
            cursor.execute(sql, (employee_id,))
            result = cursor.fetchone()
            if result:
                return Employee(result[0], result[1], result[2], result[3])
            return None
        except Exception as e:
            print(f"Error al obtener empleado: {e}")
            return None
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def get_all_employees(self):
        employees = []
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "SELECT employee_id, name, email, role FROM employees"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                employees.append(Employee(result[0], result[1], result[2], result[3]))
            return employees
        except Exception as e:
            print(f"Error al obtener todos los empleados: {e}")
            return []
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def update_employee(self, employee):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "UPDATE employees SET name = %s, email = %s, role = %s WHERE employee_id = %s"
            values = (employee.name, employee.email, employee.role, employee.employee_id)
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            connection.rollback()
            return False
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def delete_employee(self, employee_id):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "DELETE FROM employees WHERE employee_id = %s"
            cursor.execute(sql, (employee_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            connection.rollback()
            return False
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)