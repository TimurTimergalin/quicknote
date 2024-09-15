from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class NotesToTags(Base):
    __tablename__ = "notes_to_tags"
    note_id: Mapped[int] = mapped_column(ForeignKey("notes.id"), primary_key=True)
    tag_name: Mapped[str] = mapped_column(ForeignKey("tags.name"), primary_key=True)

    note: Mapped["Note"] = relationship(back_populates="tags")
    tag: Mapped["Tag"] = relationship(back_populates="notes")


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    text: Mapped[str]
    created: Mapped[datetime] = mapped_column(index=True)
    tags: Mapped[list["NotesToTags"]] = relationship(back_populates="note")


class Tag(Base):
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(primary_key=True, index=True)
    notes: Mapped[list["NotesToTags"]] = relationship(back_populates="tag")


__all__ = [
    "Base",
    "Note",
    "Tag",
    "NotesToTags"
]
