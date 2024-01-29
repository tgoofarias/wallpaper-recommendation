import os
import json

from django.shortcuts import render
from django.templatetags.static import static
from django.conf import settings

from .utils import recommend


dataset_path = f"{settings.BASE_DIR}{static('dataset/dataset.json')}"
wallpapers_path = f"{settings.BASE_DIR}{static('images/wallpapers/')}"
wallpapers_images = os.listdir(wallpapers_path)


with open(dataset_path) as dataset_json:
    dataset = json.load(dataset_json)


def home(request):
    wallpapers_with_data_in_dataset = []
    for wallpaper_image in wallpapers_images:
        wallpaper_image_formatted = (
            wallpaper_image.replace(".png", "")
            .replace(".jpg", "")
            .replace(".gif", "")
            .replace(".jpeg", "")
        )
        if wallpaper_image_formatted in dataset.keys():
            wallpapers_with_data_in_dataset.append(wallpaper_image)

    context = {"wallpapers": wallpapers_with_data_in_dataset}

    return render(request, "recommendation/home.html", context=context)


def recommendations(request, wallpaper):
    wallpaper_formatted = (
        wallpaper.replace(".png", "")
        .replace(".jpg", "")
        .replace(".gif", "")
        .replace(".jpeg", "")
    )

    recommendations = recommend(wallpaper_formatted, dataset)

    recommendations_images = []
    for recommendation in recommendations[:10]:
        for image in wallpapers_images:
            if image.startswith(recommendation[1]):
                recommendations_images.append(image)
                break

    context = {"wallpaper": wallpaper, "recommendations": recommendations_images}
    return render(request, "recommendation/recommendations.html", context=context)
