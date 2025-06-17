from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=3)

    #customized validation
    def validate_name(sef,value):
        available_at = Product.objects.filter(name__iexact=value).exists()

        if available_at:
            raise serializers.ValidationError("This product already exists")
        return value


    class Meta:
        model = Product
        fields = '__all__'
        # read_only_fields = ('') #solo para leer  y no editar

