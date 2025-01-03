# Generated by Django 5.1.4 on 2025-01-02 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_pizzamodel_pizza_shop'),
        ('pizza_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzamodel',
            name='pizza_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='pizza_shop.pizzashopmodel'),
        ),
    ]
