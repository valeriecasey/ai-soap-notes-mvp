import openai
import os
import logging
from fastapi import UploadFile
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

async def transcribe_audio(file: UploadFile) -> str:
    """
    Transcribe audio file to text using OpenAI's Whisper API (newer version for openai>=1.0.0).
    
    Args:
        file (UploadFile): The audio file to be transcribed.
        
    Returns:
        str: The transcribed text.
    """
    try:
        # Save the uploaded file temporarily
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())
        logger.info(f"File saved temporarily at: {temp_file_path}")

        # Transcribe the audio file using OpenAI's Whisper API
        with open(temp_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",  # Specify the Whisper model
                file=audio_file
            )
        logger.debug(f"OpenAI transcription response: {response}")

        # Remove the temporary file
        os.remove(temp_file_path)
        logger.info(f"Temporary file removed: {temp_file_path}")

        return response["text"]
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
        raise Exception("Failed to transcribe audio file.")