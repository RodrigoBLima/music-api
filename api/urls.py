"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API para fãs de música')

# VIEWSETS
from accounts.viewsets import UserViewSet
from musics.viewsets import TracksViewSet
from artists.viewsets import ArtistsViewSet
from playlist.viewsets import AlbumViewSet

router = routers.DefaultRouter()

router.register(r'accounts', UserViewSet)
router.register(r'musics', TracksViewSet)
router.register(r'artists', ArtistsViewSet)
router.register(r'playlists', AlbumViewSet)

urlpatterns = [
    url(r'^api/v1/$', schema_view),
    url('admin/', admin.site.urls),
    url(r'api/v1/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)