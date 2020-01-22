"""EmployeeManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from employee import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.dashboard, name='index.html'),
    path('dashboard', views.dashboard, name='dashboard.html'),
    path('showprojects', views.showprojects, name='showprojects.html'),
    path('show', views.show, name='show.html'),
    path('add', views.add, name='addemployeedetails.html'),
    path('user_logout', views.user_logout, name='user_logout.html'),
    path('add3', views.add3, name='addprojectdetails.html'),
    path('addemp', views.addemp),
    path('auth_login', views.auth_login),
    path('user_login', views.user_login, name='user_login'),
    path('addproject', views.addproject),
    path('editempdetails/<int:id>', views.editempdetails),
    path('editprojectdetails/<int:id>', views.editprojectdetails),
    path('update/<int:id>', views.update, name='login.html'),
    path('error', views.error, name='error.html'),
    path('update3/<int:id>', views.update3, name='show.html'),
    path('test', views.test),
    path('deleteEmp/<int:id>',views.deleteEmp),
    path('deletePro/<int:id>',views.deletePro)
]
