# Generated by Django 2.2.13 on 2022-04-12 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0003_book_b_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='B_id',
        ),
    ]