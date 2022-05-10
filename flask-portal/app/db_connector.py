import os
from pyairtable import Table, Base, Api
from abc import ABC, abstractmethod

class DB_Connector(ABC):
    @abstractmethod
    def Get_Api(self):
        pass

    @abstractmethod
    def Get_Base(self):
        pass

    @abstractmethod
    def Get_Table(self, table_name: str):
        pass

class PyAirtable_DB_Connector(DB_Connector):
    def __init__(self):
        self.api_key = os.environ['AIRTABLE_API_KEY']
        self.base_id = os.environ['AIRTABLE_BASE_ID']

    def Get_Api(self):
        return Api(self.api_key)

    def Get_Base(self):
        return Base(self.api_key, self.base_id)

    def Get_Table(self, table_name: str):
        return Table(self.api_key, self.base_id, table_name)

# class DB_2(DB_operator):
#     def __init__(self):
#         self.api_key = os.environ['AIRTABLE_API_KEY']
#         self.base_id = os.environ['AIRTABLE_BASE_ID']
#         self.base = Base(self.api_key, self.base_id)

#     def get_base(self):
#         return self.base

#     def get_table(self, table_name: str):
#         self.table = Table(self.api_key, self.base_id, table_name)
#         return self.table

# class UseDB():
#     def usedb(db_operator: DB_operator):
#         return db_operator.get_base()

# db1 = DB_1()
# db2 = DB_2()
# UseDB().usedb(db1)