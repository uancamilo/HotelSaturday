class Person:

    def __init__(self, id, name, last_name, phone, email):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._email = email

    # Getter y Setter para ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # Getter y Setter para Nombre
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # Getter y Setter para Apellido
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    # Getter y Setter para Teléfono
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    # Getter y Setter para Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
