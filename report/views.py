from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum,Avg,Max,Min
from .seed import generate_ranks
import matplotlib.pyplot as plt
from django.http import HttpResponse

def home(request):
    students = Student.objects.all()
    passedstudents = Student.objects.annotate(marks=Sum('StudentMarks__marks')).filter(marks__gte=175).count()
    Failedstudents = Student.objects.annotate(marks=Sum('StudentMarks__marks')).filter(marks__lt=175).count()
    highscore = Student.objects.annotate(marks=Sum('StudentMarks__marks')).aggregate(marks1=Max('marks'))
    lowscore = Student.objects.annotate(marks=Sum('StudentMarks__marks')).aggregate(marks1=Min('marks'))
    return render(request,'report/base.html',{'students':students,'passedstudents':passedstudents,'Failedstudents':Failedstudents,'highscore':highscore,'lowscore':lowscore})


def get_student(request):

    queryset = Student.objects.all().order_by('StudentReportCard')
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(Q(student_name__icontains= search)|Q(deparment__department__icontains= search)|Q(student_id__student_id__icontains= search))
    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'report/student.html',{'queryset':page_obj})



def see_marks(request,student_id):
    
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    
    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks})
