from django.urls import path

from .import views
app_name = 'order'
urlpatterns = [
    path('add-to-cart/<int:pk>/',views.add_to_cart,name="add-to-cart"),
    path('add-to-cart_minuman/<int:pk>/',views.add_to_cart_minuman,name="add-to-cart_minuman"),
    path('add-to-cart_home_home/<int:pk>/',views.add_to_cart_home_home,name="add-to-cart_home_home"),
    path('add-to-cart_home/<int:pk>/',views.add_to_cart_home,name="add-to-cart_home"),
    path('add-to-cart_home_minuman/<int:pk>/',views.add_to_cart_home_minuman,name="add-to-cart_home_minuman"),
    path('cart-view/',views.cart_view,name="cart"),
    path('increase-quantity/<int:pk>/',views.increase_cart,name="increase-cart"),
    path('decrease-quantity/<int:pk>/',views.decrease_cart,name="decrease-cart"),
    path('delete_cart/<int:pk>/',views.delete_cart,name="delete_cart"),
    path('delete_cart_home/<int:pk>/',views.delete_cart_home,name="delete_cart_home"),
    path('delete_cart_home_home/<int:pk>/',views.delete_cart_home_home,name="delete_cart_home_home"),
]
