"""
Image generation API routes
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from typing import List
import logging
import uuid
from datetime import datetime

from app.models.schemas import ImageGenerationRequest, ImageGenerationResponse
from app.services.image_generator import ImageGenerator
from app.utils.cache import TaskCache

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize image generator
image_generator = ImageGenerator()
task_cache = TaskCache()

@router.post("/generate", response_model=ImageGenerationResponse)
async def generate_image(
    request: ImageGenerationRequest,
    background_tasks: BackgroundTasks
):
    """
    Rasm yaratuvchi endpoint
    
    Parameters:
    - prompt: Rasm tavsifi
    - style: Uslub (realistic, artistic, cartoon, etc.)
    - width: Rasm eni
    - height: Rasm balandligi
    - num_images: Yaratilishi kerak bo'lgan rasmlar soni
    """
    try:
        task_id = str(uuid.uuid4())
        
        # Store task in cache
        task_cache.set_task(task_id, {
            "status": "processing",
            "progress": 0,
            "created_at": datetime.now().isoformat()
        })
        
        # Add background task
        background_tasks.add_task(
            image_generator.generate,
            task_id=task_id,
            prompt=request.prompt,
            style=request.style.value,
            width=request.width,
            height=request.height,
            num_images=request.num_images,
            guidance_scale=request.guidance_scale,
            num_inference_steps=request.num_inference_steps
        )
        
        logger.info(f"Image generation task started: {task_id}")
        
        return ImageGenerationResponse(
            status="processing",
            task_id=task_id,
            message="Rasm yaratish boshlandi. Kutib turing..."
        )
    
    except Exception as e:
        logger.error(f"Error in image generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{task_id}")
async def get_image_status(task_id: str):
    """
    Rasm yaratish STATUS-ini olish
    """
    try:
        task = task_cache.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task topilmadi")
        
        return {
            "task_id": task_id,
            "status": task.get("status"),
            "progress": task.get("progress", 0),
            "images": task.get("images"),
            "created_at": task.get("created_at"),
            "completed_at": task.get("completed_at")
        }
    
    except Exception as e:
        logger.error(f"Error getting task status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_models():
    """Mavjud rasm modellarini qaytaradi"""
    return {
        "models": [
            {
                "name": "Stable Diffusion v2",
                "id": "stable-diffusion-v2",
                "description": "Zamonavoy va precise rasm generatsiyasi"
            },
            {
                "name": "Stable Diffusion XL",
                "id": "stable-diffusion-xl",
                "description": "Yuqori sifatli, batafsil rasmlar"
            },
            {
                "name": "OpenJourney",
                "id": "openjourney",
                "description": "Sanat uslubiga mos rasmlar"
            }
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

@router.get("/examples")
async def get_examples():
    """Misol rasmlarini qaytaradi"""
    return {
        "examples": [
            {
                "title": "Futuristik shahar",
                "prompt": "A futuristic city with neon lights at night, high quality digital art"
            },
            {
                "title": "Tabiat",
                "prompt": "A beautiful mountain landscape with a river flowing through it, sunset"
            },
            {
                "title": "Portre",
                "prompt": "Portrait of a woman with detailed features, professional lighting"
            }
        ]
    }
