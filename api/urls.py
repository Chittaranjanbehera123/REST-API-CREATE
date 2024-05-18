from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViweset,EmployeeViewset
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'companies', CompanyViweset)
router.register(r'employees',EmployeeViewset)


urlpatterns = [
    path('',include(router.urls))
    
]

#companies/{companyId}/employees