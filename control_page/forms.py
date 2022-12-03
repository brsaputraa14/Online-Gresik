from django import forms
from django.forms import HiddenInput
from setuptools import Require
from store.models import Product,Category

pilihan = (
	(0,'Tidak Tersedia'),
	(1,'Ada'),
)

# class ProductTambah(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#     tipe = forms.ModelChoiceField(queryset=Category.objects.all())
#     preview_des = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
#     img = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
#     price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     old_price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     stok = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     status = forms.ChoiceField(choices=pilihan)
#     slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class ProductTambah(forms.ModelForm):
	class Meta:
		model = Product
		fields =  [ 'name','category','tipe','preview_des','description','img','price','old_price','stok','status','slug' ]
		widgets = {
			'name':forms.TextInput(attrs={'class': 'form-control'}),
    		'category':forms.Select,
    		'tipe':forms.Select,
    		'preview_des':forms.TextInput(attrs={'class':'form-control'}),
    		'description':forms.Textarea(attrs={'class':'form-control'}),
    		'img':forms.FileInput(attrs={'class':'form-control'}),
    		'price':forms.TextInput(attrs={'class':'form-control'}),
    		'old_price':forms.TextInput(attrs={'class':'form-control'}),
    		'stok':forms.TextInput(attrs={'class':'form-control'}),
    		'status':forms.RadioSelect(choices=pilihan),
    		'slug':forms.TextInput(attrs={'class':'form-control'}),
		}



# class ProductTambah(forms.ModelForm):
#      class Meta:
#         model = Product
#         fields = [ 'name','category','tipe','short_description','description','img','price','old_price','stok','status','slug' ]
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'category': forms.ModelChoiceField(queryset=Category.objects.all()),
#             'tipe': forms.ModelChoiceField(queryset=Category.objects.all()),
#             'short_description': forms.TextInput(attrs={'class':'form-control'}),
#             'description': forms.TextInput(attrs={'class':'form-control'}),
#             'img': forms.FileInput(attrs={'class':'form-control'}),
#             'price': forms.TextInput(attrs={'class':'form-control'}),
#             'old_price': forms.TextInput(attrs={'class':'form-control'}),
#             'stok': forms.TextInput(attrs={'class':'form-control'}),
#             'status': forms.TextInput(attrs={'class':'form-control'}),
#             'slug': forms.TextInput(attrs={'class':'form-control'}),

#         }
        

class ProductEdit(forms.ModelForm):
	class Meta:
		model = Product
		fields =  [ 'name','category','tipe','preview_des','description','img','price','old_price','stok','status','slug' ]
		widgets = {
			'name':forms.TextInput(attrs={'class': 'form-control'}),
    		'category':forms.Select,
    		'tipe':forms.Select,
    		'preview_des':forms.TextInput(attrs={'class':'form-control'}),
    		'description':forms.Textarea(attrs={'class':'form-control'}),
    		'img':forms.FileInput(attrs={'class':'form-control'}),
    		'price':forms.TextInput(attrs={'class':'form-control'}),
    		'old_price':forms.TextInput(attrs={'class':'form-control'}),
    		'stok':forms.TextInput(attrs={'class':'form-control'}),
    		'status':forms.RadioSelect(choices=pilihan),
    		'slug':forms.TextInput(attrs={'class':'form-control'}),
		}

