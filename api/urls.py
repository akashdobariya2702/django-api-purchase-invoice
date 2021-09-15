from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# plugin library

# project library
from api import views

router = DefaultRouter()


router.register(r'company', views.CompanyViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'purchase-order', views.PurchaseOrderViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'api'), namespace='v1')),
]
app_name = 'api'
