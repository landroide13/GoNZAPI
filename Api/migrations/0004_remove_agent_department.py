# Generated by Django 4.1 on 2022-08-23 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_remove_agent_position_agent_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='department',
        ),
    ]
