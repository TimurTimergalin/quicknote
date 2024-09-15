from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models import Base


class DataBase:
    def __init__(self, path):
        self.engine = create_engine(path)
        Base.metadata.create_all(self.engine)

    def session(self):
        return Session(self.engine)
