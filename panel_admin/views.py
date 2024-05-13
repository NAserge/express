from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from .forms import Orderform
from package.models import contactmessage

from . models import Order

# Create your views here.

def dashboard(request):
    count =Order.objects.count()
    return render(request, 'index.html', {'count':count} )

def logoutUser(request):
    logout(request)
    return redirect('panel_admin:login')


def loginUser(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('panel_admin:dashboard')   
        else:
            print('Username or password is not correct')         
    return render(request, 'login.html')


def newOder(request):
    form = Orderform()
    if request.method =='POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel_admin:order-list')
    context = {'form':form}
    return render(request, 'order_form.html',context )

def updateOder(request, pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method =='POST':
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('panel_admin:order-list')
    context = {'form':form}
    return render(request, 'order_form.html',context )


def orders(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def details(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'details.html', {'order': order})


def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method =='POST':
        order.delete()
        return redirect('panel_admin:order-list')
    context = {'order': order}
    return render(request, 'delete.html', context)

def Allmessages(request):
    contactmessage = contactmessage.objects.all()
    return render(request, 'allmessage.html', {'contactmessage': contactmessage})

def messageDetails(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'details.html', {'order': order})

