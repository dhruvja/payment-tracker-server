from django.db import models

# Create your models here.

class Payment(models.Model): 
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    payment_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
