from repository.persistence.UserRepository import UserRepository
from domain.models.User import User

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def add_user(self, user_id, username, password, employee_id=None):
        user = User(user_id, username, password, employee_id)
        return self.user_repository.add_user(user)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_username(self, username):
        return self.user_repository.get_user_by_username(username)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, username, password, employee_id=None):
        user = User(user_id, username, password, employee_id)
        return self.user_repository.update_user(user)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)