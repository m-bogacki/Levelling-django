from django.urls import path, include
from .views import UserListCreateView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

swagger_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"
    ),
]

jwt_urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = (
    [
        path("users/", include("account.urls")),
    ]
    + swagger_urlpatterns
    + jwt_urlpatterns
)
