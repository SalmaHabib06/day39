# Generated by Django 4.2.7 on 2023-12-13 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_employee_gender_employee_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Department',
            new_name='department',
        ),
    ]
