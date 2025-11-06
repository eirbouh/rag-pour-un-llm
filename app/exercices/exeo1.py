from pathlib import Path
import packages.generic as generic

INPUT_DIRECTORY = Path(r"C:\Users\eir20812\opt\projet\LLM\RAG-LLM\inputs")
OUTPUT_DIRECTORY = Path(r"C:\Users\eir20812\opt\projet\LLM\RAG-LLM\markdown_output")
# Extensions prises en charge
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".csv", ".txt", ".xlsx", ".wav", ".webp", ".png"]

filesToConvert = generic.prepareFileToConversion(INPUT_DIRECTORY , OUTPUT_DIRECTORY, SUPPORTED_EXTENSIONS)  
# conversion de chaque fichier 
generic.doConversion(filesToConvert, OUTPUT_DIRECTORY )
# sauvegarde du fichier dans le repertoire de sortie


