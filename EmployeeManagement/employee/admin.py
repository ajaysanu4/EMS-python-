from django.contrib import admin
from django_db_logger.admin import StatusLogAdmin

from employee.models import Employee, ProjectDetails,StatusLog

admin.site.register(Employee)
admin.site.register(ProjectDetails)
admin.site.register(StatusLog, StatusLogAdmin)
# Register your models here.
