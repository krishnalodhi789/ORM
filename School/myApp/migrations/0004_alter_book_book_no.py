# Generated by Django 5.0 on 2023-12-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_book_id_remove_book_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_no',
            field=models.IntegerField(),
        ),
    ]
