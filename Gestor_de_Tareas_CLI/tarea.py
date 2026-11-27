import typer
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_dir = BASE_DIR / "tareas.json"

app = typer.Typer()
# ============================================================================|
try:
    with open(file_dir,"r",encoding="utf-8") as f:
        lista_de_tareas = json.load(f)
except FileNotFoundError:
    with open(file_dir, "w",encoding="utf-8")as f:
        json.dump([],f)
        lista_de_tareas = []

# Escribir en archivo json
def cargar_json():
    with open(file_dir,"w", encoding="utf-8") as f:
        json.dump(lista_de_tareas,f, indent=2)

# ============================================================================|
# Agregar tarea
@app.command()
def agg(tarea: str):
    lista_de_tareas.append([{"tarea": tarea}])
    cargar_json()
    print("Tarea agregada. ")



# ****************************************************************************|
@app.callback()
def main():
    pass
if __name__ == "__main__":
    app()
# ****************************************************************************|