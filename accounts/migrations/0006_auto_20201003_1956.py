# Generated by Django 3.1.2 on 2020-10-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201003_1952'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ord',
            new_name='Order',
        ),
    ]
