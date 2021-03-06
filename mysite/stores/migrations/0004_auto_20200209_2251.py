# Generated by Django 2.2 on 2020-02-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_store_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.CharField(choices=[('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'), ('Uttara', 'Uttara'), ('Azampur', 'Azampur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'), ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'), ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')], default='Farmgate', max_length=200),
        ),
    ]
