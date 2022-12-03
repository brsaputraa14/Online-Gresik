from django import forms

class Couponcodeforms(forms.Form):
    code = forms.CharField()