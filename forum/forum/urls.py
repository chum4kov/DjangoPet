
from django.contrib import admin
from django.urls import path
from info.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('post/<int:post_id>', one_post, name='post'),
    path('add_like/', add_like, name='add-like')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)