from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import create_engine
from .models import User, Model
from .crud import UserCRUD,ModelCRUD
from dataclasses import dataclass


class CRUD:
    def __init__(self, session: Session):
        self.user_crud = UserCRUD(session=session)
        self.model_crud = ModelCRUD(session=session)
 

@dataclass
class AlchemyManagerCfg:
   db_url: str
   db_username: str
   db_password: str


class AlchemyDbManager:
    def __init__(self,cfg:AlchemyManagerCfg):
        self.settings = cfg
        engine = create_engine(cfg.db_url)
        self.session_maker = sessionmaker(bind=engine)
        self.crud=CRUD(session=self.session_maker())

    
