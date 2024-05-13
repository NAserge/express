from panel_admin.models import Order
from django.forms import ModelForm
from .models import Order, contactmessage



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('tracking_number',)
        
class messageForm(ModelForm):
    class Meta:
        model = contactmessage
        fields = '__all__'