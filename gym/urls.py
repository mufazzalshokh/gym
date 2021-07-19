from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('pages.urls', namespace='contact')),
    path('price/', include('trainer.urls', namespace='price')),
    path('trainer/', include('trainer.urls', namespace='master')),
    path('gallery/', include('blog.urls', namespace='gallery')),
    path('', include('pages.urls', namespace='home')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
