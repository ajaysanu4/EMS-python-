from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

# Create your views here.
from employee.forms import EmployeeForm, EmployeeForm, ProjectForm, UserForm
from employee.models import Employee, Employee, ProjectDetails

var = 0


@login_required(login_url='/auth_login')
def dashboard(request):
    employees = Employee.objects.all()
    user = User.objects.get(id=1)
    print(user.username)
    return render(request, "index.html", {'employees': employees, 'user': user})


@login_required(login_url='/auth_login')
def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


@login_required(login_url='/auth_login')
def showprojects(request):
    projects = ProjectDetails.objects.all()
    return render(request, "showprojects.html", {'projects': projects})


@login_required(login_url='/auth_login')
def add(request):
    form = EmployeeForm()
    project = ProjectDetails.objects.all()
    employee = Employee.objects.all()
    return render(request, 'addemployeedetails.html', {'form': form, 'project': project, 'employee': employee})


@login_required(login_url='/auth_login')
def add3(request):
    form1 = ProjectForm()
    return render(request, 'addprojectdetails.html', {'form1': form1})


@login_required(login_url='/auth_login')
def editempdetails(request, id):
    employee = Employee.objects.get(emp_id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form1 = EmployeeForm()
    return render(request, "editempdetails.html",
                  {'employee': employee, 'form': form, 'form1': form1})


@login_required(login_url='/auth_login')
def editprojectdetails(request, id):
    project = ProjectDetails.objects.get(project_id=id)
    form = ProjectForm(request.POST, instance=project)
    return render(request, "editprojectdetails.html", {'project': project, 'form': form})


@login_required(login_url='/auth_login')
def update(request, id):
    employee = Employee.objects.get(emp_id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.save()
            return redirect("/show")
    employee = Employee.objects.get(emp_id=id)
  #  return render(request, "editempdetails.html", {'employee': employee})


@login_required(login_url='/auth_login')
def update3(request, id):
    project = ProjectDetails.objects.get(project_id=id)
    employees = Employee.objects.all()
    form = ProjectForm(request.POST, instance=project)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/showprojects")
    return render(request, "editprojectdetails.html", {'employees': employees, 'project': project})


@login_required(login_url='/auth_login')
def addemp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.save()
            return redirect("/show")
    else:
        form = EmployeeForm()
    return render(request, 'addemployeedetails.html', {'form': form})


@login_required(login_url='/auth_login')
def addproject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.save()
            return redirect("/showprojects")
    else:
        form = EmployeeForm()
    return render(request, 'addprojectdetails.html', {'form': form})


def test(request):
    return render(request, "testing.html")


def auth_login(request):
    form = UserForm()
    return render(request, 'login.html', {'form': form})


def error(request):
    return render(request, "error.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                variable = User.objects.filter(username=username).values('id')
                for a in variable:
                    print(a['id'])
                global var
                var = a['id']
                print(var)
                return redirect("/dashboard")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


@login_required(login_url='/auth_login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


@login_required(login_url='/auth_login')
def deleteEmp(request, id):
    try:
        employee = Employee.objects.get(emp_id=id)
        employee.delete()
        return redirect("/show")
    except:
        return redirect("/error")


@login_required(login_url='/auth_login')
def deletePro(request, id):
    try:
        project = ProjectDetails.objects.get(project_id=id)
        project.delete()
        return redirect("/showprojects")
    except:
        return redirect("/error")

