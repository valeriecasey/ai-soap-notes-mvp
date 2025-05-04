import sys
import os
import logging
from fastapi import FastAPI
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

# Health check endpoint
@app.get("/")
async def health_check():
    return {"status": "healthy"}

# Include the transcription router
app.include_router(transcription_router, prefix="/api")