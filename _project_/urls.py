"""
URL configuration for _project_ project.

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
from django.urls import include, path

from shortener.views import main_page, redirect_to_original

urlpatterns = [
    path('', main_page, name='main_page'),
    path('admin/', admin.site.urls),
    path('shortener/', include('shortener.urls')),
    path('images/', include('image_url.urls')),
    path('<str:short_code>/', redirect_to_original, name='redirect_to_original'),
]
