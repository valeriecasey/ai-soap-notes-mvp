import sys
import os
import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.transcription import router as transcription_router
from database.db_setup import init_db

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create the FastAPI app
app = FastAPI()

# Initialize the database
init_db()

# Serve the `frontend` folder as static files
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

# Serve the `index.html` file at the root URL
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("../frontend", "index.html"))

# Include the transcription router
app.include_router(transcription_router, prefix="/api")