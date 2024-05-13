from django.shortcuts import render,  redirect
from panel_admin.models import Order
from django.contrib import messages
from .forms import messageForm

# Create your views here.

def home(request):
    return render(request, 'home1.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html' )

def about(request):
    return render(request, 'about.html' )

def track(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            model_instance = Order.objects.get(tracking_number=tracking_number)
            return render(request, 'track.html', {'model_instance': model_instance})
        except Order.DoesNotExist:
            messages.error(request, 'Order not found.')
    return render(request, 'track.html')



def newmessage(request):
    form = messageForm()
    if request.method =='POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.save()
            messages(request, 'message sent.')
            return redirect('package:contacts')
    context = {'form':form}
    return render(request, 'contacts.html',context )

def Allmessages(request):
    contactmessage = contactmessage.objects.all()
    return render(request, 'allmessage.html', {'contactmessage': contactmessage})

def messageDetails(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'details.html', {'order': order})
