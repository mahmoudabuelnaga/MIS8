# Generated by Django 2.2.11 on 2020-05-10 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20200510_0429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='appartment_address',
            new_name='apartment_address',
        ),
    ]
