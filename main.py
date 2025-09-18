from fastapi import FastAPI
from routers.tasks import router as tasks_router
from routers.notes import router as notes_router
from routers.products import router as products_router

app = FastAPI()

app.include_router(tasks_router)
app.include_router(notes_router)
app.include_router(products_router)

# Puedes ejecutar con: uvicorn main:app --reload
