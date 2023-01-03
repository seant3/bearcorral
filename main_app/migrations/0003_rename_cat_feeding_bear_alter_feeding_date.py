# Generated by Django 4.1.4 on 2022-12-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='cat',
            new_name='bear',
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
    ]
