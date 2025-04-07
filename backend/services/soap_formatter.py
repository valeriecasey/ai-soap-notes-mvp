import openai

def format_to_soap(transcription: str) -> dict:
    """
    Format the transcription into SOAP notes.

    Args:
        transcription (str): The raw transcription text.

    Returns:
        dict: A dictionary containing the SOAP notes.
    """
    prompt = f"""
    Format the following transcription into SOAP notes:
    Transcription: {transcription}

    Return the SOAP notes in this structure:
    - Subjective:
    - Objective:
    - Assessment:
    - Plan:
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response["choices"][0]["text"].strip()