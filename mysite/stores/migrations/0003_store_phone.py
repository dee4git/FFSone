# Generated by Django 2.2 on 2020-02-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20200129_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='phone',
            field=models.CharField(default='01719588000', max_length=200),
        ),
    ]