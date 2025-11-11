from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Test API")

class Item(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "API en ligne"}

@app.post("/generate/")
async def generate_text(item: Item):
    return {"generated_text": f"Tu as envoyé : {item.text}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.exercices.localLLM:app", host="0.0.0.0", port=8000, reload=True)
