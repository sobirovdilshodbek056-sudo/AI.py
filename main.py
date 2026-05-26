"""
AI Video & Image Generation Application
Zamonavoy dezaynga ega AI rasm va video generator
"""

from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import logging

from app.core.config import settings
from app.api import routes_image, routes_video
from app.utils.file_manager import FileManager

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Media Generator",
    description="Sun'iy intellekt asosida rasm va video yaratuvchi dastur",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create necessary directories
FileManager.create_dirs()

# Mount static files
if Path("static").exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API routers
app.include_router(routes_image.router, prefix="/api/image", tags=["Image Generation"])
app.include_router(routes_video.router, prefix="/api/video", tags=["Video Generation"])

@app.get("/")
async def root():
    """Asosiy page"""
    return {
        "name": "AI Media Generator",
        "version": "1.0.0",
        "description": "Sun'iy intellekt asosida rasm va video yaratuvchi",
        "endpoints": {
            "image_generation": "/api/image/generate",
            "video_generation": "/api/video/generate",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

@app.get("/api/models")
async def get_available_models():
    """Mavjud AI modellarni qaytaradi"""
    return {
        "image_models": [
            "stable-diffusion-v2",
            "stable-diffusion-xl",
            "openjourney"
        ],
        "video_models": [
            "frame-interpolation",
            "video-synthesis"
        ],
        "styles": [
            "realistic",
            "artistic",
            "cartoon",
            "oil-painting",
            "watercolor",
            "3d-render",
            "photography",
            "concept-art"
        ]
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Global exception: {str(exc)}")
    return {
        "error": "Xatolik yuz berdi",
        "message": str(exc)
    }

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "10000"))  # Render default port
    debug_mode = os.getenv("DEBUG", "False") == "True"
    
    logger.info(f"Starting server on {host}:{port}")
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=debug_mode
    )
