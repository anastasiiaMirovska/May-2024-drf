# Generated by Django 5.1.4 on 2025-01-03 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_alter_pizzamodel_name_alter_pizzamodel_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzamodel',
            name='size',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('^[A-Z][a-z]{,19}$', 'Only alpha characters are allowed. First character must be uppercase.')]),
        ),
    ]
