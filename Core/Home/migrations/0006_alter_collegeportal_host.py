# Generated by Django 5.0.7 on 2024-08-05 11:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_collegeportal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeportal',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
