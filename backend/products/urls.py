from django.urls import path
from . import views

urlpatterns = [
    path('', views.productDetailAPIView.as_view())   
]
