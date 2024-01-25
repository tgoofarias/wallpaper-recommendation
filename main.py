import json

import streamlit as st


with open("dataset.json", "r") as dataset_json:
    wallpapers = json.load(dataset_json)


def manhattan(wallpaper1, wallpaper2):
    distance = 0
    total = 0
    for key in wallpaper1:
        if key in wallpaper2:
            distance += abs(wallpaper1[key] - wallpaper2[key])
            total += 1
    return distance


def recommend(wallpaper_name, wallpapers):
    wallpaper_selected = wallpapers[wallpaper_name]
    distances = []
    for wallpaper in wallpapers:
        if wallpaper != wallpaper_name:
            distance = manhattan(wallpapers[wallpaper], wallpaper_selected)
            distances.append((distance, wallpaper))
    distances.sort()
    return distances


def main():
    st.title("Selecione uma imagem")

    imagens = [k for k in wallpapers.keys()]
    checkboxes_state = []

    cols = st.columns(2, gap="large")

    aux = 0
    for i, image in enumerate(imagens):
        if aux == 2:
            aux = 0
        checkbox_state = cols[aux].checkbox(f"Selecionar Imagem {i+1}", key=i)
        checkboxes_state.append((checkbox_state, image))
        for extension in [".png", ".gif", ".jpg", ".jpeg"]:
            try:
                cols[aux].image(
                    f"images/{image}{extension}",
                    use_column_width=False,
                    caption=f"Imagem {i+1}",
                    width=300,
                )
            except:
                pass
        aux += 1

    if st.button("Recomendar"):
        for state in checkboxes_state:
            if state[0]:
                st.write("Wallpapers recomendados")

                wallpaper_name = state[1]
                for extension in [".png", ".gif", ".jpg", ".jpeg"]:
                    try:
                        wallpaper_name.replate(extension, "")
                    except:
                        pass

                recomendations = recommend(wallpaper_name, wallpapers)

                for wallpaper in recomendations[:10]:
                    for extension in [".png", ".gif", ".jpg", ".jpeg"]:
                        try:
                            st.image(
                                f"images/{wallpaper[1]}{extension}",
                                use_column_width=False,
                                caption=f"Imagem {i+1}",
                                width=300,
                            )
                        except:
                            pass


if __name__ == "__main__":
    main()
