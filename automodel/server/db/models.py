from sqlalchemy.orm import DeclarativeMeta, mapped_column, Mapped


class AbstractDBManage:    
    pass

class Base(DeclarativeMeta):
    pass


class User(Base):
    __table__ = 'user'

    user: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()


class Model(Base):
    __table__ = 'models'

    user: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

