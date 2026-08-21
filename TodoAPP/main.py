#this page binds the model and detabase.py files and acomplish to create the database

from .routers import auth, todos, admin, users
from fastapi import FastAPI, status, Request
from .models import Base
from .database import engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from .dependencies import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI()
templates = Jinja2Templates(directory='TodoAPP/templates')
app.mount("/static",StaticFiles(directory='TodoAPP/static'), name="static")


Base.metadata.create_all(bind=engine) # table creation happen here, and if the table doesn't exist in models, it creates it when we run the program
# crete_all works to create the tables if it's not already created

#now we have to make it consumeable by the api app
#create the dependecy
@app.get("/")
async def test():
    return RedirectResponse(url="/todos/todo-page", status_code= status.HTTP_302_FOUND)

@app.get ('/test_pytest', status_code= status.HTTP_200_OK)
def test_pytest ():
    return {'test': 'successful'}

# the limiter object has to attached with directly app becasuse app is on the top level than APIRouter and listen for every action on the app
#also APIRouter instances have no .state attribute
app.state.limiter =limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)