import json
import pickle
import faiss

from sentence_transformers import (
    SentenceTransformer
)

# Load Disease Knowledge

with open(
    "datasets/disease_knowledge.json",
    "r",
    encoding="utf-8"
) as file:

    diseases = json.load(file)

# Embedding Model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []

for disease in diseases:

    text = f"""
    Crop: {disease['crop']}
    Disease: {disease['disease']}
    Symptoms: {' '.join(disease['symptoms'])}
    Cause: {disease['cause']}
    Treatment: {disease['treatment']}
    Prevention: {disease['prevention']}
    """

    documents.append(text)

# Create Embeddings

embeddings = model.encode(
    documents,
    convert_to_numpy=True
)

# Create FAISS Index

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

# Save Index

faiss.write_index(
    index,
    "vector_db/faiss_index.bin"
)

# Save Documents

with open(
    "vector_db/documents.pkl",
    "wb"
) as file:

    pickle.dump(
        documents,
        file
    )

print(
    f"Indexed {len(documents)} diseases"
)