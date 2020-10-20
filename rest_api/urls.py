from django.urls import path, include
from rest_framework import routers

from rest_api.views.employee import EmployeeViewSet, OfficeViewSet, DepartmentViewSet, get_data

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='Employee')
router.register(r'offices', OfficeViewSet, basename='Office')
router.register(r'departments', DepartmentViewSet, basename='Department')

urlpatterns = [
    path('get_data', get_data),
    path('', include(router.urls))
]