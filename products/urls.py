from django.urls import path
from products import views 

urlpatterns = [
    path('',views.index,name = 'index'),
    path('product_list/',views.list_products,name = 'list_product'),
    path('product_details/<pk>',views.detail_product,name = 'product_details'),
    
]