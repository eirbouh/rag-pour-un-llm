import requests

resp = requests.post(
    "http://localhost:8000/generate/",
    json={"text": "Explique-moi la différence entre l'IA et le machine learning."}
)
print(resp.json())
