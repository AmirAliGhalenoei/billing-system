from django.db import models
from django.db.models import Sum
from django.core.validators import MaxValueValidator, MinValueValidator


class Invoice(models.Model):
    created = models.DateField(auto_now_add=True)

    @property
    def total_invoice(self):
        return self.items.aggregate(total=Sum("total_amount"))["total"] or 0

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=256)
    quantity = models.PositiveBigIntegerField()
    price = models.BigIntegerField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    total_amount = models.PositiveBigIntegerField(editable=False)
    
    def save(self, *args, **kwargs):
        amount = self.quantity * self.price
        if self.discount:
            amount = amount * (1 - self.discount / 100)
        self.total_amount = int(amount)
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.title


