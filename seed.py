from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random
from main import Subject,Student,Teacher,Grade,Group
from db_engine import engine, Session

session = Session()

Base = declarative_base()

fake = Faker()

for _ in range(3):
    group = Group(name=fake.word())
    session.add(group)

for _ in range(3):
    teacher = Teacher(name=fake.name())
    session.add(teacher)

for _ in range(5):
    subject = Subject(name=fake.word(), teacher_id=random.randint(1, 3))
    session.add(subject)

for _ in range(30):
    student = Student(name=fake.name(), group_id=random.randint(1, 3))
    session.add(student)

for _ in range(20):
    grade = Grade(value=random.randint(1, 12), date=fake.date(), student_id=random.randint(1, 30), subject_id=random.randint(1, 5))
    session.add(grade)

session.commit()
