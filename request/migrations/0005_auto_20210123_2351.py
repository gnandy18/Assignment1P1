# Generated by Django 3.1.5 on 2021-01-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_auto_20210123_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='nuid',
            field=models.CharField(max_length=8),
        ),
    ]