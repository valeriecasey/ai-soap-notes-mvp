from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transcription import router as transcription_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the transcription routes
app.include_router(transcription_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered SOAP Notes API"}