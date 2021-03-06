from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home),
    path('shop', views.shop),
    path('shop/<int:page_number>', views.shop, name = "shop"),
    path('product',views.product),
    path('cart', views.cart, name = "cart"),
    path('about', views.about),
    path('contact', views.contact),
    path('register', views.register),
    path('login', views.log_in),
    path('logout', views.log_out),
    path('accounts/', include('django.contrib.auth.urls'))
]
