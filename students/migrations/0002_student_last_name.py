# Generated by Django 5.0.4 on 2024-04-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]