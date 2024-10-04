from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Boolean,String

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column()