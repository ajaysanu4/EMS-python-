from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from employee.forms import EmployeeForm, ProjectForm, UserForm, UserRegistrationForm
from employee.models import Employee, ProjectDetails
import logging

db_logger = logging.getLogger('db')


@login_required(login_url='/auth_login')
def dashboard(request):
    try:
        return render(request, "index.html")
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def show(request):
    try:
        employees = Employee.objects.filter(user_id_id=request.session.get('id'))
        return render(request, "show.html", {'employees': employees})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def showprojects(request):
    try:
        projects = ProjectDetails.objects.filter(user_id_id=request.session.get('id'))
        return render(request, "showprojects.html", {'projects': projects})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def add(request):
    try:
        form = EmployeeForm()
        project = ProjectDetails.objects.all()
        employee = Employee.objects.all()
        return render(request, 'addemployeedetails.html', {'form': form, 'project': project, 'employee': employee})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def add3(request):
    try:
        form = ProjectForm()
        return render(request, 'addprojectdetails.html', {'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def editempdetails(request, id):
    try:
        employee = Employee.objects.get(emp_id=id)
        form = EmployeeForm(request.POST, instance=employee)
        return render(request, "editempdetails.html", {'employee': employee, 'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def editprojectdetails(request, id):
    try:
        project = ProjectDetails.objects.get(project_id=id)
        form = ProjectForm(request.POST, instance=project)
        return render(request, "editprojectdetails.html", {'project': project, 'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def update(request, id):
    try:
        if request.method == "POST":
            employee = Employee.objects.get(emp_id=id)
            form = EmployeeForm(request.POST, instance=employee)
            print(form.is_valid())
            if form.is_valid():
                save_data = form.save(commit=False)
                save_data.user_id_id = request.session.get('id')
                save_data.save()
                message = "Data Updated Successfully"
                employees = Employee.objects.filter(user_id_id=request.session.get('id'))
                return render(request, "show.html", {'employees': employees, 'message': message})
            else:
                return render(request, "editempdetails.html", {'employee': employee, 'form': form})

        else:
            employee = Employee.objects.get(emp_id=id)
            form = EmployeeForm()
        return render(request, "editempdetails.html", {'employee': employee, 'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def update3(request, id):
    try:
        if request.method == "POST":
            project = ProjectDetails.objects.get(project_id=id)
            form = ProjectForm(request.POST, instance=project)
            print(form.is_valid())
            if form.is_valid():
                save_data = form.save(commit=False)
                save_data.user_id_id = request.session.get('id')
                save_data.save()
                message = "Data Updated Successfully"
                projects = ProjectDetails.objects.filter(user_id_id=request.session.get('id'))
                return render(request, "showprojects.html", {'projects': projects, 'message': message})
            else:
                employee = Employee.objects.get(emp_id=id)
                project = ProjectDetails.objects.get(project_id=id)
                return render(request, "editprojectdetails.html",
                              {'employee': employee, 'project': project, 'form': form})
        else:
            employee = Employee.objects.get(emp_id=id)
            form = EmployeeForm()
        return render(request, "editprojectdetails.html", {'employee': employee, 'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def addemp(request):
    try:
        if request.method == "POST":
            form = EmployeeForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                save_data = form.save(commit=False)
                save_data.user_id_id = request.session.get('id')
                save_data.save()
                message = "Employee Added Successfully"
                employees = Employee.objects.filter(user_id_id=request.session.get('id'))
                return render(request, "show.html", {'employees': employees, 'message': message})
            else:
                return render(request, 'addemployeedetails.html', {'form': form})
        else:
            form = EmployeeForm(request.POST)
            return render(request, 'addemployeedetails.html', {'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def addproject(request):
    try:
        if request.method == "POST":
            form = ProjectForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                save_data = form.save(commit=False)
                save_data.user_id_id = request.session.get('id')
                save_data.save()
                message = "Project Added Successfully"
                projects = ProjectDetails.objects.filter(user_id_id=request.session.get('id'))
                return render(request, "showprojects.html", {'projects': projects, 'message': message})
            else:
                return render(request, 'addprojectdetails.html', {'form': form})
        else:
            form = ProjectForm()
        return render(request, 'addprojectdetails.html', {'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


def help(request):
    return render(request, "help.html")


def auth_login(request):
    form = UserForm()
    return render(request, 'login.html', {'form': form})


def error(request):
    try:
        return render(request, "error.html")
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


def user_login(request):
    try:
        if request.method == "POST":
            form = UserForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        variable = User.objects.filter(username=username).values('id')
                        for a in variable:
                            request.session['id'] = a['id']
                        return redirect("/dashboard")
                else:
                    message = "Unable to login. Either username or password is incorrect."
                    return render(request, 'login.html', {'form': form, 'message': message})
            else:
                return render(request, 'login.html', {'form': form})
        else:
            form = UserForm()
        return render(request, 'login.html', {'form': form})
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def user_logout(request):
    try:
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def deleteEmp(request, id):
    try:
        employee = Employee.objects.get(emp_id=id)
        employee.delete()
        return redirect("/show")
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


@login_required(login_url='/auth_login')
def deletePro(request, id):
    try:
        project = ProjectDetails.objects.get(project_id=id)
        project.delete()
        return redirect("/showprojects")
    except Exception as e:
        db_logger.exception(e)
        return redirect("/error")


def auth_register(request):
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            form = UserForm()
            register_message = "User Registered Successfully"
            return render(request, 'login.html', {'form': form, 'register_message': register_message})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
