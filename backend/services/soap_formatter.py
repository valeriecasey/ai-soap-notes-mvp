def format_soap_note(transcription):
    """
    Formats the transcribed text into the SOAP note structure.

    Args:
        transcription (str): The raw transcription text.

    Returns:
        dict: A dictionary containing the formatted SOAP note with keys 'Subjective', 'Objective', 'Assessment', and 'Plan'.
    """
    # Placeholder for the SOAP note structure
    soap_note = {
        "Subjective": "",
        "Objective": "",
        "Assessment": "",
        "Plan": ""
    }

    # Simple logic to split the transcription into sections
    # This can be enhanced with more sophisticated NLP techniques
    sections = transcription.split("\n\n")  # Assuming sections are separated by double newlines

    if len(sections) > 0:
        soap_note["Subjective"] = sections[0].strip()
    if len(sections) > 1:
        soap_note["Objective"] = sections[1].strip()
    if len(sections) > 2:
        soap_note["Assessment"] = sections[2].strip()
    if len(sections) > 3:
        soap_note["Plan"] = sections[3].strip()

    return soap_note