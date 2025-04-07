
from domain.models.User import User


class Employee(User):

    def __init__(self, id, name , last_name,phone, email, password, status, rol):
        super.__init__(id, name , last_name,phone, email, password, status)
        self._rol = rol


    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol


    def __str__(self):
        return f"rol{self._rol}"
