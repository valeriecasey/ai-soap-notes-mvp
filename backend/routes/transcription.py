from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from services.speech_to_text import transcribe_audio
from services.soap_formatter import format_to_soap
from database.db_setup import get_db
from models.note import SOAPNote as SOAPNoteModel
from sqlalchemy.orm import Session
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(('.mp3', '.wav')):
        logger.error(f"Invalid file type: {file.filename}")
        raise HTTPException(status_code=400, detail="Invalid file type. Only MP3 and WAV files are accepted.")
    
    try:
        # Log file upload
        logger.info(f"Received file: {file.filename}")
        
        # Transcribe the audio file
        transcription = await transcribe_audio(file)
        logger.debug(f"Transcription result: {transcription}")
        
        # Format the transcription into SOAP notes
        soap_note = format_to_soap(transcription)
        logger.debug(f"SOAP note generated: {soap_note}")
        
        # Save SOAP notes to the database
        db_note = SOAPNoteModel(
            subjective=soap_note["Subjective"],
            objective=soap_note["Objective"],
            assessment=soap_note["Assessment"],
            plan=soap_note["Plan"]
        )
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        logger.info(f"SOAP note saved to database with ID: {db_note.id}")
        
        return {"soap_note": soap_note}
    except Exception as e:
        logger.error(f"Error in /transcribe endpoint: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the file.")

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploaded_files/{file.filename}", "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename}

# The JavaScript code has been removed. Place it in a separate `.js` file.

from fastapi import FastAPI
from routes.transcription import router as transcription_router

app = FastAPI()

# Include the transcription router
app.include_router(transcription_router, prefix="/api")