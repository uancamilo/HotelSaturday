from domain.models.Bedroom import Bedroom

class BedroomRepository:
    def __init__(self):
        self.bedroom = Bedroom

    def create_bedroom(self, bedroom, db):
        query = "INSERT INTO bedroom (number, bedroom_type, price, status) VALUES (%s, %s, %s, %s)"
        values = (bedroom.number, bedroom.bedroom_type, bedroom.price, bedroom.status)
        db.execute_query(query, values)

    def list_bedrooms(self, db):
        query = "SELECT id, number, bedroom_type, price, status FROM bedroom"
        results = db.execute_query(query)
        return results