from rest_framework import serializers
from application.models import ApplicationRequest, Operators

class OperatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operators
        fields = ['id', 'name', 'surname', 'department']

class ApplicationRequestSerializer(serializers.ModelSerializer):
    operators = OperatorsSerializer(many=True, read_only=True)
    course = serializers.StringRelatedField()

    class Meta:
        model = ApplicationRequest
        fields = ['id', 'user_name', 'commentary', 'phone', 'handled', 'course', 'operators']
