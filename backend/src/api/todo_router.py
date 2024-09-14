from uuid import UUID
from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession


from src.db import get_db
from src.schemas import ShowToDo, ToDoCreate, DeletedToDoResponse
from src.tools import create_todo, delete_todo, get_todos

todo_router = APIRouter()

@todo_router.post("/create", response_model=ShowToDo)
async def create_todo_api(
    body: ToDoCreate,
    db: AsyncSession = Depends(get_db)
) -> ShowToDo: 
    new_todo = await create_todo(body=body, db=db)
    if new_todo is None: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Что-то пошло не так, попробуйте позже!")
    return new_todo

@todo_router.delete("/delete/{todo_id}", response_model=DeletedToDoResponse)
async def delete_todo_api(
    todo_id: UUID, 
    db: AsyncSession = Depends(get_db)
) -> DeletedToDoResponse: 
    deleted_todo_id = await delete_todo(todo_id=todo_id, db=db)
    if deleted_todo_id is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Что-то пошло не так, попробуйте позже!")
    return DeletedToDoResponse(deleted_todo_id=deleted_todo_id)

@todo_router.get("/list", response_model=List[ShowToDo])
async def get_todos_api(
    db: AsyncSession = Depends(get_db)
) -> List[ShowToDo]: 
    todos = await get_todos(db=db)
    if not todos: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Кажется, у нас нет записей твоих задач :(")
    
    return [ShowToDo.model_validate(todo.__dict__) for todo in todos]
