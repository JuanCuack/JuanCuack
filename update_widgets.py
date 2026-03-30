import requests
import os

# Diccionario con tus widgets y parámetros estéticos exactos
WIDGETS = {
    "streak.svg": "https://github-readme-streak-stats.herokuapp.com/?user=JuanCuack&theme=tokyonight&hide_border=false&background=1a1b27&ring=11eeff&fire=ff9f43&stroke=11eeff&locale=es&cache_seconds=600",
    "langs.svg": "https://github-readme-stats.vercel.app/api/top-langs/?username=JuanCuack&layout=compact&theme=tokyonight&hide_border=false&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27&locale=es&cache_seconds=600",
    "stats.svg": "https://github-readme-stats.vercel.app/api?username=JuanCuack&show_icons=true&theme=tokyonight&hide_border=false&bg_color=1a1b27&title_color=11eeff&icon_color=ff9f43&text_color=11eeff&locale=es&count_private=true&include_all_commits=true&cache_seconds=600"
}

def update_assets():
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    for name, url in WIDGETS.items():
        try:
            print("🔄 Sincronizando {0}...".format(name))
            response = requests.get(url, timeout=30)
            
            # Validación: Solo guardamos si recibimos un SVG real
            if response.status_code == 200 and "<svg" in response.text:
                with open(os.path.join("assets", name), "w", encoding="utf-8") as f:
                    f.write(response.text)
                print("✅ {0} actualizado con éxito.".format(name))
            else:
                print("⚠️ {0} saltado (Respuesta inválida del servidor externo).".format(name))
        except Exception as e:
            print("❌ Error en {0}: {1}".format(name, str(e)))

if __name__ == "__main__":
    update_assets()
