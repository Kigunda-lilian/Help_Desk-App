# Generated by Django 4.0.3 on 2022-04-09 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag_title',
        ),
    ]
