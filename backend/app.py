from fastapi import FastAPI
from routes.transcription import router as transcription_router

app = FastAPI()

# Include the transcription routes
app.include_router(transcription_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI SOAP Notes API"}