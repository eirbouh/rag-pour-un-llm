import os
import P1C3_exercice as DoConverter
import sys


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



print(sys.executable)


# Exemple d’utilisation :
INPUT_DIRECTORY = "C:\\Users\\eir20812\\opt\\projet\\LLM\\RAG-LLM\\inputs"
OUTPUT_DIRECTORY = "C:\\Users\\eir20812\\opt\\projet\\LLM\\RAG-LLM\\markdown_outputs" # Nom du dossier de sortie
resultats = lister_dossiers(INPUT_DIRECTORY)

# Affichage
# for chemin_complet, extension in resultats:
#    print(f"{chemin_complet} → {extension}")

for chemin_complet in resultats:
  DoConverter.convert_documents_to_markdown(chemin_complet, OUTPUT_DIRECTORY)
