from sqlalchemy import func, desc, and_, distinct, select

from src.models import Teacher, Student, Subject, Grade, Group
from src.db import session


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    :return:
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    :return:
    """
    result = None
    return result


def select_3():
    """
    Знайти середній бал у групах з певного предмета.
    :return:
    """
    result = None
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    :return:
    """
    result = None
    return result


def select_5():
    """
    Знайти, які курси читає певний викладач.
    :return:
    """
    result = None
    return result


def select_6():
    """
    Знайти список студентів у певній групі.
    :return:
    """
    result = None
    return result


def select_7():
    """
    Знайти оцінки студентів в окремій групі з певного предмета.
    :return:
    """
    result = None
    return result


def select_8():
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    :return:
    """
    result = session.query(distinct(Teacher.fullname), func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Subject) \
        .join(Teacher) \
        .where(Teacher.id == 3).group_by(Teacher.fullname).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_9():
    """
    Знайти список курсів, які відвідує певний студент.
    :return:
    """
    result = None
    return result


def select_10():
    """
    Список курсів, які певному студенту читає певний викладач.
    :return:
    """
    result = None
    return result


def select_11():
    """
    Середній бал, який певний викладач ставить певному студентові.
    :return:
    """
    result = None
    return result


def select_12():
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті.
    :return:
    """
    group_id = 2
    dis_id = 2
    # Знаходимо останнє заняття
    subq = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == dis_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1)).scalar_subquery()

    result = session.query(Student.fullname, Subject.name, Group.name, Grade.grade, Grade.date_of) \
        .select_from(Grade) \
        .join(Student) \
        .join(Subject) \
        .join(Group) \
        .filter(and_(Grade.discipline_id == dis_id, Group.id == group_id, Grade.date_of == subq)) \
        .order_by(desc(Grade.date_of)).all()
    return result


if __name__ == '__main__':
    print(select_1())
    print(select_2())
    print(select_3())
    print(select_4())
    print(select_5())
    print(select_6())
    print(select_7())
    print(select_8())
    print(select_9())
    print(select_10())
    print(select_11())
    print(select_12())
