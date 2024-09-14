from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select
from uuid import UUID
from typing import List, Union

from src.db.models import ToDo

class ToDoDAL: 
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_todo(
            self, header: str, body: str 
    ) -> ToDo: 
        new_todo = ToDo(
            header=header,
            body=body
        )   
        self.db_session.add(new_todo)
        await self.db_session.flush()
        return new_todo
    
    async def delete_todo(
            self, todo_id: UUID
    ) -> Union[UUID, None]: 
        query_to_delete = delete(ToDo). \
            where(ToDo.todo_id == todo_id)
        query_to_select = select(ToDo). \
            where(ToDo.todo_id == todo_id)
        
        result = await self.db_session.execute(query_to_select)
        todo_to_delete = result.scalar_one_or_none()

        if todo_to_delete is None: 
            return todo_to_delete
        
        await self.db_session.execute(query_to_delete)
        return todo_to_delete.todo_id
    
    async def get_todos(
            self
    ) -> List[ToDo]: 
        query = select(ToDo)
        result = await self.db_session.execute(query)
        todos = result.scalars().all()
        return todos