from django.urls import path
from . import views

#URLConf
urlpatterns = [
     path('hello/<name>',views.hello_there, name="hello_there"),
     path('hello/',views.say_hello),
     path('home/', views.home, name="home"),
     path('about/', views.about, name="about"),
     path('contact/', views.contact, name="contact"),
     path('log/', views.log_message, name="log"),
]