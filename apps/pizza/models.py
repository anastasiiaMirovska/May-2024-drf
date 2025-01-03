from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.pizza_shop.models import PizzaShopModel


class DaysChoices(models.TextChoices):
    MONDAY = 'Monday',
    TUESDAY = 'Tuesday',
    WEDNESDAY = 'Wednesday',
    THURSDAY = 'Thursday',
    FRIDAY = 'Friday',
    SATURDAY = 'Saturday',
    SUNDAY = 'Sunday'


class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
        ordering = ('id',) # Це робиться для того, щоб завжди був визначений порядок сортування (дані в базі можуть зберігатись в хаотичному порядку і під час пагінації може виникнути збій, наприклад, відобразиться двічі один і той самий об'єкт
    name = models.CharField(max_length=20, validators=[V.MinLengthValidator(1), V.MaxLengthValidator(100)])
    size = models.IntegerField(validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)])
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices)

    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')


