from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from provider import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="MozioTask API",
        default_version='v1',
        description="Welcome",
        terms_of_service="https://www.google.com",
        contact=openapi.Contact(email="dev@url.com"),
        license=openapi.License(name="My IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

router.register(
    r'providers', views.ProviderViewset, basename="providers"
)
router.register(
    r'servicearea', views.ServiceAreaViewset, basename="servicearea"
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path("loc-providers/", views.LocateProvider.as_view(), name='loc-providers')
]
