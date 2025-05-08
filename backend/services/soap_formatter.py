import openai
import logging
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def format_to_soap(transcription: str) -> dict:
    """
    Format the transcribed text into SOAP notes using OpenAI's GPT API.
    
    Args:
        transcription (str): The transcribed text.
        
    Returns:
        dict: A dictionary containing the SOAP notes.
    """
    try:
        # Define the prompt for SOAP note formatting
        prompt = f"""
        You are a helpful assistant that formats transcribed conversations of veterinary visits into SOAP notes.
        These conversations involve a traveling veterinary technician visiting a pet owner's home, inspecting the pet, 
        discussing observations with the owner, and providing an analysis and plan for the pet's care.

        Convert the following transcription into a SOAP note format. Ensure the "Plan" section is included if mentioned.

        Transcription: "{transcription}"

        Format the response as:
        Subjective: ...
        Objective: ...
        Assessment: ...
        Plan: ...
        """

        # Call OpenAI's GPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that formats veterinary visit transcriptions into SOAP notes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extract the formatted SOAP note from the response
        soap_note_text = response["choices"][0]["message"]["content"]
        logger.debug(f"OpenAI SOAP note response: {soap_note_text}")

        # Parse the SOAP note into a dictionary
        soap_note = {}
        for section in ["Subjective", "Objective", "Assessment", "Plan"]:
            start = soap_note_text.find(f"{section}:")
            end = soap_note_text.find("\n", start)
            soap_note[section] = soap_note_text[start + len(section) + 1:end].strip()

        return soap_note
    except Exception as e:
        logger.error(f"Error formatting SOAP note: {e}")
        raise Exception("Failed to format SOAP note.")