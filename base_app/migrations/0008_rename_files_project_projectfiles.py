# Generated by Django 4.0.2 on 2022-03-03 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0007_remove_designation_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='files',
            new_name='projectfiles',
        ),
    ]
