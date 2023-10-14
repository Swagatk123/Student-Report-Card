from faker import Faker
import random
fake = Faker()
from .models import *
from django.db.models import Sum
# from itertools import product


def create_subject_marks():
        Students = Student.objects.all()
        for student in Students:
         subjects = Subject.objects.all()
         for subject in subjects:
            SubjectMarks.objects.create(
                subject = subject,
                student = student,
                marks = random.randint(1,100)
            )

# def create_subject_marks():
#     students = Student.objects.all()
#     subjects = Subject.objects.all()
    
#     # Generate all possible combinations of students and subjects
#     student_subject_combinations = product(students, subjects)
    
#     for student, subject in student_subject_combinations:
#         # Check if the SubjectMarks entry already exists for this student and subject
#         existing_entry = SubjectMarks.objects.filter(student=student, subject=subject).first()
        
#         if not existing_entry:
#             # Create a new SubjectMarks entry with random marks
#             SubjectMarks.objects.create(
#                 student=student,
#                 subject=subject,
#                 marks=random.randint(1, 100)
#             )




def seed_db(n=10) -> None:
    for i in range(0,n):
        department_obj = Department.objects.all()
        random_index = random.randint(0,len(department_obj)-1)
        department = department_obj[random_index]
        student_id = random.randint(100,999)
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(20,30)
        student_address = fake.address()

        Student_id_obj = StudentID.objects.create(student_id = student_id)

        student_obj = Student.objects.create(
            deparment = department,
            student_id = Student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address
        )

# def delete_duplicates():
   
#     duplicates = SubjectMarks.objects.values('subject').annotate(count=Count('subject')).filter(count__gt=1)
#     for duplicate in duplicates:
#      duplicate_records = SubjectMarks.objects.filter(subject=duplicate['subject'])
#      first_record = duplicate_records.first()
#      duplicate_records.exclude(pk=first_record.pk).delete()

def generate_ranks():
    
    ranks = Student.objects.annotate(marks=Sum('StudentMarks__marks')).order_by('-marks','-student_age')
    i = 1
    for rank in ranks:
       ReportCard.objects.create( 
           student = rank,
           student_rank = i)
       i+=1