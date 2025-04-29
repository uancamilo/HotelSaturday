from domain.models.Person import Person

class Employee:

    def __init__(self, person, password, rol, status):
        self._person = person
        self._password = password
        self._rol = rol
        self._status = status

    # Getter y Setter para person
    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = person

    # Getter y Setter para password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    # Getter y Setter para rol
    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    # Getter y Setter para status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
