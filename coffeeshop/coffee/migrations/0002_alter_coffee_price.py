# Generated by Django 5.0.6 on 2024-05-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
