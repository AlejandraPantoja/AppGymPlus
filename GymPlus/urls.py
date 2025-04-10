from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('miembros.urls')),  # Todas tus rutas de API REST
    re_path(r'^.*$', never_cache(TemplateView.as_view(template_name="index.html"))),
]
