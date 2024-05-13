from django.db import models
from panel_admin.models import Order

# Create your models here.

class contactmessage(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField
    message = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    class Meta:
        ordering = ['-date_created']
    
    
