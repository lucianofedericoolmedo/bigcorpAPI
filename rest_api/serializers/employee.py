from rest_flex_fields import FlexFieldsModelSerializer

from rest_api.models.employee import Employee
from rest_api.serializers.department import DepartmentSerializer
from rest_api.serializers.office import OfficeSerializer
from rest_api.serializers.string_search_mixin import StringSearchMixin

current_module = 'rest_api.serializers.employee.EmployeeSerializer'


class EmployeeSerializer(StringSearchMixin, FlexFieldsModelSerializer):
    """Serializer to map the model instance into json format."""

    @staticmethod
    def check_fields():
        return 'id', 'first', 'last', 'manager', 'department', 'office'

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Employee
        fields = ('id', 'first', 'last', 'manager', 'department', 'office')
        expandable_fields = {
            'department': (DepartmentSerializer, {'many': False}),
            'manager': (current_module, {'many': False}),
            'office': (OfficeSerializer, {'many': False})
        }
