# Generated by Django 5.0.1 on 2024-02-04 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6)),
                ('type', models.CharField(choices=[('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')], max_length=7)),
                ('birth', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
    ]
