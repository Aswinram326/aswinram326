from django.shortcuts import render,redirect
from.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from.forms import customUserCreatonForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
import datetime






def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cartItems= order.get_cart_items
    else:
        items = []
        order={'get_cart_total':0,'get_cart_item':0}
        cartItems = order['get_cart_item']
    products=Product.objects.all()
    context={'items':items,'order':order,'cartItems':cartItems,'products':products}
    return render(request,"grocapp/index.html",context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cartItems = order.get_cart_items 
    else:
        items = []
        order={'get_cart_total':0,'get_cart_item':0}
        cartItems = order['get_cart_item']
 
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,"grocapp/cart.html",context) 
    


def list(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cartItems = order.get_cart_items 
    else:
        items = []
        order={'get_cart_total':0,'get_cart_item':0}
        cartItems = order['get_cart_item']
    
    products=Product.objects.all()
    context={'items':items,'order':order,'cartItems':cartItems,'products':products}
    return render(request,"grocapp/shop.html",context)

def productdetails(request,product_id):
    products=Product.objects.filter(id=product_id).get()
    return render(request,'grocapp/productdetails.html',{'products':products})

def orderdetails(request,product_id):
    products=OrderItem.objects.filter(id=product_id).get()
    return render(request,'grocapp/orderdetail.html',{'products':products})




def mail(request):
    try:
       if request.method=='POST': 
         subject=request.POST['Email']
         message=request.POST['Message']
         from_email = settings.EMAIL_HOST_USER
         recipient_list = ["aswinram326@gmail.com"]
         send_mail(subject , message, from_email , recipient_list)
        
         return render(request,'grocapp/contact.html')
       else:
           return render(request,'grocapp/contact.html')
       
    except:
       subjects=False
       return render(request,'grocapp/contact.html')
    
def contact(request):
    return render(request,"grocapp/contact.html")


def login(request):
    return render(request,"grocapp/login.html")

def address(request):
    address=Address.objects.all()
    return render(request,"grocapp/address.html",{'address':address})

def myorder(request):
            orders = OrderItem.objects.filter(customer=request.user.customer)
            print(orders)
            return render(request,"grocapp/myorders.html",{'orders':orders}) 
  


def testimonial(request):
    return render(request,"grocapp/testimonial.html")

def why(request):
    return render(request,"grocapp/why.html")

def checkout(request,**kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cartItems = order.get_cart_items 
       
    
    else:
        items = []
        order={'get_cart_total':0,'get_cart_item':0,'shipping':False}
        cartItems = order['get_cart_item']
    
      
    
  
    return render(request,"grocapp/checkout.html",{'items':items,'order':order,'cartItems':cartItems})

   


def category(request,foo):
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,"grocapp/category.html",{'products':products,'category':category})
    except:
        messages.success(request,("that category is not available"))
        return redirect('index')


def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action',action)
    print('Productid',productId)
    customer=request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order , product=product ,customer=customer,)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('item was added',safe=False)

def searchbar(request):
    query = request.GET.get('q') 
    if query:
        keywords = query.split()
        q_objects = Q()
        for keyword in keywords:
            q_objects |= (
                Q(name__icontains=keyword)     
            )
        products = Product.objects.filter(q_objects)
        context = {
            'query': query,
            'products': products,
        }
        return render(request,'grocapp/shop.html',context)
    else:
        
        products=Product.objects.all()
        return render(request,"grocapp/index.html",{"products":products})
        


def signup(request):
   
    if request.method == 'POST':
            
            form =customUserCreatonForm(request.POST)
            if form.is_valid():
                name= form.cleaned_data['name']
                email = form.cleaned_data['email']
                user = form.save()
                Customer.objects.create(user=user,name=name, email=email)
                auth_login(request,user)
                msg="Signup Success"
                return render(request, 'grocapp/signin.html')
              
    else:

        form =customUserCreatonForm()
    
    return render(request, 'grocapp/signup.html', {'form': form})
    
def signout(request):
    if 'username' in request.session:
        del request.session['username']
    logout(request)
    return redirect('/')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username']=username
            if user is not None:
                auth_login(request,user)
                return redirect(index)  
        else:
            invalid="Invalid Input"
            return render(request, 'grocapp/signin.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'grocapp/signin.html', {'form': form})

    
def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id=transaction_id
        
        if total == order.get_cart_total:
            order.complete=True
        order.save()

   

        if order.shipping == True:
            Address.objects.create(
                customer=customer,
                order=order,
                place=data['shipping']['place'],
                district=data['shipping']['district'],
                state=data['shipping']['state'],
                pincode=data['shipping']['pincode'],
               
            )

    else:
        print("Use is not logged in")

    return JsonResponse('payement complete',safe=False)

def change_password(requset):
    if requset.method =='POST':
        form=PasswordChangeForm(requset.user,requset.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form=PasswordChangeForm(requset.user)
        return render(requset, 'grocapp/changepass.html',{"form":form})
    
    return render(requset,"grocapp/changepass.html")


def charge(request):
    if request.method=="POST":
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='django charge',
            source=request.POST['stripeToken']

        )
        return render(request,"grocapp/charge.html")