"""
Pydantic schemas for API requests/responses
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class StyleEnum(str, Enum):
    """Qo'llanilishi mumkin bo'lgan uslublar"""
    REALISTIC = "realistic"
    ARTISTIC = "artistic"
    CARTOON = "cartoon"
    OIL_PAINTING = "oil-painting"
    WATERCOLOR = "watercolor"
    RENDER_3D = "3d-render"
    PHOTOGRAPHY = "photography"
    CONCEPT_ART = "concept-art"

class ImageGenerationRequest(BaseModel):
    """Image generation request schema"""
    prompt: str = Field(..., min_length=10, max_length=1000, description="Rasm keltirish sarlavhasi")
    style: StyleEnum = Field(default=StyleEnum.REALISTIC, description="Rasm uslubi")
    width: int = Field(default=768, ge=256, le=1024, description="Rasm eni")
    height: int = Field(default=768, ge=256, le=1024, description="Rasm balandligi")
    num_images: int = Field(default=1, ge=1, le=4, description="Yaratilishi kerak bo'lgan rasmlar soni")
    guidance_scale: float = Field(default=7.5, ge=1.0, le=20.0, description="Prompt ta'siri kuchi")
    num_inference_steps: int = Field(default=50, ge=20, le=100, description="Inference bosqichlari")
    quality: str = Field(default="high", description="Sifat darajasi")

class ImageGenerationResponse(BaseModel):
    """Image generation response schema"""
    status: str = Field(..., description="Status")
    task_id: str = Field(..., description="Task identifier")
    images: Optional[List[str]] = Field(None, description="Generated images URLs")
    message: str = Field(..., description="Message")
    generation_time: Optional[float] = None

class VideoGenerationRequest(BaseModel):
    """Video generation request schema"""
    prompt: str = Field(..., min_length=10, max_length=1000, description="Video keltirish sarlavhasi")
    style: StyleEnum = Field(default=StyleEnum.REALISTIC, description="Video uslubi")
    duration: int = Field(default=5, ge=1, le=60, description="Video davomiyligi (soniya)")
    fps: int = Field(default=24, ge=12, le=60, description="Kadr soni (fps)")
    width: int = Field(default=512, ge=256, le=1024, description="Video eni")
    height: int = Field(default=512, ge=256, le=1024, description="Video balandligi")
    quality: str = Field(default="high", description="Sifat darajasi")

class VideoGenerationResponse(BaseModel):
    """Video generation response schema"""
    status: str = Field(..., description="Status")
    task_id: str = Field(..., description="Task identifier")
    video_url: Optional[str] = None
    preview_image: Optional[str] = None
    message: str = Field(..., description="Message")
    generation_time: Optional[float] = None

class TaskStatusResponse(BaseModel):
    """Task status response schema"""
    task_id: str
    status: str
    progress: int
    result: Optional[dict] = None
    error: Optional[str] = None

class HealthCheckResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
