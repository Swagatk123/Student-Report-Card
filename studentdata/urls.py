
from django.contrib import admin
from django.urls import path
from report.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('students/',get_student,name="get_student"),
    path('see_marks/<student_id>/',see_marks,name='see_marks'),

]

