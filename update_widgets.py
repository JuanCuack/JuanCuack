import os
import requests

# URLs oficiales con estética TokyoNight y soporte en español
WIDGETS = {
    "streak.svg": (
        "https://github-readme-streak-stats.herokuapp.com/"
        "?user=JuanCuack&theme=tokyonight&hide_border=false"
        "&background=1a1b27&ring=11eeff&fire=ff9f43&stroke=11eeff"
    ),
    "languages.svg": (
        "https://github-readme-stats.vercel.app/api/top-langs/"
        "?username=JuanCuack&theme=tokyonight&hide_border=false"
        "&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27"
        "&locale=es&langs_count=5"
    ),
    "statistics.svg": (
        "https://github-readme-stats.vercel.app/api"
        "?username=JuanCuack&show_icons=true&theme=tokyonight"
        "&hide_border=false&bg_color=1a1b27&title_color=11eeff"
        "&icon_color=ff9f43&text_color=11eeff&locale=es&count_private=true"
    )
}

# Palabras clave emitidas en respuestas de error de las APIs
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
                and not any(error.lower() in response.text.lower() for error in ERROR_INDICATORS)
            )

            if is_valid_svg:
                file_path = os.path.join("assets", name)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"✅ {name} actualizado con éxito.")
            else:
                print(f"⚠️ {name} saltado: Error de API o rate limit detectado (Status: {response.status_code}). Se conserva la versión anterior.")

        except Exception as e:
            print(f"❌ Error al procesar {name}: {str(e)}")

if __name__ == "__main__":
    update_assets()
