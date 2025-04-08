@echo off
cd C:\Users\valer\Documents\ai-soap-notes-mvp\backend
.venv\Scripts\activate
uvicorn app:app --reload --log-level debug