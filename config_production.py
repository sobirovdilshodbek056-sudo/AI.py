"""
Advanced configuration for production deployment
"""

import os
from pathlib import Path

# Production Settings
class ProductionSettings:
    """Production environment konfiguratsiyasi"""
    
    # API
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    DEBUG = False
    
    # Workers
    WORKERS = int(os.getenv("WORKERS", 4))
    MAX_WORKERS = int(os.getenv("MAX_WORKERS", 8))
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    
    # Cache
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    CACHE_TTL = 3600  # 1 hour
    
    # File storage
    STORAGE_TYPE = os.getenv("STORAGE_TYPE", "local")  # local, s3, etc.
    OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "./outputs"))
    TEMP_DIR = Path(os.getenv("TEMP_DIR", "./temp"))
    
    # Models
    MODEL_CACHE_DIR = os.getenv("MODEL_CACHE_DIR", "/mnt/models")
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
    
    # CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
    
    # Rate limiting
    RATE_LIMIT_ENABLED = True
    RATE_LIMIT_REQUESTS = 100
    RATE_LIMIT_PERIOD = 3600  # 1 hour
    
    # Task settings
    TASK_TIMEOUT = 1800  # 30 minutes
    TASK_RETENTION = 24 * 3600  # 24 hours
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "./logs/app.log")

class DevelopmentSettings:
    """Development environment konfiguratsiyasi"""
    
    API_HOST = "127.0.0.1"
    API_PORT = 8000
    DEBUG = True
    
    WORKERS = 1
    MAX_WORKERS = 2
    
    DATABASE_URL = "sqlite:///./dev.db"
    REDIS_URL = "redis://localhost:6379"
    
    OUTPUT_DIR = Path("./outputs")
    TEMP_DIR = Path("./temp")
    
    MODEL_CACHE_DIR = Path.home() / ".cache" / "huggingface"
    
    SECRET_KEY = "dev-key-change-in-production"
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGINS = ["*"]
    
    RATE_LIMIT_ENABLED = False
    TASK_TIMEOUT = 3600
    TASK_RETENTION = 24 * 3600
    
    LOG_LEVEL = "DEBUG"
    LOG_FILE = "./logs/dev.log"

def get_settings(environment: str = None):
    """O'rni qanday muhitda ishlashni aniqlash"""
    if environment is None:
        environment = os.getenv("ENVIRONMENT", "development")
    
    if environment == "production":
        return ProductionSettings()
    else:
        return DevelopmentSettings()
