from rest_framework import serializers
from .models import Product
from user_auth.serializers import UserAccountSerializer

class ProductSerializer(serializers.ModelSerializer):
    useraccount = UserAccountSerializer
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description', 'price', 'itemType', 'useraccount',)