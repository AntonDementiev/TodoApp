import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from src import todo_router

app = FastAPI(title="ToDoAppAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://87.228.19.237/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router, prefix="/todo", tags=["ToDo"])


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
