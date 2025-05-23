from domain.models.Person import Person

class Guest:

    def __init__(self, person=None, origin=None, occupation=None):
        self.person = person
        self.origin = origin
        self.occupation = occupation

    # Getter y Setter para person
    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = person

    # Getter y Setter para origin
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    # Getter y Setter para occupation
    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation
