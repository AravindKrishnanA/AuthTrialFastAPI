from fastapi import FastAPI

app = FastAPI()


from controllers.user import userController

app.include_router(userController.user)

