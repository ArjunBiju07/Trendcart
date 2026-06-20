from django.urls import path
from customers import views 

urlpatterns = [
    path('account/',views.show_account,name = 'show_account'),
  
]