from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('home/', include('apps.main.urls')),
    path('menu/', include('apps.menu.urls')),
    path('', include('apps.menu_details.urls')),
    #path('sign_up', include('apps.sign_up.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('apps.users.urls')),
    path('profile/', include('apps.userProfile.urls'))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
