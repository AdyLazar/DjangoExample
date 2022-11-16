from django.urls import path
from .import views

urlpatterns = [
    path('show/', views.apiOverView),
    path('data/',views.getPost),
    path('log/create',views.CreateLogMessage),
]