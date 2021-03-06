# Generated by Django 3.0.7 on 2020-07-04 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hkman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithDraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(default=0)),
                ('method', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('hkman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hkman.HKMan')),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('hkman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hkman.HKMan')),
            ],
        ),
    ]
