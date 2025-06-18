from models.libro import Libro as LibroModel
from schemas.libro import Libro

class LibroService:

    def __init__(self, db) -> None:
        self.db = db

    def get_libros(self):
        return self.db.query(LibroModel).all()

    def get_libro(self, id: int):
        return self.db.query(LibroModel).filter(LibroModel.id == id).first()

    def get_libros_by_categoria(self, categoria: str):
        return self.db.query(LibroModel).filter(LibroModel.categoria == categoria).all()

    def create_libro(self, libro: Libro):
        nuevo_libro = LibroModel(**libro.model_dump())
        self.db.add(nuevo_libro)
        self.db.commit()
        self.db.refresh(nuevo_libro)
        return nuevo_libro

    def update_libro(self, id: int, data: Libro):
        libro = self.db.query(LibroModel).filter(LibroModel.id == id).first()
        if libro:
            libro.titulo = data.titulo
            libro.autor = data.autor
            libro.anio = data.anio
            libro.categoria = data.categoria
            libro.paginas = data.paginas
            self.db.commit()
            self.db.refresh(libro)
        return libro

    def delete_libro(self, id: int):
        libro = self.db.query(LibroModel).filter(LibroModel.id == id).first()
        if libro:
            self.db.delete(libro)
            self.db.commit()
        return libro
