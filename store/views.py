from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Product,Category,ProductImages
from order.models import Cart,Order
from django.contrib.auth.decorators import login_required
from order.forms import pembelianform
from .forms import productforms 
from datetime import datetime,timezone
from django.contrib import messages
from payment.models import Billingaddress
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
def operator(user):
    return user.groups.filter(name='operator').exists()
def kurir(user):
    return user.groups.filter(name='kurir').exists()

# class HomeListView(ListView):
#     model = Product``
#     template_name = 'index.html'
#     context_object_name = 'products'

@login_required(login_url='/account/login')
def home (request):
    product = Product.objects.all()
    category = Category.objects.filter(id = 1,parent = None)
    category2 = Category.objects.filter(id = 2,parent = None)
    context = {
        'products':product,
        'cate1':category,
        'cate2':category2,
    }
    return render(request,'index.html',context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'item'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        context['ya'] = Cart.objects.filter(user=self.request.user)
        return context

class MinumanDetailView(DetailView):
    model = Product
    template_name = 'minuman.html'
    context_object_name = 'item'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        context['ya'] = Cart.objects.filter(user=self.request.user)
        return context

@login_required
def productdetail (self,request):
    product = Product.objects.all()
    product_images = ProductImages.objects.filter(product=self.object.id)
    ya = Cart.objects.filter(user=self.request.user)
    context = {
        'item':product,
        'product_images':product_images,
        'ya':ya
    }
    return render(request,'index.html',context)


class MakananListView(ListView):
        model = Product
        template_name = 'mk_makanan.html'
        context_object_name = 'product'

        def get_context_data(self,**kwargs):
            products = Product.objects.filter(tipe='1')
            CATID = self.request.GET.get('category')
            if CATID:
                products = Product.objects.filter(tipe='1',category=CATID)
            else:
                products = Product.objects.filter(tipe='1')
            context = super().get_context_data(**kwargs)    
            context['cate1'] = Category.objects.filter(id = 1,parent = None)
            context['cat'] = Category.objects.filter(parent='1')
            context['products'] = Product.objects.filter(tipe='1')
            return context

class MinumanListView(ListView):
    model = Product
    template_name = 'mn_minuman.html'
    context_object_name = 'product'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['cate2'] = Category.objects.filter(id = 2,parent = None)
        context['cat'] = Category.objects.filter(parent='2')
        context['products'] = Product.objects.filter(tipe='2')

        return context
@login_required        
def minuman_view (request):
    product = Product.objects.all()
    cate2 = Category.objects.filter(id = 2,parent = None)
    category = Category.objects.filter(parent='2')
    products = Product.objects.filter(tipe='2')

    CATID = request.GET.get('category')
    if CATID:
        products = Product.objects.filter(tipe='2',category=CATID)
    else:
        products = Product.objects.filter(tipe='2')

    context = {
        'product':product,
        'cate2':cate2,
        'cat':category,
        'products':products,
    }
    return render(request,'mn_minuman.html',context)
@login_required
def makanan_view (request):
    product = Product.objects.all()
    cate1 = Category.objects.filter(id = 1,parent = None)
    category = Category.objects.filter(parent='1')
    products = Product.objects.filter(tipe='1')

    CATID = request.GET.get('category')
    if CATID:
        products = Product.objects.filter(tipe='1',category=CATID)
    else:
        products = Product.objects.filter(tipe='1')

    context = {
        'product':product,
        'cate1':cate1,
        'cat':category,
        'products':products,
    }
    return render(request,'mk_makanan.html',context)

# def home (request):
    # product = Product.objects.all()
    # context = {
    #     'item':product
    # }
#     return render(request,'index.html',context)

# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     context = {
#         'item':item
#     }

#     return render(request,'product.html',context)

@login_required
def pembelian (request):
    # sales = Product.objects.all()
    # sale_data = []
    # for sale in sales:
    #     data = {}
    #     for field in sale._meta.get_fields(include_parents=False):
    #         if field.related_model is None:
    #             data[field.name] = getattr(sale,field.name)
    #     data['items'] = Product.objects.filter(items__user= request.user).all()
    #     data['item_count'] = len(data['items'])
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    order = Order.objects.filter(created__year=current_year,
        created__month = current_month,
        created__day = current_day,status__lt='5',ordered=True)
    category = Category.objects.filter(id = 1,parent = None)
    category2 = Category.objects.filter(id = 2,parent = None)
    order_qs = Order.objects.filter(user=request.user, ordered=True)
    context = {
        'order_qs':order_qs,
        'order':order,
        'cate1':category,
        'cate2':category2,
    }
    return render(request,'pembelian.html',context)

# @login_required
# def salesList(request):
#     sales = Sales.objects.all()
#     sale_data = []
#     for sale in sales:
#         data = {}
#         for field in sale._meta.get_fields(include_parents=False):
#             if field.related_model is None:
#                 data[field.name] = getattr(sale,field.name)
#         data['items'] = salesItems.objects.filter(sale_id = sale).all()
#         data['item_count'] = len(data['items'])
#         if 'tax_amount' in data:
#             data['tax_amount'] = format(float(data['tax_amount']),'.2f')
#         # print(data)
#         sale_data.append(data)
#     # print(sale_data)
#     context = {
#         'page_title':'Struk',
#         'sale_data':sale_data,
#     }
#     # return HttpResponse('')
#     return render(request, 'posApp/sales.html',context)
@user_passes_test(operator,login_url='home')
def cek_pembelian (request):
    order = Order.objects.filter(status__lt='5',ordered=True)
    category = Category.objects.filter(id = 1,parent = None)
    category2 = Category.objects.filter(id = 2,parent = None)
    order_qs = Order.objects.filter(user=request.user, ordered=True)
    context = {
        'order_qs':order_qs,
        'order':order,
        'cate1':category,
        'cate2':category2,
    }
    return render(request,'cek/cek_pembelian.html',context)

@user_passes_test(kurir,login_url='home')
def cek_pembelian2 (request):
    order = Order.objects.filter(status__lt='5',ordered=True)
    category = Category.objects.filter(id = 1,parent = None)
    category2 = Category.objects.filter(id = 2,parent = None)
    order_qs = Order.objects.filter(user=request.user, ordered=True)
    context = {
        'order_qs':order_qs,
        'order':order,
        'cate1':category,
        'cate2':category2,
    }
    return render(request,'cek/cek_pembelian2.html',context)

# def view_pembelian (request):
#     now = datetime.now()
#     current_year = now.strftime("%Y")
#     current_month = now.strftime("%m")
#     current_day = now.strftime("%d")
#     order = Order.objects.filter(ordered=True)
#     category = Category.objects.filter(id = 1,parent = None)
#     category2 = Category.objects.filter(id = 2,parent = None)
#     order_qs = Order.objects.filter(user=request.user, ordered=True)
#     context = {
#         'order_qs':order_qs,
#         'order':order,
#         'cate1':category,
#         'cate2':category2,
#     }
#     return render(request,'view/pembelian.html',context)


@user_passes_test(operator,login_url='home')
def view_pembelian (request):
    alamat = Billingaddress.objects.all()
    context = {
        'al':alamat
    }

    return render(request, 'alamat/pembeliann.html',context)

@user_passes_test(operator,login_url='home')
def detail_alamat (request,id):
    alamat = Billingaddress.objects.get(pk=id)
    context = {
        'al':alamat
    }

    return render(request, 'alamat/detail_alamat.html',context)

def detail_alamates (request,id):
    user1 = User.objects.get(username='admin')
    alamat = Order.objects.filter(user=user1)
    context = {
        'user1':user1,
        'al':alamat,
    }

    return render(request, 'alamat/detail_tes.html',context)

@user_passes_test(kurir,login_url='home')
def detail_alamat2 (request,id):
    alamat = Billingaddress.objects.get(pk=id)
    context = {
        'al':alamat
    }

    return render(request, 'alamat/detail_alamat2.html',context)
@user_passes_test(operator,login_url='home')
def search_alamat(request):
    if request.method == "POST":
        pencarian = request.POST['pencarian_alamat']
        hasil = Billingaddress.objects.filter(user__username__contains=pencarian)
        return render(request, "alamat/search_alamat.html",
        {'pencarian':pencarian,'hasil':hasil})
    else:
        return render(request, "alamat/search_alamat.html", {})

@user_passes_test(kurir,login_url='home')
def view_pembelian2 (request):
    alamat = Billingaddress.objects.all()
    context = {
        'al':alamat
    }

    return render(request, 'alamat/pembeliann2.html',context)
@user_passes_test(kurir,login_url='home')
def search_alamat2(request):
    if request.method == "POST":
        pencarian = request.POST['pencarian_alamat']
        hasil = Billingaddress.objects.filter(user__username__contains=pencarian)
        return render(request, "alamat/search_alamat2.html",
        {'pencarian':pencarian,'hasil':hasil})
    else:
        return render(request, "alamat/search_alamat2.html",
        {})
    # def informasi_buku(request,id):
    # all_data = Products.objects.get(pk=id)
    

    # context = {
    #     'data':all_data 
        
    #     }

    # return render(request, 'toko/informasi_buku.html', context)
@user_passes_test(operator,login_url='home')
def search_pembelian(request):
    if request.method == "POST":
        now = datetime.now()
        current_year = now.strftime("%Y")
        current_month = now.strftime("%m")
        current_day = now.strftime("%d")
        pencarian = request.POST['pencarian']
        hasil = Order.objects.filter(code__contains=pencarian)
        category = Category.objects.filter(id = 1,parent = None)
        category2 = Category.objects.filter(id = 2,parent = None)
        order_qs = Order.objects.filter(user=request.user, ordered=True)
        return render(request, "search/pembelian.html",
        {'pencarian':pencarian,'hasil':hasil,'cate1':category,
        'cate2':category2,'order_qs':order_qs,})
    else:
        return render(request, "search/pembelian.html",
        {})
@user_passes_test(kurir,login_url='home')
def search_pembelian2(request):
    if request.method == "POST":
        now = datetime.now()
        current_year = now.strftime("%Y")
        current_month = now.strftime("%m")
        current_day = now.strftime("%d")
        pencarian = request.POST['pencarian']
        hasil = Order.objects.filter(code__contains=pencarian)
        category = Category.objects.filter(id = 1,parent = None)
        category2 = Category.objects.filter(id = 2,parent = None)
        order_qs = Order.objects.filter(user=request.user, ordered=True)
        return render(request, "search/pembelian2.html",
        {'pencarian':pencarian,'hasil':hasil,'cate1':category,
        'cate2':category2,'order_qs':order_qs,})
    else:
        return render(request, "search/pembelian2.html",
        {})
@login_required
def pesanan_sampai (request,id):
    order = get_object_or_404(Order,id=id)
    if request.method == "POST": 
        order.status = '5'
        order.save()
        messages.success(request,'Pesanan kamu telah berhasil dikonfirmasi!')
        return redirect('pembelian')   
    context = {
        'obj':order
    }
    return render(request, 'update/konfirmasi_pembelian.html',context)

@user_passes_test(operator,login_url='home')
def update_pesanan(request, id):
  if request.method == 'POST':
    pi = Order.objects.get(pk=id)
    fm = pembelianform(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Status pesanan telah diperbarui!')
      return redirect('pembelian')
    
  else:
    pi = Order.objects.get(pk=id)
    fm = pembelianform(instance=pi)     
  return render(request, 'update/pembelian.html', {'form':fm})

@user_passes_test(kurir,login_url='home')
def update_pesanan2(request, id):
  if request.method == 'POST':
    pi = Order.objects.get(pk=id)
    fm = pembelianform(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Status pesanan telah diperbarui!')
      return redirect('cek_pembelian2')
    
  else:
    pi = Order.objects.get(pk=id)
    fm = pembelianform(instance=pi)     
  return render(request, 'update/pembelian2.html', {'form':fm})


@user_passes_test(operator,login_url='home')
def update_stok(request, id):
  if request.method == 'POST':
    pi = Product.objects.get(pk=id)
    fm = productforms(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Stok telah berhasil diperbarui!')
      return redirect('makanan_ma')
  else:
    pi = Product.objects.get(pk=id)
    fm = productforms(instance=pi)     
  return render(request, 'update/update_product.html', {'form':fm})

@user_passes_test(operator,login_url='home')
def update_stok_minuman(request, id):
  if request.method == 'POST':
    pi = Product.objects.get(pk=id)
    fm = productforms(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Stok telah berhasil diperbarui!')
      return redirect('minuman_mi')
  else:
    pi = Product.objects.get(pk=id)
    fm = productforms(instance=pi)     
  return render(request, 'update/update_product.html', {'form':fm})

# def search(request):
#     if request.method == "POST":
#         pencarian = request.POST['pencarian']
#         hasil = FileUpload.objects.filter(file_name__contains=pencarian)
#         return render(request, "search.html",
#         {'pencarian':pencarian,'hasil':hasil})
#     else:
#         return render(request, "search.html",
#         {})



    # def delete_product(request, id):
#     data = get_object_or_404(Product, id=id) 
#     data.delete()
#     messages.success(request,'Data telah berhasil di hapus!')

#     return redirect('makanan')

# def control_page(request):
#     now = datetime.now()
#     current_year = now.strftime("%Y")
#     current_month = now.strftime("%m")
#     current_day = now.strftime("%d")
#     categories = len(Category.objects.all())
#     products = len(Product.objects.all())
#     transaction = len(Order.objects.filter(
#         created__year=current_year,
#         created__month = current_month,
#         created__day = current_day,ordered =True
#     ))
#     today_sales = Cart.objects.filter(
#         created__year=current_year,
#         created__month = current_month,
#         created__day = current_day,purchased = True
#     ).all()
#     total_sales = sum(today_sales.values_list('item__price',flat=True))