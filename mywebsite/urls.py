from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('shawarma/', include('shawarma.urls')),
    path('mebelchel/', include('mebelchel.urls')),
    path('notes/', include('notes_main.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
