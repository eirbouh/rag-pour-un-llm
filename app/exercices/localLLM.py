from fastapi import FastAPI, HTTPException
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from pydantic import BaseModel

app = FastAPI(title="Local LLM API", version="1.0")

# === Configuration du modèle ===
MODEL_PATH = "qwen/qwen3-4b-thinking-2507"

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        device_map="auto",  # GPU si disponible
        torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
        trust_remote_code=True
    )
except Exception as e:
    raise RuntimeError(f"Erreur lors du chargement du modèle : {e}")

# === Schéma d'entrée ===
class Item(BaseModel):
    text: str

# === Route de test ===
@app.get("/")
async def root():
    return {"message": "🚀 Local LLM API est en ligne ! Essayez /generate/ avec une requête POST."}

# === Route principale ===
@app.post("/generate/")
async def generate_text(item: Item):
    """Génère une réponse à partir du texte fourni."""
    try:
        # Préparation de l'entrée
        inputs = tokenizer(
            item.text,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        # Génération du texte
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id
            )

        # Décodage
        generated_text = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )

        # Nettoyage du texte généré
        if generated_text.startswith(item.text):
            generated_text = generated_text[len(item.text):].strip()

        return {"generated_text": generated_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur pendant la génération : {str(e)}")

# === Exécution locale ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.exercices.localLLM:app", host="0.0.0.0", port=8000, reload=True)
