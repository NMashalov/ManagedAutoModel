from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import create_engine
from .models import User, Model

class UserCRUD:
    def add_user(self,user):
       with self.session_maker() as session:
           session.add()  


class ModelCRUD:
    def __init__(self,session: Session):
        self.session 
    def create_model(self,model):
        self.session.add(
            Model()
        )  
 

class CRUD:
    def __init__(self, user_crud:UserCRUD, model_crud:ModelCRUD):
        self.user_crud = user_crud
        self.model_crud = model_crud

    def 


class AlchemyDbManager:
    def __init__(self,connection):
        engine = create_engine
        self.session_maker = sessionmaker(bind=engine)

    
