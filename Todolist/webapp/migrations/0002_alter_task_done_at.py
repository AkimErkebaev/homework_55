# Generated by Django 4.0.5 on 2022-06-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
