import os

import fastapi
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import typing as tp

class ServerConfigs:
    def __init__(self,
            root_user_name,
            root_user_password,
            db_url,
            ):
        self.root_user_name = root_user_name
        self.root_user_password = root_user_password
        self.db_url = db_url

    @classmethod
    def from_envs(cls):
        return cls(
            root_user_name = os.environ.get('AUTO_MODEL_ROOT'),
            root_user_password = os.environ.get('AUTO_MODEL_ROOT')
        )
    


class Server:
    def __init__(self):
        pass

    def security(self):
        @self.app.post("/token")
        async def login(form_data: tp.Annotated[OAuth2PasswordRequestForm, Depends()]):
            user_dict = fake_users_db.get(form_data.username)
            if not user_dict:
                raise HTTPException(status_code=400, detail="Incorrect username or password")
            user = UserInDB(**user_dict)
            hashed_password = fake_hash_password(form_data.password)
            if not hashed_password == user.hashed_password:
                raise HTTPException(status_code=400, detail="Incorrect username or password")

            return {"access_token": user.username, "token_type": "bearer"}


    @app.get("/items/")
    async def read_items(token: tp.Annotated[str, Depends(oauth2_scheme)]):
        return {"token": token}



    