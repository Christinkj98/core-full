# Generated by Django 4.0.2 on 2022-03-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_rename_leave_applyleave'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_taskassign',
            name='extension_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
