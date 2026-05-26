"""
Configuration variables for the application
"""

import os
from typing import Dict, List

# Model configurations
MODELS_CONFIG: Dict[str, Dict] = {
    "image": {
        "stable-diffusion-v1-5": {
            "name": "Stable Diffusion v1.5",
            "description": "General purpose image generation",
            "model_id": "runwayml/stable-diffusion-v1-5",
            "memory_required": "10GB"
        },
        "stable-diffusion-v2": {
            "name": "Stable Diffusion v2",
            "description": "Improved image generation",
            "model_id": "stabilityai/stable-diffusion-2-1",
            "memory_required": "15GB"
        }
    },
    "video": {
        "frame-interpolation": {
            "name": "Frame Interpolation",
            "description": "Smooth video synthesis",
            "memory_required": "12GB"
        }
    }
}

# Styles configuration
STYLES: Dict[str, str] = {
    "realistic": "Realistic and photographic",
    "artistic": "Artistic and stylized",
    "cartoon": "Cartoon style",
    "oil-painting": "Oil painting style",
    "watercolor": "Watercolor painting",
    "3d-render": "3D rendered",
    "photography": "Professional photography",
    "concept-art": "Concept art"
}

# Generation presets
PRESETS: Dict[str, Dict] = {
    "fast": {
        "steps": 20,
        "guidance_scale": 7.5,
        "quality": "standard"
    },
    "balanced": {
        "steps": 50,
        "guidance_scale": 7.5,
        "quality": "high"
    },
    "quality": {
        "steps": 100,
        "guidance_scale": 8.0,
        "quality": "ultra"
    }
}

# Video presets
VIDEO_PRESETS: Dict[str, Dict] = {
    "short_clip": {
        "duration": 3,
        "fps": 24,
        "resolution": (512, 512)
    },
    "standard": {
        "duration": 5,
        "fps": 24,
        "resolution": (512, 512)
    },
    "cinematic": {
        "duration": 10,
        "fps": 30,
        "resolution": (1024, 576)
    }
}

# Prompt enhancement templates
PROMPT_TEMPLATES: Dict[str, str] = {
    "photography": "Professional photography, high quality, detailed, masterpiece, 4k, cinematic lighting",
    "concept_art": "Concept art, illustration, artstation, highly detailed, digital painting",
    "scifi": "Sci-fi, futuristic, high tech, neon, cyberpunk, detailed, 4k",
    "fantasy": "Fantasy art, magical, detailed, intricate, epic, dramatic lighting",
    "nature": "Nature photography, landscape, beautiful, serene, high quality, detailed"
}
