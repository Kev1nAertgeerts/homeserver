# Generated by Django 4.2.5 on 2024-02-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitvavo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sec',
            name='crypto_gr_key',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sec',
            name='key',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sec',
            name='sec',
            field=models.CharField(max_length=200),
        ),
    ]
