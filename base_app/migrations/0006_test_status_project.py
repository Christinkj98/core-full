# Generated by Django 4.0.2 on 2022-03-02 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_project_tester'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_status',
            name='project',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statusproject', to='base_app.project'),
        ),
    ]