import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from operation_on_bd.CRUD import (
    get_user,
    create_record,
    get_all_records,
    update_record,
    remove_record,
)
from src.models import Teacher, Subject, Grade, Student, Group

parser = argparse.ArgumentParser(description="DataBase APP")
parser.add_argument("--action", "-a", help="Command: create, update, list, remove")
parser.add_argument("--model", "-m", help="Command: Teacher, Student, Subject, Grade, Group")
parser.add_argument("--id")
parser.add_argument("--name", "-n")
parser.add_argument("--login")

arguments = parser.parse_args()

action = arguments.action
model = arguments.model
_id = arguments.id
name = arguments.name
login = arguments.login


def main():
    if action == "create":
        if model == "Teacher":
            create_record(Teacher, name=name)
        elif model == "Subject":
            create_record(Subject, name=name)
        elif model == "Grade":
            create_record(Grade, name=name)
        elif model == "Student":
            create_record(Student, name=name)
        elif model == "Group":
            create_record(Group, name=name)

    elif action == "list":
        if model == "Teacher":
            teachers = get_all_records(Teacher)
            for t in teachers:
                print(t.id, t.fullname)
        elif model == "Subject":
            subjects = get_all_records(Subject)
            for s in subjects:
                print(s.id, s.name, s.tachers_id)
        elif model == "Grade":
            grades = get_all_records(Grade)
            for g in grades:
                print(g.id, g.grade, g.date_of, g.student_id, g.subject_id)
        elif model == "Student":
            students = get_all_records(Student)
            for s in students:
                print(s.id, s.fullname, s.group_id)
        elif model == "Group":
            groups = get_all_records(Group)
            for g in groups:
                print(g.id, g.name)

    elif action == "update":
        if model == "Teacher":
            update_record(Teacher, _id, name=name)
        elif model == "Subject":
            update_record(Subject, _id, name=name)
        elif model == "Grade":
            update_record(Grade, _id, name=name)
        elif model == "Student":
            update_record(Student, _id, name=name)
        elif model == "Group":
            update_record(Group, _id, name=name)

    elif action == "remove":
        if model == "Teacher":
            remove_record(Teacher, _id)
        elif model == "Subject":
            remove_record(Subject, _id)
        elif model == "Grade":
            remove_record(Grade, _id)
        elif model == "Student":
            remove_record(Student, _id)
        elif model == "Group":
            remove_record(Group, _id)


if __name__ == "__main__":
    user = get_user(login)
    password = input("password: ")
    if password == user.password:
        try:
            main()
        except SQLAlchemyError as err:
            print(err)
    else:
        print("Wrong password!")
        sys.exit()
