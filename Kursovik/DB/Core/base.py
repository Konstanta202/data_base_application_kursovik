from typing import Annotated
from sqlalchemy import MetaData, String
from sqlalchemy.orm import DeclarativeBase

metadata_obj = MetaData()
str_256 = Annotated[str,256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if hasattr(self, "repr_cols") and col in self.repr_cols:
                cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__}({', '.join(cols)})>"
