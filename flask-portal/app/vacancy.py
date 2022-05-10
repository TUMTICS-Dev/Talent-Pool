from datetime import datetime
from app.db_model import DB_Model

class Vacancy(DB_Model):

    Id: int
    Company: str
    Title: str
    Description: str
    Referrer: int
    CreatedTime: datetime
    ModifiedTime: datetime

    def __init__(self):
        # TODO
        pass

    def all(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

    def exists(self):
        # TODO
        pass

    def fetch(self):
        # TODO
        pass

    def first(self):
        # TODO
        pass

    def save(self):
        # TODO
        pass
    