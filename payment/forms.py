from django import forms

from .models import Billingaddress
from order.models import Order
class Billingaddressform(forms.ModelForm):
    class Meta:
        model = Billingaddress
        fields = ['first_name','last_name','address1','address2','city','zipcode','phone_number']

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20, blank=True,null=True)
    # last_name = models.CharField(max_length=20, blank=True,null=True)
    # address = models.TextField(verbose_name="Alamat")
    # city = models.CharField(max_length=100, blank=True,null=True, verbose_name="Kota")
    # zipcode = models.CharField(max_length=15, blank=True,null=True, verbose_name='Kode pos')
    # phone_number = models.CharField(max_length=16,blank=True,null=True,verbose_name="Nomor Telepon")

class PaymentMethod(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
