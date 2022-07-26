"""umibot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from src.api.user_views import UserView

SchemaView = get_schema_view(
    openapi.Info(
        title="UmiShop bots API",
        default_version="v1",
        description="API for integrations with UmiShop company",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="fran.rodeno@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        SchemaView.without_ui(),
        name="schema-json",
    ),
    re_path(r"^swagger/$", SchemaView.with_ui("swagger"), name="schema-swagger-ui"),
    re_path(r"^redoc/$", SchemaView.with_ui("redoc"), name="schema-redoc"),
    path("api/v1/user/", UserView.as_view(), name="user"),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)  # type: ignore
