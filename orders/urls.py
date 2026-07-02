from django.urls import path
from orders import views 

urlpatterns = [
    path('cart/',views.show_cart,name = 'cart'),
    path('add_to_cart/',views.add_to_cart,name ='add_to_cart'),
    path('remove_cart_item/<pk>',views.remove_cart_item,name = 'remove'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('view_orders/',views.view_order,name = 'view_orders')
]