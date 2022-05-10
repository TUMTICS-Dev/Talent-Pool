from abc import ABC, abstractmethod

class DB_Model(ABC):

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def exists(self):
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def save(self):
        pass