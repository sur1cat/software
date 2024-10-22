from django.urls import path
from application.api.v1.views.application_views import ApplicationRequestViewSet

urlpatterns = [
    path('requests/create', ApplicationRequestViewSet.as_view({"post": "create"}), name='create_application'),
    path('requests/list', ApplicationRequestViewSet.as_view({"get": "list"}), name='get_application_list'),
    path('requests/retrieve/<int:pk>', ApplicationRequestViewSet.as_view({"get": "retrieve"}), name='retrieve_application'),
    path('requests/delete/<int:pk>', ApplicationRequestViewSet.as_view({"delete": "destroy"}), name='delete_application'),
    path('requests/assign-operators/<int:pk>', ApplicationRequestViewSet.as_view({"post": "assign_operators"}), name='assign_operators'),
]
