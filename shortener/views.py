from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import URLForm
from .models import ShortenedURL
from .utils import generate_short_code


def main_page(request):
    return render(request, "main_page.html")


def about(request):
    return render(request, "shortener/about.html")


def shorten_url(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data["original_url"]

            # Проверяем уникальность URL
            existing_url = ShortenedURL.objects.filter(
                original_url=original_url
            ).first()
            if existing_url:
                short_url = request.build_absolute_uri(f"/{existing_url.short_code}")
                return render(
                    request, "shortener/success.html", {"short_url": short_url}
                )

            short_code = generate_short_code()
            while ShortenedURL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()

            shortened_url = ShortenedURL.objects.create(
                original_url=original_url, short_code=short_code
            )
            short_url = request.build_absolute_uri(f"/{short_code}")
            return render(
                request,
                "shortener/success.html",
                {"short_url": short_url, "reused": True},
            )

    else:
        form = URLForm()
    return render(request, "shortener/form.html", {"form": form})


def redirect_to_original(request, short_code):
    url = get_object_or_404(ShortenedURL, short_code=short_code)
    return HttpResponseRedirect(url.original_url)


def url_list(request):
    urls = ShortenedURL.objects.all()
    for url in urls:
        url.full_short_url = request.build_absolute_uri(f"/{url.short_code}")
    return render(request, "shortener/url_list.html", {"urls": urls})
