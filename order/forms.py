from django import forms
from .models import Order,Cart

class pembelianform(forms.ModelForm):
     class Meta:
        model = Order
        fields = [ 'status' ]
        widgets = {
            'status': forms.Select, 
        }