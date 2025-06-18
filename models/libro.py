from config.database import Base
from sqlalchemy import Column, Integer, String

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)
    paginas = Column(Integer, nullable=False)
    sinopsis = Column(String, nullable=True)
    imagen = Column(String, nullable=True)
