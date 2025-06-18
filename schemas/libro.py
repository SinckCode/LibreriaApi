from pydantic import BaseModel, Field
from typing import Optional

class Libro(BaseModel):
    titulo: str = Field(min_length=2, max_length=100)
    autor: str = Field(min_length=2, max_length=100)
    anio: int = Field(ge=0, le=2025)
    categoria: str = Field(min_length=3, max_length=50)
    paginas: int = Field(ge=1, le=5000)
    sinopsis: Optional[str] = Field(None, max_length=500)
    imagen: Optional[str] = Field(None, max_length=300)

    class Config:
        json_schema_extra = {
            "example": {
                "titulo": "Noches Blancas",
                "autor": "Fiódor Dostoyevski",
                "anio": 1848,
                "categoria": "Romance",
                "paginas": 96,
                "sinopsis": "Un joven soñador solitario entabla una conexión profunda con una mujer durante cuatro noches en San Petersburgo.",
                "imagen": "https://example.com/noches-blancas.jpg"
            }
        }
