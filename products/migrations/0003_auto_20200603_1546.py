# Generated by Django 3.0.6 on 2020-06-03 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200522_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tovar',
            options={'ordering': ['-id', '-name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
