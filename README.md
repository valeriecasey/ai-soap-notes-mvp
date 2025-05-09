# Transcription for SOAP Notes

This project is an application that transcribes veterinarian-patient conversations into structured SOAP notes, minimizing manual documentation.

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
│   └── index.html             # Main HTML file for the frontend application
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

   The backend will start, and you can access the application at:
   ```
   http://127.0.0.1:8000/
   ```

---

### Usage

1. **Open the Application**:
   Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

2. **Upload an Audio File**:
   - Click the "Browse" button to select an `.mp3` or `.wav` file.
   - Click the "Upload Audio File" button to process the file.

3. **View Results**:
   - The transcription will appear in the first text box.
   - The SOAP-formatted notes will appear in the second text box.

4. **Download Results**:
   - Use the "Download Transcription" and "Download SOAP Format" links to save the results as `.txt` files.

---

### Notes

- **Virtual Environment**: Always activate the virtual environment (`.venv`) before running the backend to ensure the correct dependencies are used.
- **File Formats**: The application currently supports `.mp3` and `.wav` files for transcription.
- **OpenAI Version**: When running the application, OpenAI 0.28.0 is used. If the transcription fails, please check the OpenAI API version and update it if necessary.

---

## TODO

### Deployment
- [ ] Replace the local SQLite database with an online database for scalability and ease of use.
- [ ] Allow other devices to access the application via a public URL.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
