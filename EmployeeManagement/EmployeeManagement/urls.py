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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from employee import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.dashboard, name='dashboard.html'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^showprojects$', views.showprojects, name='showprojects.html'),
    url(r'^show$', views.show, name='show.html'),
    url(r'^add$', views.add, name='addemployeedetails.html'),
    url(r'^user_logout$', views.user_logout, name='user_logout.html'),
    url(r'^add3$', views.add3, name='addprojectdetails.html'),
    url(r'^addemp$', views.addemp),
    url(r'^auth_login$', views.auth_login, name='login.html'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'^addproject$', views.addproject),
    url(r'^editempdetails/(?P<id>[0-9]+)/$', views.editempdetails, name='editempdetails'),
    url(r'^editprojectdetails/(?P<id>[0-9]+)/$', views.editprojectdetails),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name='login.html'),
    url(r'^error$', views.error, name='error.html'),
    url(r'^update3/(?P<id>[0-9]+)$', views.update3, name='show.html'),
    url(r'^help$', views.help),
    url(r'^deleteEmp/(?P<id>[0-9]+)$', views.deleteEmp),
    url(r'^deletePro/(?P<id>[0-9]+)$', views.deletePro),
    url(r'^auth_register$', views.auth_register, name='register.html'),
    url(r'^user_register$', views.register, name='register.html'),
]
