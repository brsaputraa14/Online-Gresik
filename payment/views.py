from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Billingaddress
from django.urls import reverse
# Create your views here.
from .forms import Billingaddressform,PaymentMethod
from order.models import Cart,Order
from store.models import Product
from django.views.generic import TemplateView
from datetime import datetime,timezone
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
def operator(user):
    return user.groups.filter(name='operator').exists()

class CheckoutTemplateView(TemplateView):   
    def get(self,request,*args,**kwargs):
        saved_address = Billingaddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = Billingaddressform(instance=saved_address)
        paymen_method = PaymentMethod()



        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_total = order_qs[0].get_totals()

        context = {
            'billing_address': form,
            'order_item' : order_item,
            'order_total' : order_total,
            'payment_method':paymen_method

        }
        return render(request, 'checkout.html',context)

    def post(self,request,*args,**kwargs):
        saved_address = Billingaddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = Billingaddressform(instance=saved_address)
        trig = Product.objects.filter(items__user=request.user,items__purchased=False)[0]
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethod(instance=payment_obj)
        if request.method == 'post' or request.method == 'POST':
            form = Billingaddressform(request.POST, instance=saved_address)
            pay_form = PaymentMethod(request.POST, instance=payment_obj)
            catatan = request.POST.get('catatan')
            total_harga = request.POST.get('total_harga')
            if form.is_valid() and pay_form.is_valid():
                form.save()
                pay_method = pay_form.save()

                if not saved_address.is_fully_filled():
                    return redirect('checkout')     


                if pay_method.payment_method == 'Cash on delivery':
                    cart_itemso = Cart.objects.filter(user=request.user, purchased=False)[0]
                    pref = datetime.now().year + datetime.now().year
                    code = 'ST' + str(datetime.now().day)+str(datetime.now().second) + str(pref) 

                    if trig.stok < 0:
                        cart_items = Cart.objects.filter(user=request.user, purchased=False)
                        order_qs = Order.objects.filter(user=request.user, ordered=False)
                        order = order_qs[0]
                        order.ordered = False
                        order.orderid = order.pk
                        order.paymentid = pay_method.payment_method
                        order.save()
                        cart_items = Cart.objects.filter(user=request.user, purchased=False)
                        for item in cart_items:
                            item.purchased = False
                            item.save()
                        print('Order submited successfully')
                        return redirect('home')
                    else:
                        cart_items = Cart.objects.filter(user=request.user, purchased=False)
                        order_qs = Order.objects.filter(user=request.user, ordered=False)
                        pref = datetime.now().year 
                        code = 'ST' + str(datetime.now().day)+str(datetime.now().second) + str(pref) 
                        order = order_qs[0]
                        order.total_harga = str(total_harga)
                        order.catatan = str(catatan)
                        order.code = code 
                        order.ordered = True
                        order.orderid = order.pk
                        order.paymentid = pay_method.payment_method
                        order.save()
                        cart_items = Cart.objects.filter(user=request.user, purchased=False)
                        for item in cart_items:
                            item.catatan = str(catatan)
                            item.code = code
                            item.purchased = True
                            item.save()
                        
                        messages.success(request,'Terima Kasih telah berbelanja di warung makan kami')
                        return redirect('home')
                  


