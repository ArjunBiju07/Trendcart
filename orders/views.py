from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from orders.models import Orders,OrderedItems
from products.models import Products
from django.contrib import messages
# Create your views here.

@login_required(login_url='show_account')
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Orders.objects.get_or_create(
            owner = customer,
            order_status = Orders.CART_STAGE
        )
    context = {'cart' : cart_obj}
    return render(request,'cart.html',context)

@login_required(login_url='show_account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj,created = Orders.objects.get_or_create(
            owner = customer,
            order_status = Orders.CART_STAGE
        )
        product = Products.objects.get(pk = product_id) 
        ordered_item = OrderedItems.objects.filter(
            products = product,
            owner = cart_obj
        ).first()

        if ordered_item:
            ordered_item.quantity = ordered_item.quantity + quantity
            ordered_item.save()
        else:
            ordered_item = OrderedItems.objects.create(
                products = product,
                owner = cart_obj,
                quantity = quantity
            )

        return redirect('cart') 

@login_required(login_url='show_account')
def remove_cart_item(request,pk):
    item = OrderedItems.objects.get(pk = pk)
    if item:
        item.delete()
    return redirect('cart')

@login_required(login_url='show_account')
def checkout(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = Orders.objects.get(
                owner = customer,
                order_status = Orders.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Orders.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_msg = "Your order is procesed.Your item will be deliverd soon"
                messages.success(request,status_msg)
            else:
                status_msg = "Unable to processed.No items in cart"
                messages.error(request,status_msg)
        except Exception as e:
            status_msg = "Unable to processed.No items in cart"
            messages.error(request,status_msg)
    
    return redirect('cart')

@login_required(login_url='show_account')
def view_order(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Orders.objects.filter(owner = customer).exclude(order_status = Orders.CART_STAGE)
    context = {'orders' : all_orders}
    return render(request,'orders.html',context)