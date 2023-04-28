
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',employee_home),
    path('add-emp',add_emp),
    path('delete-emp/<int:emp_id>',del_emp),
]
