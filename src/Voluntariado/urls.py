"""Voluntariado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

from solicitud_proyecto.views import SolicitudViewSet
from project_images.views import ProjectImagesViewSet
from faculties.views import FacultyViewSet
from majors.views import MajorViewSet
from project_request_links.views import ProjectRequestLinksViewSet
from users.views import UserViewset

router = routers.DefaultRouter()
router.register(r'^solicitud-proyecto', SolicitudViewSet)
router.register(r'^project-images', ProjectImagesViewSet)
router.register(r'^faculties', FacultyViewSet)
router.register(r'^majors', MajorViewSet)
router.register(r'^project-links', ProjectRequestLinksViewSet)
router.register(r'^users', UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
