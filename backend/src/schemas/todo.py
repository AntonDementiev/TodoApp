import uuid
from pydantic import BaseModel

class ToDoCreate(BaseModel): 
    header: str
    body: str

class ShowToDo(ToDoCreate): 
    todo_id: uuid.UUID
    class Config:
        orm_mode = True

class DeletedToDoResponse(BaseModel): 
    deleted_todo_id: uuid.UUID
    