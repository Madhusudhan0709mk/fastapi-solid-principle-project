from sqlalchemy.orm import Session
from models import TodoItem
from schemas import TodoCreate, TodoUpdate

class ITodoRepository:
    def create(self, db: Session, todo: TodoCreate):
        pass
    
    def get_all(self, db: Session):
        pass
    
    def update(self, db: Session, todo_id: int, todo: TodoUpdate):
        pass

    def delete(self, db: Session, todo_id: int):
        pass

class TodoRepository(ITodoRepository):
    def create(self, db: Session, todo: TodoCreate):
        todo_item = TodoItem(**todo.dict())
        db.add(todo_item)
        db.commit()
        db.refresh(todo_item)
        return todo_item
    
    def get_all(self, db: Session):
        return db.query(TodoItem).all()
    
    def update(self, db: Session, todo_id: int, todo: TodoUpdate):
        todo_item = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
        if todo_item:
            todo_item.title = todo.title
            todo_item.description = todo.description
            todo_item.completed = todo.completed
            db.commit()
            db.refresh(todo_item)
            return todo_item
        return None
    
    def delete(self, db: Session, todo_id: int):
        todo_item = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
        if todo_item:
            db.delete(todo_item)
            db.commit()
