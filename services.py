from sqlalchemy.orm import Session
from schemas import TodoCreate, TodoUpdate
from repositories import ITodoRepository

class TodoService:
    def __init__(self, repository: ITodoRepository):
        self.repository = repository
    
    def create_todo(self, db: Session, todo: TodoCreate):
        return self.repository.create(db, todo)
    
    def get_all_todos(self, db: Session):
        return self.repository.get_all(db)
    
    def update_todo(self, db: Session, todo_id: int, todo: TodoUpdate):
        return self.repository.update(db, todo_id, todo)
    
    def delete_todo(self, db: Session, todo_id: int):
        self.repository.delete(db, todo_id)
