from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name='panel_admin'

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-order/', views.newOder, name='new-order'),
    path('orders/', views.orders, name='order-list'),
    path('details/<str:pk>/', views.details, name = 'details'),
    path('update-order/<str:pk>/', views.updateOder, name= 'update-order'),
    path('delete-order/<str:pk>/', views.deleteorder, name="delete-order"), 
    
    
]
urlpatterns += staticfiles_urlpatterns()