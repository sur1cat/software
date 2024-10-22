from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from application.models import Course
from rest_framework.permissions import AllowAny
from application.api.v1.serializers.course_serializers import CourseSerializer


class CoursesViews(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin):
    permission_classes = (AllowAny,)
    queryset = Course.objects.all()

    def get_serializer_class(self):
        return CourseSerializer

    def create(self, request, *args, **kwargs):
        course_serializer: CourseSerializer = self.get_serializer(data=self.request.data)

        if course_serializer.is_valid(raise_exception=True):
            course = course_serializer.create(course_serializer.validated_data)
            return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        courses: CourseSerializer = self.get_serializer(self.queryset.all(), many=True)
        return Response(courses.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            self.queryset.filter(id=self.kwargs['pk']).delete()
            return Response({"status":"Completed"},status=status.HTTP_202_ACCEPTED)
        except Exception as exc:
            raise exc

    def retrieve(self, request, *args, **kwargs):
        try:
            course = self.queryset.get(id=self.kwargs['pk'])
            return Response(CourseSerializer(course).data, status=status.HTTP_200_OK)

        except Exception as exc:
            return exc
