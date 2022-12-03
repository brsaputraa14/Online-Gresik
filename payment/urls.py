from django.urls import path
from .import views

urlpatterns = [
    path('checkout/',views.CheckoutTemplateView.as_view(),name="checkout")
]
