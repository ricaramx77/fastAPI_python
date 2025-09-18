from fastapi import APIRouter
from models.task import Task
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])
tasks_db: List[Task] = []

@router.post("/", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

@router.get("/", response_model=List[Task])
def list_tasks():
    return tasks_db
