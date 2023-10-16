from django.db import models

# Create your models here.


# capacity
# shipment
# orders

statusOfProd = (
                ('1', 'arrival'),
                ('2', 'in-store'),
                ('3', 'dispatch'),
                )
PRODUCT_CATEGORIES = (
                    ('Books', 'Books'),
                    ('Beauty', 'Beauty'),
                    ('Home', 'Home'),
                    ('Automotive', 'Automotive'),
                    ('Pets', 'Pets'),
                    ('Health', 'Health'),
                    ('Jewelry', 'Jewelry'),
                    ('Music', 'Music'),
                    ('Movies', 'Movies'),
                    ('Office', 'Office'),
                    ('Outdoor', 'Outdoor'),
                    ('Furniture', 'Furniture'),
                    ('Gaming', 'Gaming'),
                    ('Sports', 'Sports'),
                    ('Electronics', 'Electronics'),
                    ('Food', 'Food'),
                    ('Tools', 'Tools'),
                    ('Clothing', 'Clothing'),
                    ('Shoes', 'Shoes'),
                    ('Toys', 'Toys'),
                    ('null', 'null'),
                )
# "products": [{
# 		"status": "<arrival/in-store/dispatch>",
# 		"name": "<product name>",
# 		"quantity": "<quantity>",
# 		"arrival_date": "<arrival date>",
# 		"dispatch_date": "<dispatch date>"
# 	}]

class Product(models.Model) :
    products_id = models.AutoField(primary_key=True)

    products_status = models.CharField(max_length=1, choices=statusOfProd)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=15, choices=PRODUCT_CATEGORIES, default='null')
    SKU = models.CharField(max_length=20)

    quantity = models.IntegerField()

    arrival_date = models.DateField()
    dispatch_date = models.DateField()

    #shipment -> number of dispatches
    #order -> number of 
    def __str__(self):
        return self.name

# register this schema in admin.py of manager

#ware house capacity

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()  # This field represents the capacity of the warehouse

    def __str__(self):
        return self.name