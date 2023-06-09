from fastapi import APIRouter, Depends, HTTPException
from auth import AuthHandler
from controllers.user.userSchema import AuthRegisterDetails, AuthLoginDetails
import database.services.userService as userService



# app = FastAPI()
user = APIRouter()


auth_handler = AuthHandler()
# users = []

@user.post('/register', status_code=201)
def register(auth_details: AuthRegisterDetails):
    #isuser()
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    userService.create_user(auth_details.username, hashed_password, auth_details.role);
    return


@user.post('/login')
def login(auth_details: AuthLoginDetails):
    if not (userService.valid_username(auth_details.username) or 
            (not auth_handler.verify_password(auth_details.password, userService.get_password(auth_details.username)))):
        raise HTTPException(status_code=401, detail='Invalid username and/or password**')
        
    token = auth_handler.encode_token(userService.get_role(auth_details.username))
    return { 'token': token }


#Role demonstration
@user.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }

@user.get('/admin')
def admin_only(role=Depends(auth_handler.auth_wrapper)):
    print(role[3:8])
    if role[3:8] != 'admin':
        raise HTTPException(status_code=403, detail='Forbidden')
    return { 'message': 'Admin only' }

@user.get('/unprivileged')
def unprivileged(role=Depends(auth_handler.auth_wrapper)):
    return { 'message': 'This area is common to users and admin' }
