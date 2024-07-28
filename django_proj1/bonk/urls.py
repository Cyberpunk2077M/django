from django.urls import path
from . import views

urlpatterns = [
    path('', views.bonkfn1, name='bonk_function'),
    path('bonk/<int:car_id>/', views.car_details, name='car_details'),
]
