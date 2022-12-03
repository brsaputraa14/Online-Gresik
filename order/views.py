from django.shortcuts import render,get_object_or_404,redirect
from store.models import Product
from .models import Cart,Order
from coupon.forms import Couponcodeforms
from coupon.models import Coupon        
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
def operator(user):
    return user.groups.filter(name='operator').exists()
# Create your views here.
@login_required(login_url='/account/login')
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item = item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_item2 = get_object_or_404(Cart.objects.filter(item = item,user=request.user,purchased=False))

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            jenis = request.POST.get('jenis')
            quantity = request.POST.get('quantity')
            # proses handle stok
            if quantity:
                if item.stok > int(quantity):
                    print(quantity +"stok kurang dari 200 atau sama dengan")
                    order_item[0].quantity += int(quantity)
                    item.stok -= int(quantity)
                    item.save()
                    messages.success(request,'Pesanan kamu telah masuk kedalam keranjang!')


                if item.stok == int(quantity) or item.stok > int(quantity) and item.stok < 0:
                    print(quantity +"sama aja tapi sama sama stok kurang dari 200 atau sama dengan")
                    order_item[0].quantity = order_item[0].quantity - 200 + order_item[0].quantity
                    order_item[0].quantity += int(quantity) 
                    item.stok -= int(quantity)
                    item.save()
                    messages.success(request,'Waah terima kasih telah memborong habis pesanan ini')

                if item.stok < int(quantity) and item.stok == int(quantity) :
                    print(quantity  + "else dari stok kurang dari 200 atau sama dengan")
                    order_item[0].quantity = order_item[0].quantity 
                    item.stok = item.stok
                    item.status = True
                    item.save()
                    messages.error(request,'Maaf stok tidak mencukupi!')


                if item.stok <= 0 and item.stok > int(quantity):
                    print("stok habis")
                    order_item[0].quantity = order_item[0].quantity 
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.error(request,'Saat ini stok dari pesanan telah habis!')
                
            else:
                if item.stok <= 200 :
                    order_item[0].quantity += 1
                    item.stok -= int(1)
                    item.save()
                else:
                    order_item[0].quantity 
                    item.stok
                    item.status = False
                    item.save()
            # program kalau kurang dari 0 stoknya
            if item.stok < 0 or item.stok < order_item2.quantity:
                order_item[0].quantity += int(quantity)
                item.status = False
                item.save()

            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
            order_item[0].save()
            return redirect('makanan_ma')
        else:
            jenis = request.POST.get('jenis')
            if jenis:
                order_item[0].jenis = jenis 
            else:
                if item.stok <= 200 or item.stok <= int(quantity):
                    item.stok -= int(1)
                    item.save()
                else:
                    item.status = False
                    item.save()
            order.orderitems.add(order_item[0])
            return redirect('makanan_ma')

    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('makanan_ma')
