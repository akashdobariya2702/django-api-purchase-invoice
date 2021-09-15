from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework import serializers, generics, permissions, viewsets, status, filters
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import *
# from api.functions import *

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all().order_by('-id')
    serializer_class = PurchaseOrderSerializer

    @action(methods=['GET'], detail=True)
    def invoice(self, request, pk=None):
        obj = self.get_object()

        data = self.request.data

        jsondata =  model_to_dict( obj )
        jsondata["created_at"] = str(obj.created_at.date())
        jsondata["seller"] = obj.company.name
        jsondata["product_name"] = obj.product.name

        print(jsondata)
        return render(request, 'api/invoice.html', jsondata)
