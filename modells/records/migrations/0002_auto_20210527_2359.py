# Generated by Django 3.2.3 on 2021-05-27 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='faculty_name',
            new_name='faculty_names',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_name',
            new_name='faculty_names',
        ),
    ]
