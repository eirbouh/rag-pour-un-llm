from pathlib import Path

def lister_fichiers(base_path):
    base = Path(base_path)
    fichiers = [(str(f), f.suffix) for f in base.rglob('*') if f.is_file()]
    return fichiers

# Exemple :
chemin = "C:\\Users\\eir20812\\opt\\projet\\LLM\\RAG-LLM\\inputs"
resultats = lister_fichiers(chemin)

for chemin_complet, extension in resultats:
    print(f"{chemin_complet} → {extension}")
