# Generated by Django 2.2.1 on 2019-05-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condo_app', '0006_auto_20190520_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condo',
            name='name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='condo_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
