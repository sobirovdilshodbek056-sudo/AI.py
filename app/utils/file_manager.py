"""
File management utilities
"""

from pathlib import Path
import shutil
import logging

logger = logging.getLogger(__name__)

class FileManager:
    """Fayllar bilan ishlash"""
    
    @staticmethod
    def create_dirs():
        """Zaruriy direktoriyalarni yaratish"""
        dirs = [
            Path("outputs"),
            Path("outputs/images"),
            Path("outputs/videos"),
            Path("temp"),
            Path("static"),
            Path("static/uploads")
        ]
        
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory created/verified: {dir_path}")
    
    @staticmethod
    def cleanup_temp(days: int = 1):
        """Eski fayllarni o'chirish"""
        import time
        
        temp_dir = Path("temp")
        current_time = time.time()
        
        for file_path in temp_dir.glob("*"):
            file_age = current_time - file_path.stat().st_mtime
            if file_age > days * 86400:
                file_path.unlink()
                logger.info(f"Removed old file: {file_path}")
    
    @staticmethod
    def get_file_size(file_path: str) -> str:
        """Fayl o'lchamini insan o'qiy oladigan formatda qaytarish"""
        size = Path(file_path).stat().st_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"
