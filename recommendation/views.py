import os
import json
import random

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
    context = {
        "wallpapers": random.sample(list(dataset.keys()), 50),
        "options": [
            "cute",
            "animal",
            "dark",
            "music",
            "artist",
            "pink",
            "blue",
            "abstract",
            "hq",
            "game",
            "anime",
        ],
    }

    return render(request, "recommendation/home.html", context=context)


def recommendations(request, wallpaper):
    recommendations = recommend(wallpaper, dataset)

    recommendations_images = []
    for recommendation in recommendations[:10]:
        recommendations_images.append(recommendation[1])

    context = {"wallpaper": wallpaper, "recommendations": recommendations_images}
    return render(request, "recommendation/recommendations.html", context=context)


def options_recommendation(request):
    if request.method == "POST":
        option_1 = request.POST.get("option1")
        option_2 = request.POST.get("option2")

        wallpaper = {
            "cute": 0,
            "animal": 0,
            "dark": 0,
            "music": 0,
            "artist": 0,
            "pink": 0,
            "blue": 0,
            "abstract": 0,
            "hq": 0,
            "game": 0,
            "anime": 0,
        }

        wallpaper[option_1] = 5
        wallpaper[option_2] = 5

        recommendations = recommend(wallpaper, dataset)

        recommendations_images = []
        for recommendation in recommendations[:10]:
            recommendations_images.append(recommendation[1])

        context = {"recommendations": recommendations_images}
        return render(request, "recommendation/recommendations.html", context=context)
