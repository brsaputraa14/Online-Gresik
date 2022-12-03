from django.urls import path
from .import views



urlpatterns = [
    
    path('', views.home, name="home"),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name="product_details"),
    path('minuman/<slug:slug>', views.MinumanDetailView.as_view(), name="minuman_details"),
    path('Minuman', views.minuman_view, name="minuman_mi"),
    path('Makanan', views.makanan_view, name="makanan_ma"),
    path('pembelian', views.pembelian, name="pembelian"),
    path('cek_pembelian', views.cek_pembelian, name="cek_pembelian"),
    path('cek_pembelian/kurir', views.cek_pembelian2, name="cek_pembelian2"),
    path('pesanan_sampai/<int:id>', views.pesanan_sampai, name="pesanan_sampai"),
    path('update_pesanan/<int:id>', views.update_pesanan, name="update_pesanan"),
    path('update_pesanan/kurir/<int:id>', views.update_pesanan2, name="update_pesanan2"),
    path('update_stok/<int:id>', views.update_stok, name="update_stok"),
    path('search_pembelian', views.search_pembelian, name="search_pembelian"),
    path('search_pembelian/kurir', views.search_pembelian2, name="search_pembelian2"),
    path('alamat', views.view_pembelian, name="view_pembelian"),
    path('search_alamat', views.search_alamat, name="search_alamat"),
    path('detail_alamat/<int:id>', views.detail_alamat, name="detail_alamat"),
    path('detail_tes/<int:id>', views.detail_alamates, name="detail_tes"),
    path('detail_alamat/kurir/<int:id>', views.detail_alamat2, name="detail_alamat2"),
    path('alamat/kurir', views.view_pembelian2, name="view_pembelian2"),
    path('search_alamat/kurir', views.search_alamat2, name="search_alamat2"),
    # path('makanan', views.MakananListView.as_view(), name="makanan"),

]