# Generated by Django 2.2.5 on 2019-10-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
