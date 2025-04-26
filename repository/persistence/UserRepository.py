class UserRepository:

    def check_user_exists(self, user_id, db):
        """Verifica si un usuario existe en la tabla 'user' por su ID."""
        query = "SELECT 1 FROM user WHERE id = %s LIMIT 1"
        values = (user_id,)
        cursor = None
        try:
            cursor = db.execute_query(query, values)
            result = cursor.fetchone() if cursor else None
            return result is not None
        except Exception as e:
            print(f"Error al verificar existencia del usuario ID {user_id}: {e}")
            return False 