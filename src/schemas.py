from pydantic import BaseModel


class AuthRegisterDetails(BaseModel):
    username: str
    password: str
    role: str

class AuthLoginDetails(BaseModel):
    username: str
    password: str
    role:str