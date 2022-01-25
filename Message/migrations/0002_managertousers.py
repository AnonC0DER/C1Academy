# Generated by Django 3.2.9 on 2022-01-25 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0008_alter_manager_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerToUsers',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True, null=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Manager.manager')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
    ]