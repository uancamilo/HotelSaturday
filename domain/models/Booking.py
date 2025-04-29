class Booking:

    def __init__(self, id=None, user_id=None, bedroom_id=None, services=None, check_in=None, check_out=None, total_price=0.0, status="confirmed"):
        self._id = id
        self._user_id = user_id
        self._bedroom_id = bedroom_id
        self._services = services if services is not None else []
        self._check_in = check_in
        self._check_out = check_out
        self._total_price = total_price
        self._status = status

    # Getters and Setters

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def bedroom_id(self):
        return self._bedroom_id

    @bedroom_id.setter
    def bedroom_id(self, bedroom_id):
        self._bedroom_id = bedroom_id

    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, services):
        self._services = services

    @property
    def check_in(self):
        return self._check_in

    @check_in.setter
    def check_in(self, check_in):
        self._check_in = check_in

    @property
    def check_out(self):
        return self._check_out

    @check_out.setter
    def check_out(self, check_out):
        self._check_out = check_out

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        self._total_price = total_price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
