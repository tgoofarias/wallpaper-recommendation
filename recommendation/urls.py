from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "recommendations/<str:wallpaper>",
        views.recommendations,
        name="recommendations",
    ),
]
