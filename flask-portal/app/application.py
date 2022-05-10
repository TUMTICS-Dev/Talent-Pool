from datetime import datetime
from app.db_model import DB_Model
from app.member import Member
from app.vacancy import Vacancy

class Application(DB_Model):

    Id: int
    Member: Member
    vacancy: Vacancy
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
    