# app.py
from fastapi import FastAPI
from main import app as main_app
from upload import router as upload_router

app = FastAPI()

# Include the routers from other files
app.include_router(main_app)
app.include_router(upload_router, prefix="/upload")
