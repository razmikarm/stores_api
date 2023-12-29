from rest_framework import serializers
from .models import Product, Store


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('__all__')



class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = ('id', 'address', 'capacity', 'products')
