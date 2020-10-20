from django.urls import path, include
from rest_framework import routers

from rest_api.views.employee import EmployeeViewSet, OfficeViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='Employee')
router.register(r'offices', OfficeViewSet, basename='Office')
router.register(r'departments', DepartmentViewSet, basename='Department')

urlpatterns = [
    path('', include(router.urls))
]