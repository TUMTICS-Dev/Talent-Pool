import os
from pyairtable import Table
from abc import ABC

class DB(ABC):
    def __init__(self):
        self.api_key = os.environ['AIRTABLE_API_KEY']

    def get_table(self):
        self.table = Table(self.api_key, 'appRCVEoTuhuY9MEo', 'TUM-Students')
        return self.table.all()