# Generated by Django 2.0.5 on 2019-04-20 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapplication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='days',
        ),
        migrations.RemoveField(
            model_name='workhour',
            name='emp_name',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
        migrations.DeleteModel(
            name='Workhour',
        ),
    ]