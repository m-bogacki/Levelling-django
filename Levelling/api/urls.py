from django.urls import path
from .views import UserListCreateView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="users"),
    path(
        "schema/swagger/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
]
