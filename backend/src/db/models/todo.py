import uuid 
from sqlalchemy import String, Integer, Column, UUID

from .base import Model

class ToDo(Model): 
    __tablename__ = "To Do"

    todo_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    header = Column(String, nullable=False)
    body = Column(String, nullable=False)