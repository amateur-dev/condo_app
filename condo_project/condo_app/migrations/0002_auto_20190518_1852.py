# Generated by Django 2.2.1 on 2019-05-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]