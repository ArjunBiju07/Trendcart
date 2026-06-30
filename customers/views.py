from django.contrib.admin import register
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from customers.models import Customer
from django.contrib import messages

# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('index')
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:   
            username = request.POST.get('username')
            address = request.POST.get('address')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            #Create user account
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
            # create customer account
            customer = Customer.objects.create(
                user = user,
                address = address,
                phone = phone
                
            )
            success_msg = "User registered successfully"
            messages.success(request,success_msg)
        except Exception as e:
            error_msg = "Username already exist or invalid input data"
            messages.error(request,error_msg)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"Invalid user credentials")
            return redirect('show_account') 
            
    return render(request,'account.html',context)
