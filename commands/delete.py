from .abc import Command
from data import DataBase, Note, NoteToTag

from sqlalchemy import delete

from datetime import datetime


class Delete(Command):
    def __init__(self, db: DataBase, ids: list[int] | None = None):
        self.ids = ids
        self.db = db

    def execute(self) -> None:
        with self.db.session() as session:
            stmt = delete(Note)
            if self.ids is not None:
                stmt = stmt.where(
                    Note.id.in_(self.ids)
                )

            deleted = session.execute(stmt)
            if self.ids is not None:
                print("Are you sure you want to delete specified notes? (y/[n])", end=" ")
            else:
                print("Are you sure you want to delete ALL the notes? (y/[n]", end=" ")
            ans = input()
            if ans == "y":
                session.commit()
                print(f"{deleted} Notes were successfully deleted")
            else:
                print("Deletion cancelled")
