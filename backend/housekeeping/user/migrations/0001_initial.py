# Generated by Django 3.0.7 on 2020-07-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('salt', models.CharField(blank=True, default='', max_length=128)),
                ('real_name', models.CharField(default='', max_length=20)),
                ('sex', models.BooleanField(default=True)),
                ('phone', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