@login_required
def add_to_cart_minuman(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item = item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_item2 = get_object_or_404(Cart.objects.filter(item = item,user=request.user,purchased=False))

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            jenis = request.POST.get('jenis')
            quantity = request.POST.get('quantity')
            # proses handle stok
            if quantity:
                if item.stok > int(quantity):
                    print(quantity +"stok kurang dari 200 atau sama dengan")
                    order_item[0].quantity += int(quantity)
                    item.stok -= int(quantity)
                    item.save()
                    messages.success(request,'Pesanan kamu telah masuk kedalam keranjang!')


                if item.stok == int(quantity) or item.stok > int(quantity) and item.stok < 0:
                    print(quantity +"sama aja tapi sama sama stok kurang dari 200 atau sama dengan")
                    order_item[0].quantity = order_item[0].quantity - 200 + order_item[0].quantity
                    order_item[0].quantity += int(quantity) 
                    item.stok -= int(quantity)
                    item.save()
                    messages.success(request,'Waah terima kasih telah memborong habis pesanan ini')

                if item.stok < int(quantity) and item.stok == int(quantity) :
                    print(quantity  + "else dari stok kurang dari 200 atau sama dengan")
                    order_item[0].quantity = order_item[0].quantity 
                    item.stok = item.stok
                    item.status = True
                    item.save()
                    messages.error(request,'Maaf stok tidak mencukupi!')


                if item.stok <= 0 and item.stok > int(quantity):
                    print("stok habis")
                    order_item[0].quantity = order_item[0].quantity 
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.error(request,'Saat ini stok dari pesanan telah habis!')
                
            else:
                if item.stok <= 200 :
                    order_item[0].quantity += 1
                    item.stok -= int(1)
                    item.save()
                else:
                    order_item[0].quantity 
                    item.stok
                    item.status = False
                    item.save()
            # program kalau kurang dari 0 stoknya
            if item.stok < 0 or item.stok < order_item2.quantity:
                order_item[0].quantity += int(quantity)
                item.status = False
                item.save()

            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
            order_item[0].save()
            return redirect('minuman_mi')
        else:
            jenis = request.POST.get('jenis')
            if jenis:
                order_item[0].jenis = jenis 
            else:
                if item.stok <= 200 or item.stok <= int(quantity):
                    item.stok -= int(1)
                    item.save()
                else:
                    item.status = False
                    item.save()
            order.orderitems.add(order_item[0])
            return redirect('minuman_mi')

    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('minuman_mi')

def add_to_cart_home(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item = item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_item2 = get_object_or_404(Cart.objects.filter(item = item,user=request.user,purchased=False))

    if order_qs:
        order = order_qs[0]
        if order.orderitems.filter(item=item):
            jenis = request.POST.get('jenis')
            quantity = request.POST.get('quantity')
            if quantity:
                order_item[0].quantity += int(1)
    
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                
                if item.stok < order_item2.quantity:
                    item.stok = item.stok
                    item.save()

                if item.stok <= 0:
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.warning(request,'Saat ini stok dari pesanan telah habis!')

                
            else:
                order_item[0].quantity += 1
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                if item.stok <= 0:
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.warning(request,'Saat ini stok dari pesanan telah habis!')

            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
            order_item[0].save()
            return redirect('makanan_ma')
        else:
            jenis = request.POST.get('jenis')
            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                else:
                    item.status = False
                    item.save()
            order.orderitems.add(order_item[0])
            return redirect('makanan_ma')

    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('makanan_ma')
@login_required        
def add_to_cart_home_home(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item = item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_item2 = get_object_or_404(Cart.objects.filter(item = item,user=request.user,purchased=False))

    if order_qs:
        order = order_qs[0]
        if order.orderitems.filter(item=item):
            jenis = request.POST.get('jenis')
            quantity = request.POST.get('quantity')
            if quantity:
                order_item[0].quantity += int(1)
    
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                
                if item.stok < order_item2.quantity:
                    item.stok = item.stok
                    item.save()

                if item.stok <= 0:
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.warning(request,'Saat ini stok dari pesanan telah habis!')

                
            else:
                order_item[0].quantity += 1
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                if item.stok <= 0:
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.warning(request,'Saat ini stok dari pesanan telah habis!')

            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
            order_item[0].save()
            return redirect('home')
        else:
            jenis = request.POST.get('jenis')
            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                else:
                    item.status = False
                    item.save()
            order.orderitems.add(order_item[0])
            return redirect('home')

    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('home')
@login_required
def add_to_cart_home_minuman(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item = item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_item2 = get_object_or_404(Cart.objects.filter(item = item,user=request.user,purchased=False))

    if order_qs:
        order = order_qs[0]
        if order.orderitems.filter(item=item):
            jenis = request.POST.get('jenis')
            quantity = request.POST.get('quantity')
            if quantity:
                order_item[0].quantity += int(1)
    
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                
                if item.stok < order_item2.quantity:
                    item.stok = item.stok
                    item.save()

                if item.stok <= 0:
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.warning(request,'Saat ini stok dari pesanan telah habis!')

                
            else:
                order_item[0].quantity += 1
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                if item.stok <= 0:
                    item.stok = item.stok
                    item.status = False
                    item.save()
                    messages.warning(request,'Saat ini stok dari pesanan telah habis!')

            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
            order_item[0].save()
            return redirect('minuman_mi')
        else:
            jenis = request.POST.get('jenis')
            if jenis:
                order_item[0].jenis = jenis 
            else:
                order_item[0]
                if item.stok > 0 or item.stok >= order_item2.quantity:
                    item.stok -= int(1)
                    item.save()
                else:
                    item.status = False
                    item.save()
            order.orderitems.add(order_item[0])
            return redirect('minuman_mi')

    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('minuman_mi')

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user,purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)

    if carts.exists()and orders.exists():
        order = orders[0]
        coupon_form = Couponcodeforms(request.POST)
        if coupon_form.is_valid():
            current_time = timezone.now()
            code = coupon_form.cleaned_data.get('code')
            coupon_obj = Coupon.objects.get(code=code)
            if coupon_obj.valid_to >= current_time and coupon_obj.active == True:
                get_discount = (coupon_obj.discount / 100) * order.get_totals()
                total_price_after_discount = order.get_totals() - get_discount
                request.session['discount_total'] = total_price_after_discount
                request.session['coupon_code'] = code

                return redirect ('order:cart')
            else:
                return redirect('order:cart')
        total_price_after_discount = request.session.get('discount_total')
        coupon_code = request.session.get('coupon_code')
        context = {
            'cart':carts,
            'order':order,
            'coupon_form':coupon_form,
            'coupon_code': coupon_code,
            'total_price_after_discount': total_price_after_discount

        }

    return render(request,'cart.html',context)
@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists:
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity >= 0 or item.stok >= 0:
                order_item.quantity += 1
                order_item.save()
                item.stok -= 1
                item.save()
                return redirect('order:cart')
        else:
            return redirect('home')
    else:
        return redirect('home')
@login_required       
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists:
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity -= 1
                order_item.save()
                item.stok += 1
                item.save()
                return redirect('order:cart')
        else:
            return redirect('home')
    else:
        return redirect('home')
@login_required
def delete_cart(request,pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists:
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 0 and order_item.quantity <= 200:
                item.stok += order_item.quantity
                item.status = True
                order_item.delete()
                item.save()
                messages.success(request,'Anda telah berhasil menghapus pesanan dari dalam keranjang!')

                return redirect('minuman_mi')

            if order_item.quantity >= 200 or item.stok <= 0:
                item.stok = 200
                item.status = True
                order_item.delete()
                item.save()
                messages.success(request,'Anda telah berhasil menghapus pesanan dari dalam keranjang!')

        else:
            return redirect('minuman_mi')
    else:
        return redirect('minuman_mi')
@login_required
def delete_cart_home(request,pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists:
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 0 and order_item.quantity < 200:
                item.stok += order_item.quantity
                item.status = True
                order_item.delete()
                item.save()
                messages.success(request,'Anda telah berhasil menghapus pesanan dari dalam keranjang!')
                return redirect('makanan_ma')

            if order_item.quantity >= 200 or item.stok <= 0:
                item.stok = 200
                item.status = True
                order_item.delete()
                item.save()
                messages.success(request,'Anda telah berhasil menghapus pesanan dari dalam keranjang!')
                return redirect('makanan_ma')

            
        else:
            return redirect('makanan_ma')
    else:
        return redirect('makanan_ma')
@login_required
def delete_cart_home_home(request,pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists:
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 0 and order_item.quantity < 200:
                item.stok += order_item.quantity
                item.status = True
                order_item.delete()
                item.save()
                messages.success(request,'Anda telah berhasil menghapus pesanan dari dalam keranjang!')
                return redirect('home')

            if order_item.quantity >= 200 or item.stok <= 0:
                item.stok = 200
                item.status = True
                order_item.delete()
                item.save()
                messages.success(request,'Anda telah berhasil menghapus pesanan dari dalam keranjang!')
                return redirect('home')

            
        else:
            return redirect('home')
    else:
        return redirect('home')
