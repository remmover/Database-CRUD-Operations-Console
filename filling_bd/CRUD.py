from sqlalchemy import and_
from src.db import session
from src.models import Teacher, Student, Subject, Grade, Group


def get_user(login) -> User:
    pass


#     user = session.query(User).filter(User.login == login).one()
#     return user
#
#
def create_todo(title, description, user):
    pass


#     todo = Todo(title=title, description=description, user=user)
#     session.add(todo)
#     session.commit()
#     session.close()

#
def get_all_todos(user) -> list[Todo]:
    pass


#     todos = session.query(Todo).join(User).filter(Todo.user == user).all()
#     return todos
#
#
def update_todo(_id, title, description, user) -> Todo:
    pass


#     todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
#     todo.update({'title': title, 'description': description})
#     session.commit()
#     session.close()
#     return todo.one()
#
#
def remove_todo(_id, user) -> int:
    pass
#     r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id)).delete()
#     session.commit()
#     session.close()
#     return r
