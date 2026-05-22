import faiss
import numpy as np
from app.services.embedding_service import get_embedding

documents = []
embeddings = None
index = None


def store_document(text: str):
    global documents, embeddings, index

    # split lines
    documents = text.split("\n")

    # create embeddings (fixed size)
    embeddings = np.array([get_embedding(doc) for doc in documents]).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)


def retrieve_relevant_chunks(query: str):
    global documents, index

    query = query.lower()

    # ✅ smarter intent-based matching

    # backend-related queries
    if "backend" in query or "server" in query:
        for doc in documents:
            if "java" in doc.lower():
                return [doc]

    # java queries
    if "java" in query:
        for doc in documents:
            if "java" in doc.lower():
                return [doc]

    # python queries
    if "python" in query or "ai" in query or "machine learning" in query:
        for doc in documents:
            if "python" in doc.lower():
                return [doc]

    # fastapi queries
    if "fastapi" in query or "api" in query:
        for doc in documents:
            if "fastapi" in doc.lower():
                return [doc]

    # ✅ fallback → FAISS
    if index is not None:
        import numpy as np
        from app.services.embedding_service import get_embedding

        query_vector = np.array([get_embedding(query)]).astype("float32")
        distances, indices = index.search(query_vector, k=1)
        return [documents[indices[0][0]]]

    return []
