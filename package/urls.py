from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='package'

urlpatterns = [
    path('', views.home, name='home1'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name= 'contacts'),
    path('about/', views.about, name='about'),
    path('track/', views.track, name='track'),
    
    path('new-message/',views.newmessage, name = 'new message'),
    path('all-messages/',views.Allmessages, name = 'all messages')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

