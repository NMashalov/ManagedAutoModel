import typing as tp

class ServerManager:
    def __init__(self, cfg :ServerConfigs):
        self.app = fastapi.FastAPI()
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        
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