"""
Application configuration settings
"""

from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True
    
    # File paths
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    OUTPUT_DIR: Path = Path("outputs")
    TEMP_DIR: Path = Path("temp")
    
    # AI Models
    IMAGE_MODEL: str = "stable-diffusion-v2"
    VIDEO_MODEL: str = "frame-interpolation"
    
    # Generation parameters
    DEFAULT_QUALITY: str = "high"
    MAX_WORKERS: int = 4
    
    # Image settings
    DEFAULT_IMAGE_SIZE: tuple = (768, 768)
    MAX_IMAGE_SIZE: tuple = (1024, 1024)
    
    # Video settings
    DEFAULT_VIDEO_FPS: int = 24
    DEFAULT_VIDEO_DURATION: int = 5
    MAX_VIDEO_DURATION: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
