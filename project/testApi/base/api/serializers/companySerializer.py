from rest_framework import serializers
from api.models.company import CompanyTable

class companySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = CompanyTable
        fields = '__all__'