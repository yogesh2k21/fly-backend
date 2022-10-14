from rest_framework import serializers
from apps.students.models import Assignment


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    """
    Teacher Assignment serializer
    """
    # giving model name with fields which is going to be serialized
    class Meta:
        model = Assignment
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)
