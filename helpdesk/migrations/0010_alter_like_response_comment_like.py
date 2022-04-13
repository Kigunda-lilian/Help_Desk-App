# Generated by Django 4.0.3 on 2022-04-13 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0009_comment_comment_dislikes_alter_like_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='like', max_length=70),
        ),
        migrations.CreateModel(
            name='Comment_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='comment_like', max_length=70)),
                ('user', models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
