from django.urls import path

from . import views

urlpatterns = [
    path("", views.about, name="about"),
    path("list/", views.url_list, name="url_list"),  # Список ссылок
    path("shorter/", views.shorten_url, name="shorten_url"),  # Сокрощатель
]
