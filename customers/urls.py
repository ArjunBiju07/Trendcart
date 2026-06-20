from django.urls import path
from customers import views 

urlpatterns = [
    path('',views.home,name = 'index'),
]
