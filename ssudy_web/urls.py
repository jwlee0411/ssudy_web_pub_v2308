"""ssudy_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('book/', include('book.urls')),
    path('clubs/', include('clubs.urls')),
    path('common/', include('common.urls')),
    path('', include('home.urls')),
    path('intro/', include('intro.urls')),
    path('manager/', include('manager.urls')),
    path('supply/', include('supply.urls')),
    path('survey/', include('survey.urls')),
    path('user/', include('user.urls', namespace='articles')),
    path('maintenance/', views.maintenance),
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
