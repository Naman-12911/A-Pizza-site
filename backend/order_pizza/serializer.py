from rest_framework import serializers
from .models import product,cart
# creating API of the pizza.
class  pizza_choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  product
        fields=('id','name', 'price', 'size','image', 'timeStamps')
class  pizza_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
class  cart_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  cart
        fields=('pizza_name','Number_of_pizza','Grand_total')