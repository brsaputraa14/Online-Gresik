from django.urls import path
from .import views


urlpatterns = [
    
    path('register/', views.register, name="register"),
    path('login/', views.customerlogin, name="customerlogin"),
    path('logout/', views.logout_view, name="logout"),

]