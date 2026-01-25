from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env") # loads the .env variables into the os envirnoment
from routes import base

app = FastAPI()

app.include_router(base.base_router)