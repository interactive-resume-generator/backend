# Generated by Django 4.2.1 on 2023-05-23 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_resume_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='owner',
        ),
    ]