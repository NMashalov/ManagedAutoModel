from sqlalchemy.orm import DeclarativeMeta, mapped_column, Mapped
from enum import Enum


class ModelSettings(Enum):
    user_table = 'user'
    model_table = 'models'


class AbstractDBManage:    
    pass

class Base(DeclarativeMeta):
    pass


class User(Base):
    __table__ = ModelSettings.user_table.value

    id: Mapped[int]  = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]


class Model(Base):
    __table__ = ModelSettings.model_table.value

    bucket_destination: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()


Base.metadata.create_all()

