# Generated by Django 3.2.5 on 2021-12-09 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]