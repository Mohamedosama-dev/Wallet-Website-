# Generated by Django 5.1.1 on 2024-09-18 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_charity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charity',
            name='address',
        ),
        migrations.RemoveField(
            model_name='charity',
            name='description',
        ),
    ]
