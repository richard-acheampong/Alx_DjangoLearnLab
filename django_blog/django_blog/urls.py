"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#imports for drf_yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include

#schema_view for drf-yasg
# schema_view = get_schema_view(
#     openapi.info(
#         title= "django_blog API",
#         default_version= "v1"
#         description= "API documentation for my django_blog project",
#         # terms_of_service= "https://www.google.com/policies/terms/",  # Optional: link to your terms of service
#         # contact=openapi.Contact(email="contact@blog.com"),  
#         license=openapi.License(name="BSD License")
#     )
#     public= False
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
     path('', include('django.contrib.auth.urls')),
   

    



    #urls for drf-yasg
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
    # path('openapi/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # OpenAPI JSON schema
]
