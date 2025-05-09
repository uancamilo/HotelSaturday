import re
from domain.models.Employee import Employee
from domain.models.Person import Person
from repository.persistence.EmployeeRepository import EmployeeRepository

class EmployeeInput:

    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def register(self, db, rol):
        print("\n--- Registro de Nuevo Empleado ---")

        # Capturar ID (debe ser un número)
        while True:
            id_input = input("Cédula del empleado: ").strip()
            if id_input.isdigit():
                id = int(id_input)
                break
            else:
                print("❌ La cédula debe ser numérica.")

        # Capturar nombre
        name = input("Nombre del empleado: ").strip()

        # Capturar apellido
        last_name = input("Apellido del empleado: ").strip()

        # Capturar teléfono
        phone = input("Teléfono del empleado: ").strip()

        # Capturar email validado
        while True:
            email = input("Correo electrónico del empleado: ").strip()
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                break
            else:
                print("❌ Formato de correo inválido. Intente nuevamente.")

        # Capturar contraseña
        while True:
             password = input("Contraseña del empleado: ").strip()
    
             if re.fullmatch(r"(?=.*[A-Za-z])(?=(?:.*\d){5})[A-Za-z\d]+", password):
                break
             else:
                print("❌ La contraseña debe tener exactamente 5 números y al menos 1 letra.")
           
        # Capturar estado
        while True:
            status_input = input("¿Estado del empleado? (active/inactive) [default: active]: ").strip().lower()
            if status_input in ("active", "inactive", ""):
                status = "active" if status_input == "" else status_input
                break
            else:
                print("❌ Estado inválido. Use 'active' o 'inactive'.")

        # Crear el objeto Person
        person = Person(
            id=id,
            name=name,
            last_name=last_name,
            phone=phone,
            email=email
        )

        # Crear el objeto Employee
        employee = Employee(
            person=person,
            password=password,
            rol=rol,  # 🔥 Aquí sí usamos el rol que recibimos
            status=status
        )

        # Guardar en la base de datos
        self.employee_repository.create_employee_repository(employee, db)

