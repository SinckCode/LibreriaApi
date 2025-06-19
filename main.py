from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 agregado
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routes.libro import libro_router
from routes.user import user_router
from models import libro

app = FastAPI(
    title="LibreriaApi - Sistema de Gestión de ",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)
app.include_router(libro_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)
