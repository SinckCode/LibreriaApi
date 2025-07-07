# 📚 LibreriaApi - Sistema de Gestión de Libros

**LibreriaApi** es una API RESTful desarrollada en **FastAPI** que permite gestionar un catálogo de libros de forma sencilla, segura y escalable.  
Incluye autenticación mediante JWT, operaciones CRUD, y despliegue profesional automatizado con GitHub Actions.

---

## ✨ Descripción General

El proyecto surge de la necesidad de crear una plataforma digital que facilite el acceso, la gestión y la consulta de libros desde cualquier dispositivo.  
Se compone de dos partes:

- **Backend:** FastAPI + SQLite, con autenticación JWT y endpoints RESTful.
- **Frontend:** React desplegado en Firebase Hosting.

🌐 **API en producción:**  
[https://104.248.118.8/docs](https://104.248.118.8/docs)

💻 **Frontend en producción:**  
[https://libreriaapp-ca5dd.web.app/](https://libreriaapp-ca5dd.web.app/)  
> ⚠️ **Nota:** Para que el frontend funcione, debes tener disponible la API en línea.

---

## 🛠️ Tecnologías y Dependencias

- Python 3.12+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- PyJWT
- PM2 (despliegue en servidor)
- Nginx + SSL (proxy reverso)
- GitHub Actions (CI/CD automático)

**Dependencias principales (`requirements.txt`):**

```
annotated-types==0.7.0
anyio==4.9.0
click==8.2.1
colorama==0.4.6
fastapi==0.115.13
greenlet==3.2.3
h11==0.16.0
idna==3.10
pydantic==2.11.7
pydantic_core==2.33.2
PyJWT==2.10.1
sniffio==1.3.1
SQLAlchemy==2.0.41
starlette==0.46.2
typing-inspection==0.4.1
typing_extensions==4.14.0
uvicorn==0.34.3
```

---

## 📂 Estructura del Proyecto

```
.
├── config/               # Configuración de la base de datos
├── middlewares/          # Middleware de autenticación y errores
├── models/               # Modelos ORM (SQLAlchemy)
├── routes/               # Rutas de la API
├── schemas/              # Validación de datos (Pydantic)
├── services/             # Lógica de negocio
├── jwt_manager.py        # Generación y validación de JWT
├── main.py               # Punto de entrada
├── ecosystem.config.js   # Configuración de PM2
├── requirements.txt      # Dependencias
├── database.sqlite       # Base de datos SQLite
└── .github/workflows/    # Workflows de GitHub Actions
```

---

## 🚀 Instalación y Ejecución Local

### 📋 Requisitos Previos

- Python instalado.
- (Opcional) Crear un entorno virtual:

  ```
  python -m venv venv
  ```

  Activar en Windows:
  ```
  venv\Scripts\activate
  ```

  Activar en Linux/macOS:
  ```
  source venv/bin/activate
  ```

---

### ⚙️ Instalación de Dependencias

```
pip install -r requirements.txt
```

---

### ▶️ Iniciar la API

```
uvicorn main:app --reload --port 8000 --host 127.0.0.1
```

API disponible en:  
http://127.0.0.1:8000

Documentación Swagger:  
http://127.0.0.1:8000/docs

---

## 🔐 Autenticación

La autenticación se basa en JWT.  
Endpoint de login:

```
POST /login
```

**Cuerpo de la petición:**

```json
{
  "email": "admin@salle.com",
  "password": "admin"
}
```

**Respuesta:**

```json
{
  "token": "TOKEN_GENERADO"
}
```

Incluye este token en el header `Authorization` en cada llamada:

```
Bearer TOKEN_GENERADO
```

---

## 📑 Endpoints Principales

- `POST /login`: Genera un token JWT.
- `GET /libros`: Listar todos los libros.
- `POST /libros`: Crear un nuevo libro.
- `GET /libros/{id}`: Obtener un libro por ID.
- `PUT /libros/{id}`: Actualizar un libro.
- `DELETE /libros/{id}`: Eliminar un libro.

Todos los endpoints de `/libros` requieren autenticación.

---

## 🏗️ Despliegue Automático con GitHub Actions

Este proyecto está configurado con **GitHub Actions** para despliegue continuo en un servidor Ubuntu.  
Cada push a la rama `main` activa un workflow que realiza lo siguiente:

1. Clona el repositorio.
2. Configura una clave SSH segura.
3. Se conecta vía SSH al servidor.
4. Navega a la carpeta del proyecto.
5. Actualiza el código con `git pull`.
6. Activa el entorno virtual.
7. Reinicia la API con **PM2**.

Workflow ubicado en:

```
.github/workflows/deploy.yml
```

---

## 🖥️ Frontend

El frontend fue desarrollado en **React** y desplegado en **Firebase Hosting**:  
[https://libreriaapp-ca5dd.web.app/](https://libreriaapp-ca5dd.web.app/)

Funciones principales:

- **LoginPage:** inicio de sesión y almacenamiento de token.
- **CatalogPage:** catálogo con búsqueda, filtros y modo administrador.
- **Modales:** detalle de libros y formulario de creación/edición.
- **Modo Admin:** permite agregar, editar y eliminar libros.

⚠️ **Importante:** La API debe estar disponible para que el frontend funcione correctamente.

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia que definas (MIT, GPL, etc.).
