from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..services.auth.router import router as auth_router
from ..services.user.router import router as user_router
from fastapi.staticfiles import StaticFiles
from ..services.files.router import router as files_router
import logging


logging.basicConfig(level=logging.INFO)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
    ,
    allow_headers=["*"]
)
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")
app.include_router(files_router, prefix="/files")
app.mount("/files/static", StaticFiles(directory="backend/uploads"), name="files-static")
