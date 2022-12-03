from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True,verbose_name="Kupon Diskon")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Kode Kupon"

    def __str__(self):
        return f"{self.code} Diskon: {self.discount}%"
