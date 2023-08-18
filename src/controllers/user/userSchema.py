from pydantic import BaseModel


class AuthRegisterDetails(BaseModel):
    username: str
    password: str
    role: str

class AuthLoginDetails(BaseModel):
    username: str
    password: str

class GoogleLoginDetails(BaseModel):
    username: str

class RoleModifyDetails(BaseModel):
    username: str
    role_to_add: str