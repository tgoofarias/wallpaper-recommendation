def manhattan(wallpaper1, wallpaper2):
    distance = 0
    total = 0
    for key in wallpaper1:
        if key in wallpaper2:
            distance += abs(wallpaper1[key] - wallpaper2[key])
            total += 1
    return distance


def recommend(wallpaper_name, wallpapers):
    wallpaper_selected = (
        wallpapers[wallpaper_name]
        if not isinstance(wallpaper_name, dict)
        else wallpaper_name
    )
    distances = []
    for wallpaper in wallpapers:
        if wallpaper != wallpaper_name:
            distance = manhattan(wallpapers[wallpaper], wallpaper_selected)
            distances.append((distance, wallpaper))
    distances.sort()
    return distances
