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

## TODO

### Backend
- [ ] Test the `/transcribe` endpoint with various audio files to ensure accurate transcription and SOAP note formatting.
- [ ] Add error handling for cases where the OpenAI API fails or returns incomplete data.
- [ ] Implement logging for debugging and monitoring API usage.
- [ ] Optimize the `format_to_soap` function to handle edge cases in transcription text.
- [ ] Add unit tests for `speech_to_text.py` and `soap_formatter.py`.

### Frontend
- [ ] Set up the React frontend in the `frontend` directory.
- [ ] Create a file upload form to interact with the `/upload/` or `/transcribe` endpoints.
- [ ] Display the generated SOAP notes in a user-friendly format.
- [ ] Add error messages for invalid file uploads or API failures.
- [ ] Style the frontend using Tailwind CSS or another CSS framework.

### Deployment
- [ ] Set up a free-tier hosting service (e.g., Railway.app, Render, or Fly.io) for the backend.
- [ ] Deploy the React frontend to a hosting service like Vercel or Netlify.
- [ ] Configure environment variables securely for production (e.g., OpenAI API key).

### General
- [ ] Write additional documentation for setting up and running the project.
- [ ] Add API usage examples to the `README.md`.
- [ ] Collect feedback from test users and refine the application based on their input.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.