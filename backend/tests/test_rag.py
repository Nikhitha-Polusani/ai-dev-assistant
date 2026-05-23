from app.services.rag_service import store_document, retrieve_relevant_chunks

def test_rag():
    text = "Java is a backend language\nPython is used in AI"
    store_document(text)

    result = retrieve_relevant_chunks("backend")

    assert "Java" in result[0]
    
def test_no_matching_query():
    store_document("Java backend\nPython AI")

    result = retrieve_relevant_chunks("blockchain")

    assert result is not None


def test_multiple_lines():
    text = """Java backend
Python AI
FastAPI framework"""
    
    store_document(text)
    
    result = retrieve_relevant_chunks("api")

    assert isinstance(result, list)

def test_empty_query():
    store_document("Java backend")
    result = retrieve_relevant_chunks("")
    assert result is not None


def test_query_python():
    store_document("Java backend\nPython AI")
    result = retrieve_relevant_chunks("python")
    assert "Python" in result[0]


def test_query_fastapi():
    store_document("FastAPI is used")
    result = retrieve_relevant_chunks("api")
    assert result is not None