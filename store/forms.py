from django import forms
from .models import Product

status = (
	(0,'sedang tidak tersedia'),
	(1,'tersedia'),
)

class productforms(forms.ModelForm):
     class Meta:
        model = Product
        fields = [ 'status','stok' ]
        widgets = {
            'status': forms.Select(choices=status)
        }