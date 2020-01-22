from distutils.command import register

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from employee.models import Employee, ProjectDetails

COUNTRY_CHOICES= [
    ('india', 'INDIA'),
    ('usa', 'USA'),
    ('CHINA', 'CHINA')
    ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectDetails
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class EmployeeForm(forms.ModelForm):
    emp_country = forms.CharField(label='What is your country?', widget=forms.Select(choices=COUNTRY_CHOICES))
    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_manager_id'].label_from_instance = self.business_label_manager
        self.fields['emp_project_id'].label_from_instance = self.business_label_project

    @staticmethod
    def business_label_manager(self):
        return str(self.emp_first_name)

    @staticmethod
    def business_label_project(self):
        return str(self.project_name)


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = "employees_confirm_delete.html"
    success_url = "/"

    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(EmployeeDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
