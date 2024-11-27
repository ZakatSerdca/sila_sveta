from django.db import models


class UploadedImage(models.Model):
    image = models.ImageField(upload_to="static/images/")  # Путь сохранения файлов
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата загрузки
    permanent_link = models.CharField(max_length=255, blank=True)  # Постоянная ссылка

    def save(self, *args, **kwargs):
        # Генерация постоянной ссылки при сохранении
        if not self.permanent_link:
            self.permanent_link = f"/static/images/{self.image}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image: {self.image.name}"
