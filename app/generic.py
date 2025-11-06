import os, torch
from docling.document_converter import DocumentConverter
from pathlib import Path

"""
 retourner la liste des fichiers d'un dossier passé en paramètre 
"""
def getNodeFiles(directory: str):
  returnFiles = []
  if not os.path.isdir(directory):
    print(f"Erreur : Le répertoire d'entrée '{directory}' n'existe pas.")
    return
  
  for elet in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, elet)):
      nom, extension = os.path.splitext(elet)
      returnFiles.append((os.path.join(directory, elet), extension))
  return returnFiles


"""
 retourne la liste de fichiers en fonction de :
    - directory : le dossier de l'arborescence racine
    - supported_extension : tableau des extensions des ficheirs à retenir 
 """
def getFilestoConvert(directory=str, supported_extension=[]):
  returnFiles = []
  if not os.path.isdir(directory):
    print(f"Erreur : Le répertoire d'entrée '{directory}' n'existe pas.")
    return

  for file_path in directory.rglob("*"):
    if file_path.suffix.lower() in supported_extension:
      returnFiles.append(file_path)

  return returnFiles

"""
 parcourir une arborescence et retourner la liste de ses dossiers 
"""
def getTree(rootTree: str):
  if not os.path.isdir(rootTree):
    print(f"Erreur : Le répertoire d'entrée '{rootTree}' n'existe pas.")
    return
  directories = []
  for rep , subrep, files in os.walk(rootTree):
    directories.append(rep)
  return directories


def doConversion(fileToConvert, output_dir ):
    # ⚙️ Création du convertisseur global
    converter = DocumentConverter()

    # 🚀 Parcours de tous les fichiers du dossier

    for file_path in fileToConvert:
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

"""
   - verfier que le inputDir exist
   - Creer le outputDir
   - récupérer tous les ficheirs de inputDir
   - verfier que les extension sont admises
   - lancer le processus de conversion
   - ecrire le fichier converti dans le outputDir
"""
def prepareFileToConversion(inputDir, outputDir, supported_extension):
  if not os.path.isdir(inputDir):
    print(f"{inputDir} not found")
    return

  # creation du repertoire de sortie s'il n'existe pas
  if not os.path.isdir(outputDir):
    try:
      os.makedirs(outputDir)
      print(f"Répertoire de sortie '{outputDir}' créé.")
    except OSError as e:
      print(f"Erreur lors de la création du répertoire de sortie '{outputDir}': {e}")
      return
  
  # récupération de tous les fichiers à convertir depuis inputDir
  filesToConvert = getFilestoConvert(inputDir, supported_extension)
  if len(filesToConvert)==0 :
    print (f"{inputDir} : ne contient aucun fichier a convertir ")
    return 

  return filesToConvert          