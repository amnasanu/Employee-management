from django.urls import path
from .views import *

urlpatterns = [
    path('', records_view),
    
    path('login/', login_view),
    path('register/', register, name='register'),
    
    path('add/',add_employee, name='add_employee'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
    path('get_employee/<int:id>/', get_employee, name='get_employee'),
    path('edit/<int:id>/', edit_employee, name='edit_employee'),
]
