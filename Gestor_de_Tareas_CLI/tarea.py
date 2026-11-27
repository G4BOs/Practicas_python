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
def agregar(tarea: str):
    tarea_obj = {
        "tarea": tarea,
        "completo": False,
        "id": lista_de_tareas[-1]["id"] +1
    }
    lista_de_tareas.append(tarea_obj)
    cargar_json()
    print("Tarea agregada. ")
# ----------------------------------------------/

# Quitar tarea
@app.command()
def quitar (id: int):
    for n in lista_de_tareas:
        if n["id"] == id:
            del lista_de_tareas[ lista_de_tareas.index(n)]
    cargar_json()

@app.command()
def marcar(id: int):
    for n in lista_de_tareas:
        if n["id"] == id:
            n["completo"] = True
    cargar_json()

@app.command()
def ver(inc: bool=False):
    print(f"Tareas:\n{'\n'.join([f"\n[{t["tarea"]}]\n[id: {t["id"]} Completo: {'Si' if t["completo"] else "No"}]" for t in lista_de_tareas])}")

# ****************************************************************************|
@app.callback()
def main():
    pass
if __name__ == "__main__":
    app()
# ****************************************************************************|