# Generated by Django 5.0 on 2023-12-08 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClasses',
            fields=[
                ('class_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('roll_no', models.IntegerField(unique=True)),
                ('age', models.IntegerField()),
                ('studentclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.schoolclasses')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30, unique=True)),
                ('book_no', models.IntegerField()),
                ('author_name', models.CharField(max_length=30)),
                ('student', models.ManyToManyField(to='myApp.student')),
            ],
        ),
    ]
