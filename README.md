# AI-Powered Transcription for SOAP Notes

This project aims to develop an AI application that transcribes veterinarian-patient conversations into structured SOAP notes, minimizing manual documentation for mobile veterinary practitioners.

## Project Structure

```
ai-soap-notes-mvp
├── backend
│   ├── app.py                # Entry point for the backend application
│   ├── routes
│   │   └── transcription.py   # Routes for handling transcription requests
│   ├── services
│   │   ├── speech_to_text.py  # Functions for speech-to-text conversion
│   │   └── soap_formatter.py   # Functions for formatting transcriptions into SOAP notes
│   ├── models
│   │   └── note.py            # Data model for SOAP notes
│   ├── database
│   │   └── db_setup.py        # Database setup and connection logic
│   └── requirements.txt       # Python dependencies for the backend
├── frontend
│   ├── public
│   │   └── index.html         # Main HTML file for the frontend application
│   ├── src
│   │   ├── components
│   │   │   ├── FileUpload.js   # Component for uploading audio files
│   │   │   └── NoteDisplay.js   # Component for displaying SOAP notes
│   │   ├── App.js              # Main component of the React application
│   │   └── index.js            # Entry point for the React application
│   └── package.json            # Configuration file for the frontend application
└── README.md                   # Documentation for the project
```

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the backend application:
   ```
   uvicorn app:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required Node.js packages:
   ```
   npm install
   ```
3. Start the frontend application:
   ```
   npm start
   ```

## Usage

1. Upload audio files through the frontend interface.
2. The application will process the audio and generate SOAP notes.
3. View the formatted SOAP notes in the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.