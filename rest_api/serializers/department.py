from rest_flex_fields import FlexFieldsModelSerializer
from rest_api.models.employee import Department
from rest_api.serializers.string_search_mixin import StringSearchMixin

current_module = 'rest_api.serializers.department.DepartmentSerializer'


class DepartmentSerializer(StringSearchMixin, FlexFieldsModelSerializer):
    """Serializer to map the model instance into json format."""

    @staticmethod
    def check_fields():
        return 'id', 'name', 'super_department'

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Department
        fields = ('id', 'name', 'super_department')
        expandable_fields = {
            'super_department': (current_module, {'many': False})
        }
