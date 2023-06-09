"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# include umożliwia import urls z applikacji
from django.conf import settings
from django.conf.urls.static import static
# from django.conf import settings
# from django.conf.urls.static import static - tylko lokalnie, nie robić tak na produkcji!
from django.contrib.auth import views as auth_view
from rest_framework import routers
from movies_web.views import UserView, MovieView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'movies', MovieView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies_web/', include('movies_web.urls')),
    path('login/', auth_view.LoginView.as_view(), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(), name = 'logout'),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # tylko na local
