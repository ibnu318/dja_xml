from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from recipes.models import Recipe

info_dict = {
    "queryset": Recipe.objects.all(),
    "date_field": "updated_at",
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("recipes.urls")),
    
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"recipes": GenericSitemap(info_dict)}},
    ),
]
