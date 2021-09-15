# python library

# django library
from rest_framework import serializers

# plugin library

# project library
from api.models import *

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    invoice_url = serializers.SerializerMethodField()

    def get_invoice_url(self, obj):
        return "http://127.0.0.1:8000/api/purchase-order/"+str(obj.id)+"/invoice/"

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ('order_number', 'rate', 'total_price')
