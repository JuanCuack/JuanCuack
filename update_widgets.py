import os
import requests

# Endpoints estables usando la instancia de herokuapp / vercel
WIDGETS = {
    "streak.svg": (
        "https://github-readme-streak-stats.herokuapp.com/"
        "?user=JuanCuack&theme=tokyonight&hide_border=false"
        "&background=1a1b27&ring=11eeff&fire=ff9f43&stroke=11eeff"
    ),
    "languages.svg": (
        "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/"
        "?username=JuanCuack&theme=tokyonight&hide_border=false"
        "&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27"
        "&locale=es&langs_count=5"
    ),
    "statistics.svg": (
        "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api"
        "?username=JuanCuack&show_icons=true&theme=tokyonight"
        "&hide_border=false&bg_color=1a1b27&title_color=11eeff"
        "&icon_color=ff9f43&text_color=11eeff&locale=es&count_private=true"
    ),
    "pin_codeshift.svg": (
        "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/pin/"
        "?username=JuanCuack&repo=CodeShift&theme=tokyonight&show_icons=true"
        "&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27"
    ),
    "pin_darkquiz.svg": (
        "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/pin/"
        "?username=JuanCuack&repo=DarkQuiz-Engine&theme=tokyonight&show_icons=true"
        "&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27"
    ),
    "pin_horarius.svg": (
        "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/pin/"
        "?username=JuanCuack&repo=Horarius&theme=tokyonight&show_icons=true"
        "&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27"
    )
}

ERROR_INDICATORS = [
    "Something went wrong",
    "Maximum retries exceeded",
    "rate limit",
    "Please add an env variable"
]

def update_assets():
    os.makedirs("assets", exist_ok=True)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    for name, url in WIDGETS.items():
        try:
            print(f"🔄 Sincronizando {name}...")
            response = requests.get(url, headers=headers, timeout=30)

            is_valid_svg = (
                response.status_code == 200
                and "<svg" in response.text
                and not any(err.lower() in response.text.lower() for err in ERROR_INDICATORS)
            )

            if is_valid_svg:
                file_path = os.path.join("assets", name)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"✅ {name} actualizado correctamente.")
            else:
                print(f"⚠️ {name} saltado por respuesta no válida (HTTP {response.status_code}).")

        except Exception as e:
            print(f"❌ Error en {name}: {str(e)}")

if __name__ == "__main__":
    update_assets()
