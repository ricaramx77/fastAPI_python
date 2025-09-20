# FastAPI Python Project

Este proyecto es una API de ejemplo usando FastAPI para gestionar tareas, notas y productos.

## Estructura
- **main.py**: Archivo principal de la aplicación.
- **routers/**: Rutas separadas para tareas, notas y productos usando APIRouter.
- **models/**: Modelos Pydantic para validación de datos.

## Cómo ejecutar
1. Instala dependencias:
   pip install "fastapi[all]" "uvicorn[standard]"
   
2. Ejecuta el servidor:
   uvicorn main:app --reload
3. Accede a la documentación interactiva en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Author
ricaramx77
