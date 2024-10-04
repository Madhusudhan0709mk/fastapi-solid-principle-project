from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base
from schemas import TodoCreate, TodoUpdate ,TodoInDB
from repositories import TodoRepository
from services import TodoService
from database import engine, get_db  # Assuming you have a get_db function to manage the database session
import uvicorn
app = FastAPI()

# Initialize DB
Base.metadata.create_all(bind=engine)

# Dependency Injection (SRP, DIP)
todo_repository = TodoRepository()
todo_service = TodoService(todo_repository)

@app.post("/todos/", response_model=TodoInDB)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)

@app.get("/getall/")
def get_all_todos(db: Session = Depends(get_db)):
    return todo_service.get_all_todos(db)

@app.put("/todos/{todo_id}", response_model=TodoInDB)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = todo_service.update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_service.delete_todo(db, todo_id)
    return {"message": "Todo deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)