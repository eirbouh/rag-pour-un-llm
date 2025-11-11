
import os, sys
from docling.document_converter import DocumentConverter
from pathlib import Path

def doConversion(input_dir):
    # ⚙️ Création du convertisseur global
    converter = DocumentConverter()

    #input_dir = Path(r"C:\Users\eir20812\opt\projet\LLM\RAG-LLM\inputs\budget")
    output_dir = Path(r"/opt/projets/llm/rag-pour-un-llm/markdown_outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    input_dir = Path(input_dir)

    # 📜 Extensions prises en charge
    SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".csv", ".txt", ".xlsx"]

    # 🚀 Parcours de tous les fichiers du dossier

    for file_path in input_dir.rglob("*"):
        if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            try:
                print(f"🔄 Conversion de : {file_path.name}")

                # La méthode convert renvoie un résultat avec l’attribut .document
                result = converter.convert(file_path)

                # Nom du fichier Markdown de sortie
                output_path = output_dir / f"{file_path.stem}.md"

                # Export du contenu en Markdown
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result.document.export_to_markdown())

                print(f"✅ Fichier converti → {output_path}")

            except Exception as e:
                print(f"❌ Erreur lors de la conversion de {file_path.name} : {e}")


def doConvertion (source):
    # Change this to a local path or another URL if desired.
    # Note: using the default URL requires network access; if offline, provide a
    # local file path (e.g., Path("/path/to/file.pdf")).
    converter = DocumentConverter()
    result = converter.convert(source)

    # Print Markdown to stdout.
    print(result.document.export_to_markdown())

def lister_dossiers(base_path):
    dossiers = []
    for dossier, sous_dossiers, fichiers_dans_dossier in os.walk(base_path):
       dossiers.append(dossier)
    return dossiers

def lister_fichiers(base_path):
    fichiers = []
    for dossier, sous_dossiers, fichiers_dans_dossier in os.walk(base_path):
        for fichier in fichiers_dans_dossier:
            nom, extension = os.path.splitext(fichier)
            fichiers.append((os.path.join(dossier, fichier), extension))
    return fichiers


# Exemple d’utilisation :
INPUT_DIRECTORY = Path(r"/opt/projets/llm/rag-pour-un-llm/inputs")
OUTPUT_DIRECTORY = "/opt/projets/llm/rag-pour-un-llmmarkdown_outputs" # Nom du dossier de sortie
resultats = lister_dossiers(INPUT_DIRECTORY)

print(resultats)

for chemin_complet in resultats:
  doConversion(chemin_complet) 
  #doConversion(f"r{chemin_complet}", OUTPUT_DIRECTORY) 


