# Generated by Django 4.2.7 on 2023-11-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outlook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='Contact',
            new_name='phone_number',
        ),
    ]
