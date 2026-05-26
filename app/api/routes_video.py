"""
Video generation API routes
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
import logging
import uuid
from datetime import datetime

from app.models.schemas import VideoGenerationRequest, VideoGenerationResponse
from app.services.video_generator import VideoGenerator
from app.utils.cache import TaskCache

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize video generator
video_generator = VideoGenerator()
task_cache = TaskCache()

@router.post("/generate", response_model=VideoGenerationResponse)
async def generate_video(
    request: VideoGenerationRequest,
    background_tasks: BackgroundTasks
):
    """
    Video yaratuvchi endpoint
    
    Parameters:
    - prompt: Video tavsifi
    - style: Uslub
    - duration: Davomiyligi (soniya)
    - fps: Kadr soni
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
            video_generator.generate,
            task_id=task_id,
            prompt=request.prompt,
            style=request.style.value,
            duration=request.duration,
            fps=request.fps,
            width=request.width,
            height=request.height
        )
        
        logger.info(f"Video generation task started: {task_id}")
        
        return VideoGenerationResponse(
            status="processing",
            task_id=task_id,
            message="Video yaratish boshlandi. Kutib turing..."
        )
    
    except Exception as e:
        logger.error(f"Error in video generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{task_id}")
async def get_video_status(task_id: str):
    """
    Video yaratish STATUS-ini olish
    """
    try:
        task = task_cache.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task topilmadi")
        
        return {
            "task_id": task_id,
            "status": task.get("status"),
            "progress": task.get("progress", 0),
            "video": task.get("video"),
            "preview": task.get("preview"),
            "created_at": task.get("created_at"),
            "completed_at": task.get("completed_at")
        }
    
    except Exception as e:
        logger.error(f"Error getting task status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_models():
    """Mavjud video modellarini qaytaradi"""
    return {
        "models": [
            {
                "name": "Frame Interpolation",
                "id": "frame-interpolation",
                "description": "Smooth video synthesis"
            },
            {
                "name": "Video Synthesis",
                "id": "video-synthesis",
                "description": "Advanced video generation"
            }
        ]
    }

@router.get("/templates")
async def get_templates():
    """Video shablonlarini qaytaradi"""
    return {
        "templates": [
            {
                "name": "Intro",
                "duration": 3,
                "description": "Video kiruvchi animatsiyasi"
            },
            {
                "name": "Explainer",
                "duration": 10,
                "description": "Tushuntiruvchi video"
            },
            {
                "name": "Promo",
                "duration": 15,
                "description": "Reklama video"
            }
        ]
    }
