# Generated by Django 3.2.5 on 2021-12-09 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskes', '0003_alter_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Title',
            new_name='title',
        ),
    ]