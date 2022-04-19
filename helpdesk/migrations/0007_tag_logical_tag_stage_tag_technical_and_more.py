# Generated by Django 4.0.3 on 2022-04-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0006_alter_dislike_response_alter_like_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='logical',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='stage',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='technical',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='response',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], max_length=70, null=True),
        ),
    ]
