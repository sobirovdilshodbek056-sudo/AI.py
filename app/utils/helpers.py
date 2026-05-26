"""
Configuration utilities and helpers
"""

import os
from pathlib import Path
from typing import Dict, Any

class ConfigHelper:
    """Konfiguratsiyaga yordam beruvchi sinf"""
    
    @staticmethod
    def get_device():
        """GPU yoki CPU-ni aniqlash"""
        try:
            import torch
            return "cuda" if torch.cuda.is_available() else "cpu"
        except ImportError:
            return "cpu"
    
    @staticmethod
    def get_memory_info() -> Dict[str, Any]:
        """Xotira ma'lumotlarini olish"""
        import psutil
        
        memory = psutil.virtual_memory()
        return {
            "total_gb": memory.total / (1024**3),
            "available_gb": memory.available / (1024**3),
            "percent": memory.percent
        }
    
    @staticmethod
    def get_gpu_memory_info() -> Dict[str, Any]:
        """GPU xotira ma'lumotlarini olish"""
        try:
            import torch
            if torch.cuda.is_available():
                return {
                    "device_name": torch.cuda.get_device_name(0),
                    "total_gb": torch.cuda.get_device_properties(0).total_memory / (1024**3),
                    "allocated_gb": torch.cuda.memory_allocated(0) / (1024**3),
                    "cached_gb": torch.cuda.memory_reserved(0) / (1024**3)
                }
        except:
            pass
        return {}
    
    @staticmethod
    def validate_environment():
        """Muhitni tekshirish"""
        checks = {
            "python": False,
            "pytorch": False,
            "transformers": False,
            "cuda": False
        }
        
        import sys
        checks["python"] = sys.version_info >= (3, 8)
        
        try:
            import torch
            checks["pytorch"] = True
            checks["cuda"] = torch.cuda.is_available()
        except ImportError:
            pass
        
        try:
            import transformers
            checks["transformers"] = True
        except ImportError:
            pass
        
        return checks

class PromptOptimizer:
    """Prompt-larni optimallashtirish"""
    
    QUALITY_ENHANCERS = {
        "detailed": "extremely detailed, intricate",
        "quality": "high quality, masterpiece, 4k, 8k",
        "lighting": "cinematic lighting, dramatic lighting",
        "style": "professional, artistic"
    }
    
    @staticmethod
    def enhance_prompt(prompt: str, **kwargs) -> str:
        """
        Prompt-ni yaxshilash va kengaytirish
        
        Args:
            prompt: Asl prompt
            **kwargs: Qo'shimcha parametrlar
        
        Returns:
            Kengaytirilgan prompt
        """
        enhanced = prompt
        
        # Add quality enhancers
        if kwargs.get("high_quality"):
            enhanced += f", {PromptOptimizer.QUALITY_ENHANCERS['quality']}"
        
        if kwargs.get("detailed"):
            enhanced += f", {PromptOptimizer.QUALITY_ENHANCERS['detailed']}"
        
        if kwargs.get("cinematic"):
            enhanced += f", {PromptOptimizer.QUALITY_ENHANCERS['lighting']}"
        
        return enhanced
    
    @staticmethod
    def add_negative_prompt(prompt: str) -> str:
        """
        Salbiy prompt qo'shish (nima kerak emas)
        """
        negative_terms = [
            "ugly",
            "distorted",
            "blurry",
            "low quality",
            "watermark",
            "text",
            "logo"
        ]
        return ", ".join(negative_terms)
