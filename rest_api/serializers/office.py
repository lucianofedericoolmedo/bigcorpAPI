from rest_flex_fields import FlexFieldsModelSerializer
from rest_api.models.employee import  Office


class OfficeSerializer(FlexFieldsModelSerializer):
    """Serializer to map the model instance into json format."""

    @staticmethod
    def check_fields():
        return 'id', 'city', 'country', 'address'

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Office
        fields = ('id', 'city', 'country', 'address')