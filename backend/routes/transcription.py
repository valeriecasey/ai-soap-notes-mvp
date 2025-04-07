from fastapi import APIRouter, UploadFile, File, HTTPException
from services.speech_to_text import transcribe_audio
from services.soap_formatter import format_to_soap

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith(('.mp3', '.wav')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only MP3 and WAV files are accepted.")
    
    try:
        # Transcribe the audio file
        transcription = await transcribe_audio(file)
        
        # Format the transcription into SOAP notes
        soap_note = format_to_soap(transcription)
        
        return {"soap_note": soap_note}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploaded_files/{file.filename}", "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename}