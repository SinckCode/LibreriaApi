import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# Ruta relativa al archivo .sqlite
sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Crear el engine para SQLite
engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},  # Necesario para SQLite
    echo=True
)

# Crear SessionLocal (buena práctica para FastAPI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declaración de la base para modelos
Base = declarative_base()

# Dependencia para usar en FastAPI con Depends
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
