from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.control_page, name="cpage"),
    path('Makanan/', views.makanan, name="makanan"),
    path('Minuman/', views.minuman, name="minuman"),
    path('Makanan/Edit/<int:id>', views.update_product, name="edit"),
    path('Minuman/Edit/<int:id>', views.update_minuman, name="edit_minuman"),
    path('Makanan/Tambahkan', views.tambahkan_product, name="tambahkan_product"),
    path('Minuman/Tambahkan', views.tambahkan_minuman, name="tambahkan_minuman"),
    path('Makanan/delete/<int:id>', views.delete_product, name="delete_product"),
    path('Minuman/delete/<int:id>', views.delete_minuman, name="delete_minuman"),
]