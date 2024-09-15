from .abc import Command
from data import DataBase, Tag, Note

from sqlalchemy import select

from datetime import datetime


class Create(Command):
    def __init__(self, db: DataBase, content: str, tags: list[str]) -> None:
        self.db = db
        self.content = content
        self.tags = tags

    def execute(self) -> None:
        with self.db.session() as session:
            tags = []
            for tag in self.tags:
                existing = session.scalars(
                    select(Tag).where(Tag.name == tag)
                ).one_or_none()

                if existing is None:
                    existing = Tag(name=tag)
                    session.add(
                        existing
                    )
                tags.append(existing)

            note = Note(
                text=self.content,
                created=datetime.now()
            )
            note.tags.extend(tags)
            session.add(note)
            session.commit()




