# Generated by Django 3.2.9 on 2022-01-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_alter_manager_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('can_view_manager', 'Can view manager'), ('can_add_student', 'Can add student'), ('can_add_student_profile', 'Can add student profile'), ('can_change_student', 'Can change student'), ('can_change_student_profile', 'Can change student profile'), ('can_delete_student', 'Can delete student'), ('can_delete_student_profile', 'Can delete student profile'), ('can_view_student', 'Can view student'), ('can_view_student_profile', 'Can view student profile')],
            },
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={},
        ),
    ]
