from django.db import models


class ShortenedURL(models.Model):
    """Модель для информации о сокращении ссылок.

    Attributes:
        original_url (str): Длинная ссылка, загружаемая пользователем.
        short_code (str): Сгенерированная уникальная короткая строка.
        created_at (datetime): Дата создания.
    """

    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
