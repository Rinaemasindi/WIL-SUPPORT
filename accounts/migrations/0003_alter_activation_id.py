# Generated by Django 4.1.2 on 2022-11-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180616_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
