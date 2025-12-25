import os
import shutil
from pathlib import Path

def build_dist():
    raiz = Path(__file__).parent
    dist = raiz / "Compilado"
    
    if dist.exists(): shutil.rmtree(dist)
    dist.mkdir()

    # Pega todos os .pyd e joga na RAIZ da pasta Compilado
    for pyd in raiz.rglob("*.pyd"):
        if "Compilado" in str(pyd): continue
        nome_limpo = pyd.name.split('.')[0] + ".pyd"
        shutil.copy2(pyd, dist / nome_limpo)
        print(f"Copiado: {nome_limpo}")

    # Copia o disparador
    shutil.copy2(raiz / "__main__.py", dist / "__main__.py")
    
    with open(dist / "AbrirApp.bat", "w") as f:
        f.write("@echo off\npython __main__.py\npause")

if __name__ == "__main__":
    build_dist()