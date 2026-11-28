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
def guardar_json():
    with open(file_dir,"w", encoding="utf-8") as f:
        json.dump(lista_de_tareas,f, indent=2)

# ============================================================================|
# --------------------------------------------------------------| Agregar tarea
@app.command()
def agregar(tarea: str):
    tarea_obj = {
        "tarea": tarea,
        "completo": False,
        "id": lista_de_tareas[-1]["id"] +1 if lista_de_tareas else 1
    }
    lista_de_tareas.append(tarea_obj)
    guardar_json()
    print("Tarea agregada. ")
# ----------------------------------------------/

# ----------------------------------------------------------------|Quitar tarea
@app.command()
def quitar (id: int):
    for n in lista_de_tareas:
        if n["id"] == id:
            del lista_de_tareas[ lista_de_tareas.index(n)]
    guardar_json()
# ----------------------------------------------/

# ---------------------------------------------------------------| Marcar Hecho
@app.command()
def marcar(id: int):
    for n in lista_de_tareas:
        if n["id"] == id:
            n["completo"] = True
    guardar_json()
# ----------------------------------------------/

# -----------------------------------------------------------------| Ver Tareas
@app.command()
def ver(completas: bool=False, incompletas: bool = False):

    if completas and incompletas:
        print(" [!] Solo usa --completas o --incompletas [!]")
        return
    
    if completas:
        tareas_filtradas = [t for t in lista_de_tareas if t["completo"]]
    elif incompletas:
        tareas_filtradas = [t for t in lista_de_tareas if not t["completo"]] 
    else:
        tareas_filtradas = lista_de_tareas
    
    if not tareas_filtradas:
        print("No hay tareas con ese filtro.")
        return
    
    print("\nTareas:")
    for t in tareas_filtradas:
        estado: str = "Completa" if t["completo"] else "Incompleta"
        print(f"[TAREA ID: {t["id"]}] [Estado: {estado}]")
        print(f"> {t["tarea"]}\n{"-"*20}\n")

# ****************************************************************************|
@app.callback()
def main():
    pass
if __name__ == "__main__":
    app()
# ****************************************************************************|