# AI-Powered Transcription for SOAP Notes

This project is an AI-powered application that transcribes veterinarian-patient conversations into structured SOAP notes, minimizing manual documentation for mobile veterinary practitioners.

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
│   │   └── index.html         # Main HTML file for the frontend application (optional, not used in this version)
└── README.md                   # Documentation for the project
```

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package manager) installed.
- A virtual environment (`venv`) is recommended for managing dependencies.

---

### Backend Setup

1. **Navigate to the `backend` directory**:
   ```sh
   cd backend
   ```

2. **Set up a virtual environment**:
   ```sh
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```sh
     .\.venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```sh
     source .venv/bin/activate
     ```

4. **Install the required Python packages**:
   ```sh
   pip install -r requirements.txt
   ```

5. **Run the backend application**:
   ```sh
   uvicorn app:app --reload
   ```

   The backend will start, and you can access the Swagger UI at:
   ```
   http://127.0.0.1:8000/docs
   ```

---

### Usage

1. **Open the Swagger UI**:
   Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

2. **Use the `/api/transcribe` endpoint**:
   - Click **Try it out**.
   - Upload an `.mp3` or `.wav` file.
   - Click **Execute**.


### Notes

- **Virtual Environment**: Always activate the virtual environment (`.venv`) before running the backend to ensure the correct dependencies are used.
- **File Formats**: The application currently supports `.mp3` and `.wav` files for transcription.

---

## TODO

### Backend
- [ ] Add error handling for cases where the OpenAI API fails or returns incomplete data.
- [ ] Optimize the `format_to_soap` function to handle edge cases in transcription text.
- [ ] Add unit tests for `speech_to_text.py` and `soap_formatter.py`.

### Frontend
- [ ] Create a working frontend to streamline the system and improve user experience.

### Deployment
- [ ] Make the project accessible online (e.g., deploy the backend and frontend to a cloud hosting service).
- [ ] Replace SQLite with Firebase for a more scalable database solution.
- [ ] Create a hosted website or platform to run the frontend.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.