from repository.conexion.Conexion import Conexion
from domain.models.User import User

class UserRepository:
    def __init__(self):
        self.conexion = Conexion()

    def add_user(self, user):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "INSERT INTO users (user_id, username, password, employee_id) VALUES (%s, %s, %s, %s)"
            values = (user.user_id, user.username, user.password, user.employee_id) # ¡No olvides hashear la contraseña!
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            connection.rollback()
            return False
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def get_user_by_id(self, user_id):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "SELECT user_id, username, password, employee_id FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            if result:
                return User(result[0], result[1], result[2], result[3])
            return None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def get_user_by_username(self, username):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "SELECT user_id, username, password, employee_id FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result:
                return User(result[0], result[1], result[2], result[3])
            return None
        except Exception as e:
            print(f"Error al obtener usuario por nombre de usuario: {e}")
            return None
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def get_all_users(self):
        users = []
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "SELECT user_id, username, password, employee_id FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                users.append(User(result[0], result[1], result[2], result[3]))
            return users
        except Exception as e:
            print(f"Error al obtener todos los usuarios: {e}")
            return []
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def update_user(self, user):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "UPDATE users SET username = %s, password = %s, employee_id = %s WHERE user_id = %s"
            values = (user.username, user.password, user.employee_id, user.user_id) # ¡No olvides hashear la contraseña!
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            connection.rollback()
            return False
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)

    def delete_user(self, user_id):
        try:
            connection = self.conexion.get_connection()
            cursor = connection.cursor()
            sql = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            connection.rollback()
            return False
        finally:
            if connection:
                cursor.close()
                self.conexion.release_connection(connection)