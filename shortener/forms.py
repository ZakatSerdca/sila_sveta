from django import forms

from .models import ShortenedURL


class URLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ["original_url"]
        widgets = {
            "original_url": forms.URLInput(  # <input type="url">
                attrs={"class": "form-control", "placeholder": "Введите ссылку"}
            ),
        }
        labels = {
            "original_url": "Ссылка для сокращения",
        }
