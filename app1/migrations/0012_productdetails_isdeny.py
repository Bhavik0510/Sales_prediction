# Generated by Django 2.1.5 on 2021-03-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20210302_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='isDeny',
            field=models.BooleanField(default=False),
        ),
    ]
