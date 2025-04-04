from fastapi import FastAPI
from routes import user_routes
from core.init_db import init_db

app = FastAPI()

init_db()


app.include_router(user_routes.router)