# Generated by Django 4.0.4 on 2023-01-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_requestersrequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderrequest',
            name='applied',
            field=models.BooleanField(default=False),
        ),
    ]
