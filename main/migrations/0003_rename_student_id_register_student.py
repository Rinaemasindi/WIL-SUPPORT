# Generated by Django 4.1.3 on 2022-11-09 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_register_document_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='student_id',
            new_name='student',
        ),
    ]
