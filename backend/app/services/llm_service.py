from app.services.rag_service import retrieve_relevant_chunks

def get_ai_response(user_input: str) -> str:
    chunks = retrieve_relevant_chunks(user_input)

    context = chunks[0] if chunks else "No data found"

    return f"{context}"