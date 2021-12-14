from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=88)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'    

class Product(models.Model):
    product_name = models.CharField(max_length=99)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'   
