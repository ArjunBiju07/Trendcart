from django.shortcuts import render
from products.models import Products
# Create your views here.

def index(request):
    return render(request,'index.html')

def list_products(request):
    product_list = Products.objects.all()
    items = {'products' : product_list}
    return render(request,'products.html',items)

def detail_product(request):
    return render(request,'product_details.html')