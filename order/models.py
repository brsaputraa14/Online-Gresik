from django.db import models
from django.contrib.auth.models import User
from store.models import Product,VariationValue
from payment.models import Billingaddress

# Create your models here.

status = (
	(1,'Pesanan sedang diajukan'),
	(2,'Pesanan sedang dikemas'),
	(3,'Pesanan sedang diantar'),
    (4,'Pesanan sudah sampai'),
    (5,'Pesanan telah diambil'),
)

class Cart(models.Model):
    code = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'cart')
    item = models.ForeignKey(Product, on_delete = models.CASCADE,related_name = 'items')
    quantity = models.IntegerField(default=1)
    jenis = models.CharField(max_length=100,default="Tidak ada",blank=True,null=True)
    catatan = models.CharField(max_length=100,blank=True,null=True)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} x {self.item}'
    
    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total

    def variation_single_price(self):
        jeniss = VariationValue.objects.filter(variation="jenis",product=self.item)
        for jenis in jeniss:
            if jeniss.exists():
                if jenis.name == self.jenis:
                    total = jenis.price + self.item.price
                    net_total = total
                    float_total = format(net_total, '0.2f')
                    return float_total
            else:
                if jenis.name == self.jenis:
                    total = jenis.price + self.item.price
                    float_total = format(total, '0.2f')
                    return float_total

    def variation_total(self):
        jeniss = VariationValue.objects.filter(variation="jenis",product=self.item)
        for jenis in jeniss:
            if jeniss.exists():
                for jenis in jeniss:
                    if jenis.name == self.jenis:
                        sub_total = jenis.price + self.item.price
                        total = sub_total * self.quantity
                        net_total = total  
                        float_total = format(net_total, '0.2f')
                        return float_total
            else:
                if jenis.name == self.jenis:
                    sub_total = jenis.price + self.item.price
                    total = sub_total * self.quantity
                    float_total = format(total, '0.2f')
                    return float_total



    

class Order(models.Model):
    PAYMENT_METHOD = (
        ('Cash on delivery', 'Cash on Delivery'),
        ('Dana "fake payment" ', 'Dana "fake payment" '),
    )
    code = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    orderitems = models.ManyToManyField(Cart,related_name = 'cartt')
    catatan = models.TextField(blank=True,null=True)
    total_harga = models.CharField(max_length=100,blank=True,null=True)
    ordered = models.BooleanField(default=False)
    status = models.IntegerField(choices=status,default="1")
    created = models.DateTimeField(auto_now_add=True)
    paymentid = models.CharField(max_length=255,blank=True,null=True)
    orderid = models.CharField(max_length=255,blank=True,null=True)
    payment_method = models.CharField(max_length=30,choices=PAYMENT_METHOD,default="Cash on delivery",verbose_name="Metode pembayaran")

    def __str__(self):
        return f'{self.code} {self.user} metode {self.payment_method} in {self.created}'

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            if order_item.variation_total():
                total += float(order_item.variation_total())
            elif order_item.variation_single_price():     
                total += float(order_item.variation_single_price())
            else:
                total += float(order_item.get_total())
        return total

    def total_item(self):
        if self.orderitems.all():
            for order_item in self.orderitems.all():
                awal = order_item.item.price * order_item.quantity
                total = awal 
                net_total = total  
                float_total = format(net_total, '0.2f')
                
            return float_total
            
        else:
            return 0

class harga(models.Model):
    oder = models.ForeignKey(User, on_delete = models.CASCADE)