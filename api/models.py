from django.db import models
from datetime import datetime, date, time, timedelta

class CreateModifiedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Company(CreateModifiedModel):
    """List of all companies."""
    name = models.CharField(max_length = 50, unique=True)
    gst = models.CharField(max_length = 50)

    def __str__(self):
        return "%s: %s" %(self.id, self.name)

    class Meta:
        app_label           = 'api'
        verbose_name        = "Company"
        verbose_name_plural = "Companies"

class Product(CreateModifiedModel):
    """List of all products."""
    name = models.CharField(max_length = 50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return "%s: %s" %(self.id, self.name)

    class Meta:
        app_label           = 'api'
        verbose_name        = "Product"
        verbose_name_plural = "Products"

class PurchaseOrder(CreateModifiedModel):
    """List of all orders."""
    order_number = models.CharField(max_length = 50, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0, blank=True, null=True)
    qty = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(default=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        pk_value = self.pk
        if not pk_value:
            cur_year = datetime.now().year
            total_cur_year_orders = PurchaseOrder.objects.filter(created_at__year=cur_year).count()

            self.order_number = "PO/"+str(cur_year)+"/"+str(total_cur_year_orders)

            self.company = self.product.company
            self.rate = self.product.cost
            self.total_price = self.rate * self.qty
        super(PurchaseOrder, self).save(*args, **kwargs)

    def __str__(self):
        return "%s: %s" %(self.id, self.order_number)

    class Meta:
        app_label           = 'api'
        verbose_name        = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
