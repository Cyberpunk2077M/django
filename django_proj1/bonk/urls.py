from django.urls import path
from . import views

#localhost:8000/bonkfn1
#localhost:8000/bonkfn1/sub_fn
urlpatterns = [
    path('', views.bonkfn1, name="bonk_function"),
 ]