from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_product/<int:id_product>/', views.add_product_cart, name='cart_add_product'),
    path('product-delete/<int:id>/', views.delete_product, name='delete'),
    path('cart-checkout/', views.CartChecout.as_view(), name='cart_checkout'),

]
