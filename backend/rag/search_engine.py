import pickle
import faiss

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "vector_db/faiss_index.bin"
)

with open(
    "vector_db/documents.pkl",
    "rb"
) as file:

    documents = pickle.load(file)


def search_knowledge(
    query,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(
            documents[idx]
        )

    return results