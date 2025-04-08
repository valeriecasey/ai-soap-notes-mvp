import openai
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def format_to_soap(transcription: str) -> dict:
    """
    Format the transcription into SOAP notes.

    Args:
        transcription (str): The raw transcription text.

    Returns:
        dict: A dictionary containing the SOAP notes.
    """
    try:
        logger.debug(f"Formatting transcription to SOAP: {transcription}")
        # Example SOAP note formatting logic
        soap_note = {
            "Subjective": transcription[:50],  # Placeholder logic
            "Objective": transcription[50:100],  # Placeholder logic
            "Assessment": transcription[100:150],  # Placeholder logic
            "Plan": transcription[150:]  # Placeholder logic
        }
        logger.debug(f"Generated SOAP note: {soap_note}")
        return soap_note
    except Exception as e:
        logger.error(f"Error in format_to_soap: {e}")
        raise Exception("Failed to format transcription into SOAP notes.")