# Generated by Django 4.0.3 on 2022-04-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_alter_like_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='like', max_length=70),
        ),
    ]
