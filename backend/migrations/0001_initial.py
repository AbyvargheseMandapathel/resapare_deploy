# Generated by Django 4.0.6 on 2022-08-02 17:17

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
            name='Topic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('image', models.URLField(default=None)),
                ('wide_image', models.URLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('option_no', models.IntegerField(default=0)),
                ('option', models.CharField(max_length=55)),
                ('count', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.topic')),
            ],
            options={
                'unique_together': {('topic', 'option_no')},
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.choice')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'choice', 'topic')},
            },
        ),
    ]
