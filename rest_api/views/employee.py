import requests
from rest_framework.response import Response
from rest_flex_fields import is_expanded
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from rest_api.models.employee import Employee, Office, Department
from rest_api.serializers.department import DepartmentSerializer
from rest_api.serializers.employee import EmployeeSerializer
from rest_api.serializers.office import OfficeSerializer


class FilterInPlaceWithModelFields(object):
    def filter_by_fields_queryset_in_place(self, queryset):
        to_filter = {}
        for elem in self.serializer_class.check_fields():
            filter_elems = self.request.GET.getlist(elem)
            if len(filter_elems) > 0:
                to_filter['{0}__{1}'.format(elem, 'in')] = filter_elems
        queryset = queryset.filter(**to_filter)
        return queryset


class DepartmentViewSet(FilterInPlaceWithModelFields, viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving offices.
    """
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = Department.objects.all()
        queryset = self.filter_by_fields_queryset_in_place(queryset)
        # Query optimization
        if is_expanded(self.request, 'super_department'):
            queryset = queryset.select_related('super_department')
        return queryset


class OfficeViewSet(FilterInPlaceWithModelFields, viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving offices.
    """
    serializer_class = OfficeSerializer

    def get_queryset(self):
        queryset = Office.objects.all()
        return self.filter_by_fields_queryset_in_place(queryset)


class EmployeeViewSet(FilterInPlaceWithModelFields, viewsets.ReadOnlyModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        queryset = self.filter_by_fields_queryset_in_place(queryset)
        # Query optimization
        if is_expanded(self.request, 'manager'):
            queryset = queryset.select_related('manager')
        if is_expanded(self.request, 'department'):
            queryset = queryset.select_related('department')

        return queryset
