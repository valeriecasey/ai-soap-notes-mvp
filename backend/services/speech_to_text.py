from fastapi import UploadFile
import requests

WHISPER_API_URL = "https://api.openai.com/v1/audio/transcriptions"
API_KEY = "your_openai_api_key"  # Replace with your actual OpenAI API key

def transcribe_audio(file: UploadFile) -> str:
    """
    Transcribe audio file to text using Whisper API.
    
    Args:
        file (UploadFile): The audio file to be transcribed.
        
    Returns:
        str: The transcribed text.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    files = {
        'file': (file.filename, file.file, file.content_type),
        'model': 'whisper-1'  # Specify the model to use
    }
    
    response = requests.post(WHISPER_API_URL, headers=headers, files=files)
    
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        raise Exception(f"Error transcribing audio: {response.text}")