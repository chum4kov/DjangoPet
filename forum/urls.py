
from django.contrib import admin
from django.urls import path, include
from info.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('add-post', add_post, name='add-post'),
    path('post/<int:post_id>', one_post, name='post'),
    path('add_like/<int:post_id>', add_like, name='add-like'),
    path('reg/', register, name='reg'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:user_id>/', profile, name='profile'),

    path('captcha/', include('captcha.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)