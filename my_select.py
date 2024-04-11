from sqlalchemy import func, create_engine,desc
from sqlalchemy.orm import sessionmaker
from main import Subject,Student,Group,Grade,Teacher
from db_engine import Session, engine


session = Session()

def select_1(session):
    avg_grade = func.round(func.avg(Grade.value), 2).label('average')
    return session.query(Student.name, avg_grade).\
        join(Grade).\
        group_by(Student.id).\
        order_by(desc(avg_grade)).\
        limit(5).all()

def select_2(session, subject_id):
    avg_grade = func.round(func.avg(Grade.value),2).label('average')
    return session.query(Student.name, avg_grade).\
        join(Grade).join(Subject).\
        filter(Subject.id == subject_id).\
        group_by(Student.name).\
        order_by(desc(avg_grade)).\
        first()

def select_3(session, subject_id):
    avg_grade = func.round(func.avg(Grade.value),2).label('average')
    return session.query(Group.name,avg_grade).\
        select_from(Student).\
        join(Group).\
        join(Grade).\
        join(Subject).\
        filter(Subject.id == subject_id).\
        group_by(Group.name).all()

def select_4(session):
    return session.query(func.round(func.avg(Grade.value),2)).scalar()

def select_5(session,teacher_id):
    return session.query(Subject.name).\
        join(Teacher).\
        filter(Teacher.id==teacher_id).all()

def select_6(session, group_id):
    return session.query(Student.name).\
        join(Group).\
        filter(Group.id == group_id).\
        group_by(Student.name).all()

def select_7(session,group_id,subject_id):
    return session.query(Student.name,Grade.value).\
        join(Grade).join(Group).join(Subject).\
        filter(Group.id == group_id, Subject.id == subject_id).\
        group_by(Student.name, Grade.value).all()

def select_8(session,teacher_id):
    return session.query(func.round(func.avg(Grade.value),2)).\
        join(Subject).join(Teacher).\
        filter(Teacher.id == teacher_id).scalar()

def select_9(session,student_id):
    return session.query(Subject.name).\
    join(Grade).join(Student).\
    filter(Student.id== student_id).\
    group_by(Subject.name).all()

def select_10(session,student_id,teacher_id):
    return session.query(Subject.name).\
        join(Teacher).join(Grade).join(Student).\
        filter(Student.id == student_id, Teacher.id == teacher_id).\
        group_by(Subject.name).all()

def select_11(session,student_id,teacher_id):
    avg_grade = func.round(func.avg(Grade.value),2).label('average')
    return session.query(avg_grade).\
        select_from(Student).\
        join(Grade).join(Subject).\
        filter(Subject.teacher_id == teacher_id, Student.id ==student_id).\
        order_by(desc(avg_grade)). \
        scalar()

def select_12(session,group_id,subject_id):
    last_date = session.query(func.max(Grade.date)).scalar()
    return session.query(Student.name, Grade.value).\
        join(Grade).join(Subject).\
        filter(Group.id == group_id, subject_id == Subject.id, Grade.date == last_date).\
        group_by(Student.name, Grade.value).all()


s12 = select_12(session, 1,2)
print(s12)

# students = select_1(session)
# for student in students:
#     print(f"Студент: {student[0]}, Середній бал: {student[1]}")


# s4 = select_4(session)
# print(s4)

# s5 = select_5(session,3)
# print(s5)

# s6 = select_6(session, 'drive')
# print(s6)

# s7 = select_7(session, 1,2)
# print(s7)
#
# s8 = select_8(session,3)
# print(s8)
#
# s9 = select_9(session,6)
# print(s9)
# #
# s10 = select_10(session, 6,2)
# print(s10)