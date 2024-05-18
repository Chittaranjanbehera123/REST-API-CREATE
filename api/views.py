from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponseBase
from rest_framework import status


# Create your views here.
class CompanyViweset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    
    #companies/{companyId}/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None): 
        try:   
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Company.DoesNotExist:
            raise NotFound("Company does not exist")
        except Exception as e:
            print(e)
            return Response({
                'message': 'An error occurred while processing the request.'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer