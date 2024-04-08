from main import Subject,Student,Teacher,Grade,Group,session
import argparse

MODELS = {
    'Student': Student,
    'Subject': Subject,
    'Teacher': Teacher,
    'Grade': Grade,
    'Group': Group
}

def create(args):
    model = MODELS[args.model]
    if args.model == 'Grade':
        new_instance = model(value = args.value, date = args.date, student_id = args.student_id, subject_id = args.subject_id)
    elif args.model == 'Student':
        new_instance = model(name = args.name, group_id = args.group_id)
    elif args.model == 'Subject' :
        new_instance = model(name = args.name, teacher_id = args.teacher_id)
    elif args.model == 'Group':
        new_instance = model(name = args.name)
    elif args.model == 'Teacher':
        new_instance = model(name = args.name)
    else:
        print( "Error")
    session.add(new_instance)
    session.commit()

def list(args):
    model = MODELS[args.model]
    if args.model == 'Grade':
        grades = session.query(Grade).all()
        return [f'ID :{grade.id}, Value : {grade.value}, '
                 f'student_id : {grade.student_id}, subject_id : {grade.subject_id}, '
                 f'date : {grade.date}' for grade in grades]

    elif args.model == 'Student':
        students = session.query(Student).all()
        return [f'ID :{student.id}, Name : {student.name}, group_id : {student.group_id}' for student in students]
    elif args.model == 'Subject':
        subjects = session.query(Subject).all()
        return [f'ID :{subject.id}, Name : {subject.name}, teacher_id : {subject.teacher_id}' for subject in subjects]
    elif args.model == 'Group':
        groups = session.query(Group).all()
        return [f'ID :{group.id}, Name of group : {group.name} ' for group in groups]

    elif args.model == 'Teacher':
        teachers = session.query(Teacher).all()
        return [f'ID :{teacher.id},Teacher name : {teacher.name}' for teacher in teachers]
    else:
        print("Error")

def update(args):
    model = MODELS[args.model]
    instance = session.query(model).get(args.id)
    if instance:
        if args.model == 'Grade':
            instance.value = args.value
            instance.date = args.date
            instance.student_id = args.student_id
            instance.subject_id = args.subject_id
        elif args.model == 'Student':
            instance.name = args.name
            instance.group_id = args.group_id
        elif args.model == 'Subject':
            instance.name = args.name
            instance.teacher_id = args.teacher_id
        elif args.model == 'Group':
            instance.name = args.name
        elif args.model == 'Teacher':
            instance.name = args.name
        session.commit()
    else:
        print(f"No {args.model} found with this ID")

def remove(args):
    model = MODELS[args.model]
    instance = session.query(model).get(args.id)
    if instance:
        session.delete(instance)
        session.commit()
    else:
        print(f"No {args.model} found with this ID")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'remove'], required=True)
    parser.add_argument('-m', '--model', choices=['Student', 'Subject', 'Teacher', 'Grade', 'Group'], required=True)
    parser.add_argument('-n', '--name')
    parser.add_argument('-i', '--id', type=int)
    parser.add_argument('-v', '--value', type=int)
    parser.add_argument('-d', '--date')
    parser.add_argument('-s', '--student_id', type=int)
    parser.add_argument('-su', '--subject_id', type=int)
    parser.add_argument('-g', '--group_id', type=int)
    parser.add_argument('-t', '--teacher_id', type=int)
    args = parser.parse_args()

    if args.action == 'create':
        print(create(args))
    elif args.action == 'list':
        lister = list(args)
        for i  in lister:
            print(i)
    elif args.action == 'update':
        print(update(args))
    elif args.action == 'remove':
        print(remove(args))

if __name__ == "__main__":
    main()


