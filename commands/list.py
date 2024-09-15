from datetime import datetime

from sqlalchemy import select

from data import DataBase, Note, NoteToTag
from .abc import Command


def format_note(note: Note):
    return (
        f"{note.id}.\n" +
        note.created.strftime("Created at %d-%m-%Y %H:%M") + "\n" +
        " ".join(f"[{x.tag_name}]" for x in note.tags) + "\n" +
        note.text
    )


class List(Command):
    def __init__(self, db: DataBase, tags: list[str] | None = None, since: datetime | None = None,
                 until: datetime | None = None):
        self.until = until
        self.since = since
        self.tags = tags
        self.db = db

    def execute(self) -> None:
        with self.db.session() as session:
            if self.tags is not None:
                stmt = (
                    select(Note)
                    .distinct()
                    .join(NoteToTag)
                    .where(NoteToTag.tag_name.in_(self.tags))
                )
            else:
                stmt = select(Note)

            if self.since is not None:
                stmt = stmt.where(Note.created >= self.since)

            if self.until is not None:
                stmt = stmt.where(Note.created <= self.until)

            stmt = stmt.order_by(Note.created.desc())

            for note in session.scalars(stmt).all():
                print(format_note(note), end="\n\n")
