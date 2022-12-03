from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from store.models import Product,Category
from order.models import Order,Cart
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
# from .forms import ProductEdit,ProductTambah
from django.contrib import messages
from .forms import ProductEdit,ProductTambah
from django.contrib.auth.decorators import user_passes_test
def operator(user):
    return user.groups.filter(name='operator').exists()

def administration(user):
    return user.groups.filter(name='admin').exists()
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# function untuk menambahkan

@user_passes_test(administration,login_url='home')
def control_page(request):
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    categories = len(Category.objects.all())
    products = len(Product.objects.all())
    transaction = len(Order.objects.filter(
        created__year=current_year,
        created__month = current_month,
        created__day = current_day,ordered =True
    ))
    today_sales = Cart.objects.filter(
        created__year=current_year,
        created__month = current_month,
        created__day = current_day,purchased = True
    ).all()
    total_sales = sum(today_sales.values_list('item__price',flat=True))

    cat = Category.objects.filter(parent = None)
    context = {
        'categories' : categories,
        'products' : products,
        'transaction' : transaction,
        'total_sales' : total_sales,
        'cat':cat
    }
    return render(request, "control-page.html",context)
@user_passes_test(administration,login_url='home')
def makanan(request):
    makanan = Product.objects.filter(tipe = '1')
    cat = Category.objects.filter(parent = None)
    context = {
        'makanan':makanan,
         'cat':cat

    }

    return render(request, 'makanan/makanan.html',context)
@user_passes_test(administration,login_url='home')
def minuman(request):
    minuman = Product.objects.filter(tipe = '2')
    cat = Category.objects.filter(parent = None)
    context = {
        'minuman':minuman,
         'cat':cat

    }

    return render(request, 'minuman/minuman.html',context)
@user_passes_test(administration,login_url='home')
def tambahkan_product(request):
    cat = Category.objects.filter(parent = None)
    if request.method == 'POST':
        form = ProductTambah(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            tipe = form.cleaned_data['tipe']
            preview_des = form.cleaned_data['preview_des']
            description = form.cleaned_data['description']
            img = form.cleaned_data['img']
            price = form.cleaned_data['price']
            old_price = form.cleaned_data['old_price']
            stok = form.cleaned_data['stok']
            status = form.cleaned_data['status']
            slug = form.cleaned_data['slug']
            Product(name=name,category=category,tipe=tipe,preview_des=preview_des,description=description,img=img,price=price,old_price=old_price,stok=stok,status=status,slug=slug).save()
            messages.success(request,'Data telah berhasil ditambahkan!')
            context = {
                'cat':cat
            }
            return redirect('makanan')
        else:
            context = {
                'cat':cat
            }
            messages.error(request,'Data anda gagal ditambahkan!')
            return redirect('makanan')

#     # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # tipe = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # short_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
#     # img = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
#     # price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # old_price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # stok = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # status = forms.RadioSelect(choices=pilihan)
#     # slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    else:
        context = {
            'form':ProductTambah(),
             'cat':cat
        }      
        return render(request, 'makanan/tambahkan/tambahkan_makanan.html', context)
@user_passes_test(administration,login_url='home')
def update_product(request, id):
  if request.method == 'POST':
    print("tes")
    pi = Product.objects.get(pk=id)
    fm = ProductEdit(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Data telah berhasil di perbarui!')
      return redirect('makanan')
  else:
    pi = Product.objects.get(pk=id)
    fm = ProductEdit(instance=pi) 
  return render(request, 'makanan/edit/edit_makanan.html', {'form':fm})
    # jenis_ng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # harga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # kondisi = forms.BooleanField(widget=forms.BooleanField(attrs={'class':'form-control'}))
    # files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    # kondisi = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
@user_passes_test(administration,login_url='home')
def delete_product(request, id):
    data = get_object_or_404(Product, id=id)
    cat = Category.objects.filter(parent = None)
    if request.method == "POST": 
        data.delete()
        messages.success(request,'Data telah berhasil di hapus!')
        return redirect('makanan')
    context = {
        "obj":data,
        'cat':cat
    }

    return render(request, "makanan/delete/delete_makanan.html",context)
@user_passes_test(administration,login_url='home')
def tambahkan_minuman(request):
    cat = Category.objects.filter(parent = None)
    if request.method == 'POST':
        form = ProductTambah(request.POST, request.FILES)
        cat = Category.objects.filter(parent = None)
        print(form.as_p)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            tipe = form.cleaned_data['tipe']
            preview_des = form.cleaned_data['preview_des']
            description = form.cleaned_data['description']
            img = form.cleaned_data['img']
            price = form.cleaned_data['price']
            old_price = form.cleaned_data['old_price']
            stok = form.cleaned_data['stok']
            status = form.cleaned_data['status']
            slug = form.cleaned_data['slug']
            Product(name=name,category=category,tipe=tipe,preview_des=preview_des,description=description,img=img,price=price,old_price=old_price,stok=stok,status=status,slug=slug).save()
            messages.success(request,'Data telah berhasil ditambahkan!')
            context = {
                'cat':cat
            }
            return redirect('minuman')
        else:
            context = {
                'cat':cat
            }
            messages.error(request,'Data anda gagal ditambahkan!')
            return redirect('minuman')

#     # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # tipe = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # short_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
#     # img = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
#     # price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # old_price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # stok = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     # status = forms.RadioSelect(choices=pilihan)
#     # slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    else:
        context = {
            'form':ProductTambah(),
            'cat':cat
            
        }      
        return render(request, 'minuman/tambahkan/minuman_tambah.html', context)
@user_passes_test(administration,login_url='home')
def update_minuman(request, id):
  if request.method == 'POST':
    print("tes")
    pi = Product.objects.get(pk=id)
    fm = ProductEdit(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Data telah berhasil di perbarui!')
      return redirect('minuman')
  else:
    pi = Product.objects.get(pk=id)
    fm = ProductEdit(instance=pi) 
  return render(request, 'minuman/edit/minuman_ed.html', {'form':fm})
    # jenis_ng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # harga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # kondisi = forms.BooleanField(widget=forms.BooleanField(attrs={'class':'form-control'}))
    # files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    # kondisi = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
@user_passes_test(administration,login_url='home')
def delete_minuman(request, id):
    data = get_object_or_404(Product, id=id)
    cat = Category.objects.filter(parent = None)
    if request.method == "POST": 
        data.delete()
        messages.success(request,'Data telah berhasil di hapus!')
        return redirect('minuman')
    context = {
        "obj":data,
        'cat':cat
    }

    return render(request, "minuman/delete/delete_minuman.html",context)