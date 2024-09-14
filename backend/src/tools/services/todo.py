from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union, List

from src.db.models import ToDo
from src.db.interfaces import ToDoDAL
from src.schemas import ToDoCreate, ShowToDo

async def create_todo(body: ToDoCreate, db: AsyncSession) -> Union[ShowToDo, None]:
    async with db.begin(): 
        todo_dal = ToDoDAL(db)

        new_todo = await todo_dal.create_todo(
            header=body.header,
            body=body.body,
        )

        return ShowToDo(
            todo_id = new_todo.todo_id,
            header = new_todo.header,
            body = new_todo.body
        )

async def delete_todo(todo_id: UUID, db: AsyncSession) -> Union[UUID, None]: 
    async with db.begin(): 
        todo_dal = ToDoDAL(db)

        deleted_todo = await todo_dal.delete_todo(todo_id=todo_id)
        return deleted_todo
    
async def get_todos(db: AsyncSession) -> List[ToDo]: 
    async with db.begin(): 
        todo_dal = ToDoDAL(db)

        todos = await todo_dal.get_todos()
        return todos