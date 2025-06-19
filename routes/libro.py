from fastapi import APIRouter, Query, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from middlewares.jwt_bearer import JWTBearer
from sqlalchemy.orm import Session
from config.database import get_db
from services.libro import LibroService
from schemas.libro import Libro

libro_router = APIRouter()


@libro_router.get("/libros", tags=["Libros"], response_model=List[Libro], status_code=200, dependencies=[Depends(JWTBearer())])
def get_libros(db: Session = Depends(get_db)) -> List[Libro]:
    result = LibroService(db).get_libros()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@libro_router.get("/libros/{id}", tags=["Libros"], response_model=Libro, dependencies=[Depends(JWTBearer())])
def get_libro(id: int = Path(ge=1), db: Session = Depends(get_db)) -> Libro:
    result = LibroService(db).get_libro(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró el libro"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@libro_router.get("/libros/categoria/", tags=["Libros"], response_model=List[Libro], dependencies=[Depends(JWTBearer())])
def get_libros_por_categoria(categoria: str = Query(min_length=3, max_length=30), db: Session = Depends(get_db)) -> List[Libro]:
    result = LibroService(db).get_libros_by_categoria(categoria)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontraron libros en esta categoría"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@libro_router.post("/libros", tags=["Libros"], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_libro(libro: Libro, db: Session = Depends(get_db)) -> JSONResponse:
    LibroService(db).create_libro(libro)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el libro"})


@libro_router.put("/libros/{id}", tags=["Libros"], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_libro(id: int, libro: Libro, db: Session = Depends(get_db)) -> dict:
    if not LibroService(db).get_libro(id):
        return JSONResponse(status_code=404, content={"message": "No se encontró el libro"})
    LibroService(db).update_libro(id, libro)
    return JSONResponse(status_code=200, content={"message": "Se ha actualizado el libro"})

@libro_router.delete("/libros/{id}", tags=["Libros"], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_libro(id: int, db: Session = Depends(get_db)) -> dict:
    if not LibroService(db).get_libro(id):
        return JSONResponse(status_code=404, content={"message": "No se encontró el libro"})
    LibroService(db).delete_libro(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el libro"})
