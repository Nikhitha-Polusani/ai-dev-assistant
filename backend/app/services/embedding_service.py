def get_embedding(text):
    # ✅ fixed length embedding (size = 50)
    vector = [0] * 50

    for i, char in enumerate(text[:50]):
        vector[i] = ord(char)

    return vector
