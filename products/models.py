from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Batch(models.Model):
    supplier = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=100)
    production_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    origin = models.CharField(max_length=100)

    def __str__(self):
        return f"Batch {self.batch_number} of {self.product.name}"