
from django.urls import path
from application.api.v1.views.courses_views import CoursesViews

urlpatterns = [
    path('create', CoursesViews.as_view({"post":"create"}), name='create course'),
    path('list', CoursesViews.as_view({"get":"list"}), name="get list"),
    path('retrieve/<int:pk>', CoursesViews.as_view({"get":"retrieve"}), name='retrieve course'),
    path('delete/<int:pk>', CoursesViews.as_view({"delete":"destroy"}, name='delete course'))
]