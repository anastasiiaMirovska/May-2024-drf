from rest_framework import serializers

from pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = (
            'id',
            'name',
            'size',
            'price',
            'sweet',
        )

    # def create(self, validated_data):
    #     pizza = PizzaModel.objects.create(**validated_data)
    #     # pizza.sweet = "True"
    #     return pizza

