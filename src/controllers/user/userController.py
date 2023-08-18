from fastapi import APIRouter, Depends, HTTPException
from auth import AuthHandler
from controllers.user.userSchema import AuthRegisterDetails, AuthLoginDetails, GoogleLoginDetails,  RoleModifyDetails
import database.services.userService as userService
import json



# app = FastAPI()
user = APIRouter()


auth_handler = AuthHandler()
# users = []

@user.post('/register', status_code=201)
def register(auth_details: AuthRegisterDetails):
    if userService.valid_username(auth_details.username):
        raise HTTPException(status_code=401, detail='Existing username')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    userService.create_user(auth_details.username, hashed_password, auth_details.role);
    return


@user.post('/login')
def login(auth_details: AuthLoginDetails):
    if not (userService.valid_username(auth_details.username) or 
            (auth_handler.verify_password('', userService.get_password(auth_details.username)))
            (not auth_handler.verify_password(auth_details.password, userService.get_password(auth_details.username)))): #add a null condition of google login password
        raise HTTPException(status_code=401, detail='Invalid username and/or password**')
        
    token = auth_handler.encode_token(userService.get_role(auth_details.username))
    print(userService.valid_username(auth_details.username))
    return { "token": token, "user_id": userService.valid_username(auth_details.username)}

@user.post('/googleLogin')
def google_login(auth_details: GoogleLoginDetails):
    if not (userService.valid_username(auth_details.username)):
        userService.create_user(auth_details.username, '', 'default')#default role and null password
        
    token = auth_handler.encode_token(userService.get_role(auth_details.username))
    print(userService.valid_username(auth_details.username))
    return { "token": token, "user_id": userService.valid_username(auth_details.username)}
    




@user.post('/addrole')
def add_role(role_add_details: RoleModifyDetails, role=Depends(auth_handler.auth_wrapper)):
    if 'admin' not in role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return userService.add_role(role_add_details.username, role_add_details.role_to_add)

@user.post('/removerole')
def remove_role(role_remove_details: RoleModifyDetails, role=Depends(auth_handler.auth_wrapper)):
    if 'admin' not in role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return userService.remove_role(role_remove_details.username, role_remove_details.role_to_add)


#Role demonstration
@user.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }

@user.get('/admin')
def admin_only(role=Depends(auth_handler.auth_wrapper)):
    print(role[3:8])
    if 'admin' not in role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return { 'message': 'Admin only' }

@user.get('/unprivileged')
def unprivileged(role=Depends(auth_handler.auth_wrapper)):
    return { 'message': 'This area is common to users and admin' }
