# Generated by Django 4.2.6 on 2024-03-30 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='department',
        ),
    ]
