# Generated by Django 3.2.13 on 2022-05-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='preferences',
            field=models.CharField(default='', max_length=511),
        ),
    ]