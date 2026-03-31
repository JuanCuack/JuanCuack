import requests
import os

# URLs con instancias estables (mirror), idioma español y estética TokyoNight
WIDGETS = {
    "streak.svg": "https://github-readme-streak-stats.herokuapp.com/?user=JuanCuack&theme=tokyonight&hide_border=false&background=1a1b27&ring=11eeff&fire=ff9f43&stroke=11eeff&locale=es",
    
    "languages.svg": "https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=JuanCuack&layout=compact&theme=tokyonight&hide_border=false&title_color=11eeff&icon_color=ff9f43&bg_color=1a1b27&locale=es",
    
    "statistics.svg": "https://github-readme-stats-sigma-five.vercel.app/api?username=JuanCuack&show_icons=true&theme=tokyonight&hide_border=false&bg_color=1a1b27&title_color=11eeff&icon_color=ff9f43&text_color=11eeff&locale=es&count_private=true"
}

def update_assets():
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    for name, url in WIDGETS.items():
        try:
            print(f"🔄 Sincronizando {name}...")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=30)
            
            # Validación: Solo guardamos si recibimos un SVG real
            if response.status_code == 200 and "<svg" in response.text:
                with open(os.path.join("assets", name), "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"✅ {name} actualizado con éxito.")
            else:
                print(f"⚠️ {name} saltado (Respuesta inválida del servidor: {response.status_code}).")
        except Exception as e:
            print(f"❌ Error en {name}: {str(e)}")

if __name__ == "__main__":
    update_assets()
