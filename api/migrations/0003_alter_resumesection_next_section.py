# Generated by Django 4.2.1 on 2023-05-22 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_sectionformat_owner_alter_resumesection_next_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumesection',
            name='next_section',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.resumesection'),
        ),
    ]
