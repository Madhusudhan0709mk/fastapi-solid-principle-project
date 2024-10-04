first write (models.py) file for database to define database
  |
  |
  |
  ^
second write (schemas.py) to define data and type constraints  to validate data like this helps in taking particular input

<!-- example we can keep default value -->

description : str = None
completed:bool = False

declare the schemass in such a way that 

<!-- declare repository file as per single responsible principle(SRP) -->

REPOSITORY PATTERN

design pattern that helps you separate business logic from data access code

<!--  queries to write code to database -->

db.query(Todo).filter(Todo.id == todo_id).first()


<!-- services.py on srp,di(dependency injection) -->



