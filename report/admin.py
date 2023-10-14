from django.contrib import admin
from .models import *
from django.db.models import Sum

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name','deparment','student_age','student_address']
    
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Subject)

@admin.register(ReportCard)
class StudentRankAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','date_of_report_card']
    ordering = ['student_rank']
    def total_marks(self,obj):
        subject_marks = SubjectMarks.objects.filter(student= obj.student)
        marks =  subject_marks.aggregate(marks = Sum('marks'))
        return marks['marks']


@admin.register(SubjectMarks)
class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']