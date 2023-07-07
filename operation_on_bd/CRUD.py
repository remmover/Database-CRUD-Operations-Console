from typing import Type, Union

from src.connection import session
from src.models import User


def get_user(login: str) -> User:
    user = session.query(User).filter(User.login == login).one()
    return user


def create_record(model: Type, **kwargs) -> None:
    record = model(**kwargs)
    session.add(record)
    session.commit()
    session.close()


def get_all_records(model: Type) -> list:
    records = session.query(model).all()
    return records


def update_record(model: Type, _id: int, **kwargs) -> Union[None, Type]:
    record = session.query(model).filter(model.id == _id).one()
    for key, value in kwargs.items():
        setattr(record, key, value)
    session.commit()
    session.close()
    return record


def remove_record(model: Type, _id: int) -> int:
    record = session.query(model).filter(model.id == _id).delete()
    session.commit()
    session.close()
    return record

