from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Textes à vectoriser
textes = ["Le chat dort sur le tapis.", "Le chat est sur son ventre"]

# Obtention des embeddings
embeddings = model.encode(textes)

print(f"========================= {embeddings}")

# Vecteurs des deux textes
vec1 = embeddings[0]
vec2 = embeddings[1]

# Calcul de la similarité cosinus
similarité = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print(f"Similarité : {similarité}")
