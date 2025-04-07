from fastapi import UploadFile
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

WHISPER_API_URL = "https://api.openai.com/v1/audio/transcriptions"
API_KEY = "your_openai_api_key"  # Replace with your actual OpenAI API key

print(f"API Key: {openai.api_key}")  # This should print your API key

async def transcribe_audio(file: UploadFile) -> str:
    """
    Transcribe audio file to text using Whisper API.
    
    Args:
        file (UploadFile): The audio file to be transcribed.
        
    Returns:
        str: The transcribed text.
    """
    # Save the uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(await file.read())

    # Use OpenAI Whisper API for transcription
    with open(temp_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)

    # Clean up the temporary file
    os.remove(temp_file_path)

    return response["text"]