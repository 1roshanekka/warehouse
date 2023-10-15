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
    
    SKU = models.CharField(max_length=20)

    quantity = models.IntegerField()
    arrival_date = models.DateField()
    dispatch_date = models.DateField()

    def __str__(self):
        return self.name

# register this schema in admin.py of manager