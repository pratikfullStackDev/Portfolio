from django.urls import path,include
from .views.base import index

urlpatterns = [
 path('',index,name='index'),   
]
