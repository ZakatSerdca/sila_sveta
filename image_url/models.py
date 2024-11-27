from django.db import models


class UploadedImage(models.Model):
    """Модель для информации о загруженных изображениях

    Attributes:
        image (str): Путь к загруженному изображению.
        uploaded_at (datetime): Дата загрузки.
        permanent_link (str): Постоянная ссылка на изображение.
    """

    image = models.ImageField(upload_to="static/images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    permanent_link = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Генерация ссылки при сохранении
        if not self.permanent_link:
            self.permanent_link = f"/static/images/{self.image}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image: {self.image.name}"
