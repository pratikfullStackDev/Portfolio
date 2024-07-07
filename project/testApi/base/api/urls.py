from django.contrib import admin
from django.urls import path, include
from .views.companyViews import companyViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', companyViewset)


urlpatterns = [
   path('',include(router.urls))
]
