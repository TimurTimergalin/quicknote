from .abc import Command
from data import DataBase, Tag

from sqlalchemy import select


class Tags(Command):
    def __init__(self, db: DataBase):
        self.db = db

    def execute(self) -> None:
        with self.db.session() as session:
            print("Tags present among your notes:")
            for tag in session.scalars(
                select(Tag)
            ).all():
                print(f"[{tag.name}]")
