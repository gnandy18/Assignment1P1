# Generated by Django 3.1.5 on 2021-01-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20210123_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='approval',
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Ready', 'Ready'), ('Delivered', 'Delivered')], default='New', max_length=10),
        ),
    ]
