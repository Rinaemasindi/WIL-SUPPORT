from django.urls import path
from . import views 
 



urlpatterns = [

    path('register_wil/', views.register_wil, name='register_wil'),

    path('instractions/', views.instractions, name='instractions'),

]
