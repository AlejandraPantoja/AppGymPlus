from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('miembros.urls')),  # Todas tus rutas de API REST
    path('', TemplateView.as_view(template_name='index.html')),  # Sirve Angular
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
