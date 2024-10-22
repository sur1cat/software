from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from application.models import ApplicationRequest, Operators
from application.api.v1.serializers.application_serializer import ApplicationRequestSerializer


class ApplicationRequestViewSet(ModelViewSet):
    queryset = ApplicationRequest.objects.all()
    serializer_class = ApplicationRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            application = serializer.save()
            return Response(ApplicationRequestSerializer(application).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        applications = self.queryset.all()
        serializer = self.get_serializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            application = self.get_object()
            serializer = self.get_serializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ApplicationRequest.DoesNotExist:
            return Response({"detail": "Application not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            application = self.get_object()
            application.delete()
            return Response({"status": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ApplicationRequest.DoesNotExist:
            return Response({"detail": "Application not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def assign_operators(self, request, pk=None):
        try:
            application = self.get_object()
            operator_ids = request.data.get('operators', [])
            operators = Operators.objects.filter(id__in=operator_ids)

            if not operators:
                return Response({"detail": "No operators found."}, status=status.HTTP_400_BAD_REQUEST)

            application.operators.set(operators)
            application.handled = True
            application.save()

            return Response({"detail": "Operators assigned successfully."}, status=status.HTTP_200_OK)
        except ApplicationRequest.DoesNotExist:
            return Response({"detail": "Application not found"}, status=status.HTTP_404_NOT_FOUND)
