from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_ai_response

from fastapi import UploadFile, File
from app.services.rag_service import store_document

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    reply = get_ai_response(request.message)
    return {"response": reply}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    store_document(text)

    return {"message": "File uploaded successfully ✅"}
