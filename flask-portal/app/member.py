from datetime import datetime
from app.db_model import DB_Model

class Member(DB_Model):

    Id: int
    FirstName: str
    LastName: str
    School: str
    JobTitle: str
    Major: str
    JobTitle: str
    IsReferrer: bool
    Email: str
    LinkedIn: str
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
    