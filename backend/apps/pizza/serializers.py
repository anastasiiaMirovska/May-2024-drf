from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'size', 'price', 'day', 'pizza_shop_id', 'updated_at', 'created_at')

    def create(self, validated_data):
        return PizzaModel.objects.create(**validated_data, pizza_shop_id=1)

    # def validate_size(self, size): # Така валідація проходить тільки після того, як вхідні дані були провалідовані у model і в серіалайзері
    #     if size <= 0:
    #         raise ValidationError('Size must be greater than 0')
    #     return size
    #
    # def validate(self, attrs):
    #     price = attrs.get('price')
    #     size = attrs.get('size')
    #     if size == price:
    #         raise ValidationError('Price cannot be equal to size')
    #     return attrs



class PizzaPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('photo',)


class PizzaResponseSerializer(serializers.Serializer):
    details = serializers.CharField(default="hello")