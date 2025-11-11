from pathlib import Path
import whisper

# Transcrire avec Whisper
def transcribe_audio_with_whisper(audio_file, model_name="base"):
    # Charger le modèle Whisper
    model = whisper.load_model(model_name)

    # Transcrire le fichier audio
    result = model.transcribe(str(audio_file))  # ✅ convertir Path en str

    # Afficher la transcription
    print("Transcription :")
    print(result["text"])

# Transcrire l'audio avec Whisper
INPUT_FILE = Path("/opt/projets/llm/rag-pour-un-llm/inputs/communication/voeux2025_trifouillis.wav")
transcribe_audio_with_whisper(INPUT_FILE)