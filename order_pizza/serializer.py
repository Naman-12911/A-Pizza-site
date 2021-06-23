from rest_framework import serializers
from .models import product
# creating API of the pizza.
class  pizza_choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  product
        fields=('id','name', 'price', 'size','image', 'timeStamps')