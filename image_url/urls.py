from django.urls import path

from .views import ImageUploadAPI, about_image_service, image_list, upload_image

urlpatterns = [
    path("", about_image_service, name="about_image_service"),
    path("upload/", upload_image, name="upload_image"),
    path("list/", image_list, name="image_list"),
    path("api/upload/", ImageUploadAPI.as_view(), name="api_upload_image"),
]
