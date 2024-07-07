from django.shortcuts import render
from rest_framework import viewsets
from api.models.company import CompanyTable
from api.serializers.companySerializer import companySerializer

class companyViewset(viewsets.ModelViewSet):
    queryset = CompanyTable.objects.all()
    serializer_class = companySerializer
    