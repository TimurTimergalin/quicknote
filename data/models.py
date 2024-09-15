from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship

from datetime import datetime


class Base(DeclarativeBase):
    pass


notes_to_tags = Table(
    "notes_to_tags",
    Base.metadata,
    Column("note_id", ForeignKey("notes.id")),
    Column("tag", ForeignKey("tags.name"))
)


class Note:
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    text: Mapped[str]
    created: Mapped[datetime] = mapped_column(index=True)
    tags: Mapped[list["Tag"]] = relationship(secondary=notes_to_tags)


class Tag:
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(primary_key=True, index=True)
    notes: Mapped[list["Note"]] = relationship(secondary=notes_to_tags)


__all__ = [
    "Base",
    "Note",
    "Tag"
]
