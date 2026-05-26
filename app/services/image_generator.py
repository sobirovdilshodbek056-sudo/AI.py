"""
Image generation service using AI models
"""

import logging
import torch
from pathlib import Path
from datetime import datetime
import time
from PIL import Image
import io

logger = logging.getLogger(__name__)

class ImageGenerator:
    """AI asosida rasm yaratuvchi"""
    
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"ImageGenerator initialized on device: {self.device}")
        self.output_dir = Path("outputs/images")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def generate(
        self,
        task_id: str,
        prompt: str,
        style: str = "realistic",
        width: int = 768,
        height: int = 768,
        num_images: int = 1,
        guidance_scale: float = 7.5,
        num_inference_steps: int = 50
    ):
        """
        Rasm yaratish
        """
        try:
            # Import here to avoid loading large models at startup
            from diffusers import StableDiffusionPipeline
            from app.utils.cache import TaskCache
            
            logger.info(f"Starting image generation for task {task_id}")
            start_time = time.time()
            
            task_cache = TaskCache()
            
            # Load model
            task_cache.set_task(task_id, {
                "status": "loading_model",
                "progress": 10
            })
            
            model_id = "runwayml/stable-diffusion-v1-5"
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                use_safetensors=True
            )
            pipe = pipe.to(self.device)
            
            # Enhance prompt with style
            enhanced_prompt = f"{prompt}, {style} style, high quality, detailed, masterpiece"
            
            # Generate images
            images = []
            for i in range(num_images):
                task_cache.set_task(task_id, {
                    "status": "generating",
                    "progress": 10 + (60 * (i + 1) // num_images)
                })
                
                with torch.no_grad():
                    image = pipe(
                        enhanced_prompt,
                        num_inference_steps=num_inference_steps,
                        guidance_scale=guidance_scale,
                        height=height,
                        width=width
                    ).images[0]
                
                # Save image
                image_path = self.output_dir / f"{task_id}_{i}.png"
                image.save(image_path)
                images.append(str(image_path))
                
                logger.info(f"Image {i+1}/{num_images} saved: {image_path}")
            
            # Update task cache
            generation_time = time.time() - start_time
            task_cache.set_task(task_id, {
                "status": "completed",
                "progress": 100,
                "images": images,
                "completed_at": datetime.now().isoformat(),
                "generation_time": generation_time
            })
            
            logger.info(f"Image generation completed for task {task_id} in {generation_time:.2f}s")
        
        except Exception as e:
            logger.error(f"Error in image generation: {str(e)}")
            from app.utils.cache import TaskCache
            task_cache = TaskCache()
            task_cache.set_task(task_id, {
                "status": "failed",
                "error": str(e)
            })

    async def enhance_image(
        self,
        image_path: str,
        enhancement_type: str = "upscale"
    ) -> str:
        """
        Rasmni yaxshilash (upscale, denoise, etc.)
        """
        try:
            # Load image
            image = Image.open(image_path)
            
            # Apply enhancement based on type
            if enhancement_type == "upscale":
                # 2x upscale
                new_size = (image.width * 2, image.height * 2)
                image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save enhanced image
            output_path = Path(image_path).parent / f"enhanced_{Path(image_path).stem}.png"
            image.save(output_path)
            
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Error enhancing image: {str(e)}")
            raise
