# Generated by Django 4.0.5 on 2022-07-11 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_task_type_task_type_alter_type_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='type',
            new_name='types',
        ),
    ]