from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Employee
from .forms import *
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
def add_employee(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmpForm()
    
    return render(request, 'add_employee.html', {'form': form})

@login_required(login_url='/login')
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully')
        return redirect('/')
    return redirect('/')

@login_required(login_url='/login')
def get_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    data = {
        'emp_name': employee.emp_name,
        'email': employee.email,
        'address': employee.address,
        'phone': employee.phone,
    }
    return JsonResponse(data)

@login_required(login_url='/login')
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmpForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        return redirect('/') 

@login_required(login_url='/login')
def records_view(request):
    emp=Employee.objects.all()
    paginator = Paginator(emp, 10)
    page_number = request.GET.get('page')
    try:
        emp =paginator.page(page_number)
    except PageNotAnInteger:
        emp = paginator.page(1)
    except EmptyPage:
        emp=paginator.page(paginator.num_pages)
    context={
        'emp':emp
    }
    return render(request, "record.html", context)


