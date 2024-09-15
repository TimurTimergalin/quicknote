from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models import Base


class DataBase:
    def __init__(self, path: str) -> None:
        self.engine = create_engine(path)
        Base.metadata.create_all(self.engine)

    def session(self) -> Session:
        return Session(self.engine)
