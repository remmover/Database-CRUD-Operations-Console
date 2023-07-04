import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base,  Mapped

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = Column(Integer, primary_key=True)
    fullname: Mapped[str] = Column(String(120), nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(20), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = Column(Integer, primary_key=True)
    fullname: Mapped[str] = Column(String(120), nullable=False)
    group_id: Mapped[int] = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group: Mapped['Group'] = relationship('Group', backref='students')


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(120), nullable=False)
    teacher_id: Mapped[int] = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher: Mapped['Teacher'] = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = Column(Integer, primary_key=True)
    grade: Mapped[int] = Column(Integer, nullable=False)
    date_of: Mapped[datetime.datetime] = Column('date_of', Date, nullable=True)
    student_id: Mapped[int] = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[int] = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE'))
    student: Mapped['Student'] = relationship('Student', backref='grade')
    subject: Mapped['Subject'] = relationship('Subject', backref='grade')
