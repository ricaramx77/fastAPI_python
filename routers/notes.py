from fastapi import APIRouter
from models.note import Note
from typing import List

router = APIRouter(prefix="/notes", tags=["notes"])
notes_db: List[Note] = []

@router.post("/", response_model=Note)
def create_note(note: Note):
    notes_db.append(note)
    return note

@router.get("/", response_model=List[Note])
def list_notes():
    return notes_db
