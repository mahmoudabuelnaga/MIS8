# Generated by Django 2.2.11 on 2020-05-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200511_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
