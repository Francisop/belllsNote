# Generated by Django 3.1.4 on 2020-12-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20201228_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(default='2020 jan 12 12:00'),
        ),
    ]