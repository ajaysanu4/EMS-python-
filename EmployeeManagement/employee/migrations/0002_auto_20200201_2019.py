# Generated by Django 2.1.15 on 2020-02-01 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_manager_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ProjectDetails'),
        ),
    ]
