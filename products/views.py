from django.shortcuts import render
from products.models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_prdt = Products.objects.order_by('-priority')[:4]
    latest_prdt = Products.objects.order_by('-id')[:4]
    context = {
        'featured' : featured_prdt,
        'latest' : latest_prdt,
    }
    return render(request,'index.html',context)

def list_products(request):
    page  = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = Products.objects.order_by('-priority')
    product_page = Paginator(product_list,8)
    product_list = product_page.get_page(page) 
    items = {'products' : product_list}
    return render(request,'products.html',items)

def detail_product(request,pk):
    
    prod = Products.objects.get(pk = pk)
    context = {'prod' : prod}
    return render(request,'product_details.html',context)