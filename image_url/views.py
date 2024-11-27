from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ImageUploadForm
from .models import UploadedImage
from .serializers import ImageSerializer


def about_image_service(request):
    return render(request, "image_url/about.html")


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = ImageUploadForm()
    return render(request, "image_url/form.html", {"form": form})


def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, "image_url/image_list.html", {"images": images})


class ImageUploadAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]  # Обработчики для файлов

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save()  # Сохраняем изображение
            return Response(
                {
                    "message": "Изображение успешно загружено!",
                    "image_url": image.permanent_link,
                    "file_name": image.image.name,
                    "uploaded_at": image.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
