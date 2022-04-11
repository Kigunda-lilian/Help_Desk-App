<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 4.0.3 on 2022-04-08 01:58
=======
# Generated by Django 4.0.3 on 2022-04-07 07:58
>>>>>>> modelslil
=======
# Generated by Django 4.0.3 on 2022-04-09 21:50
>>>>>>> development

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
<<<<<<< HEAD
            name='Post',
=======
            name='Comments',
>>>>>>> modelslil
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('question', models.TextField(max_length=280)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null='False', on_delete=django.db.models.deletion.PROTECT, related_name='user_images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
        migrations.CreateModel(
=======
>>>>>>> development
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('stage', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=50, null='False')),
                ('Description', models.TextField()),
                ('logical', models.BooleanField(default=True)),
                ('technical', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> development
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_pic', models.ImageField(default='default.png', upload_to='images/')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
<<<<<<< HEAD
=======
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='default.png', upload_to='images/')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
=======
>>>>>>> development
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('question', models.TextField(max_length=280)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('comment', models.IntegerField(blank=True, default=True, null=True)),
                ('postslikes', models.IntegerField(blank=True, default=True, null=True)),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('tag_title', models.ForeignKey(null='False', on_delete=django.db.models.deletion.PROTECT, to='helpdesk.tag')),
                ('user', models.ForeignKey(null='False', on_delete=django.db.models.deletion.PROTECT, related_name='user_images', to=settings.AUTH_USER_MODEL)),
<<<<<<< HEAD
>>>>>>> modelslil
=======
>>>>>>> development
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='like', max_length=70)),
                ('user', models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reply', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.post')),
                ('user', models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
