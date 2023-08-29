from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer, name='customer-detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('add_customer/', views.add_customer, name='add-customer'),
    path('add_address/', views.add_address, name='add-address'),
    path('update_customer/<int:pk>', views.update_customer, name='update-customer'),
    path('update_address/<int:pk>', views.update_address, name='update-address'),
]
