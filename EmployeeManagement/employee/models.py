from django.db import models

from django.contrib.auth.models import User
import logging
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class ProjectDetails(models.Model):
    project_id = models.IntegerField(unique=True, primary_key=True, null=False)
    project_name = models.CharField(max_length=20)
    project_description = models.CharField(max_length=100,null=True,blank = True)
    project_company = models.CharField(max_length=20)
    project_owner = models.CharField(max_length=20)
    project_category = models.CharField(max_length=20)
    project_status = models.CharField(max_length=20)
    project_start_date = models.DateField()
    project_end_date = models.DateField(null=True,blank = True)
    project_budget = models.IntegerField()
    project_summary = models.CharField(max_length=250,null=True,blank = True)
    project_record = models.CharField(max_length=100,null=True,blank = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class meta:
        db_table = "project_details"

    def __unicode__(self):
        return self.Type


class Employee(models.Model):
    emp_id = models.IntegerField(unique=True, primary_key=True, null=False)
    emp_first_name = models.CharField(max_length=20)
    emp_last_name = models.CharField(max_length=20)
    emp_gender = models.CharField(max_length=20)
    emp_email = models.CharField(max_length=20)
    emp_dob = models.DateField()
    emp_marital_status = models.CharField(max_length=20)
    emp_home_number = models.CharField(max_length=20,null=True,blank = True)
    emp_personal_number = models.CharField(max_length=20)
    emp_hire_date = models.DateField()
    emp_designation = models.CharField(max_length=20)
    emp_type = models.CharField(max_length=20)
    emp_address = models.CharField(max_length=20)
    emp_city = models.CharField(max_length=20)
    emp_state = models.CharField(max_length=20)
    emp_postal_code = models.CharField(max_length=20)
    emp_country = models.CharField(max_length=20)
    emp_notes = models.CharField(max_length=250, null=True,blank = True)
    emp_work_location = models.CharField(max_length=20)
    emp_manager_id = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True,blank = True)
    emp_project_id = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE, null=True,blank = True)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank = True)

    class meta:
        db_table = "employee"

LOG_LEVELS = (
    (logging.NOTSET, _('NotSet')),
    (logging.INFO, _('Info')),
    (logging.WARNING, _('Warning')),
    (logging.DEBUG, _('Debug')),
    (logging.ERROR, _('Error')),
    (logging.FATAL, _('Fatal')),
)


@python_2_unicode_compatible
class StatusLog(models.Model):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LOG_LEVELS, default=logging.ERROR, db_index=True)
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.msg

    class Meta:
        ordering = ('-create_datetime',)
        verbose_name_plural = verbose_name = 'Logging'