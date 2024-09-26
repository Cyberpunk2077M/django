from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('about/', views.about, name='AboutUs'),
    path('conatct/', views.contact, name='ContactUs'),
    path('search/', views.search, name='SearchBar'),
    path('related/', views.related, name='Related'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('community/', views.community, name='Community'),
]