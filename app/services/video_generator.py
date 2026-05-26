"""
Video generation service
"""

import logging
import torch
from pathlib import Path
from datetime import datetime
import time
import numpy as np
import cv2
from PIL import Image

logger = logging.getLogger(__name__)

class VideoGenerator:
    """AI asosida video yaratuvchi"""
    
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"VideoGenerator initialized on device: {self.device}")
        self.output_dir = Path("outputs/videos")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def generate(
        self,
        task_id: str,
        prompt: str,
        style: str = "realistic",
        duration: int = 5,
        fps: int = 24,
        width: int = 512,
        height: int = 512
    ):
        """
        Video yaratish
        """
        try:
            from app.utils.cache import TaskCache
            from diffusers import StableDiffusionPipeline
            
            logger.info(f"Starting video generation for task {task_id}")
            start_time = time.time()
            
            task_cache = TaskCache()
            
            # Generate frames
            task_cache.set_task(task_id, {
                "status": "generating_frames",
                "progress": 10
            })
            
            num_frames = duration * fps
            frames = []
            
            # Load model
            model_id = "runwayml/stable-diffusion-v1-5"
            pipe = StableDiffusionPipeline.from_pretrained(model_id)
            pipe = pipe.to(self.device)
            
            enhanced_prompt = f"{prompt}, {style} style, cinematic, 4k"
            
            # Generate frames with slight variations
            for frame_idx in range(num_frames):
                task_cache.set_task(task_id, {
                    "status": "generating_frames",
                    "progress": 10 + (70 * frame_idx // num_frames)
                })
                
                # Add slight variation to prompt for each frame
                frame_prompt = f"{enhanced_prompt} frame {frame_idx + 1}"
                
                with torch.no_grad():
                    image = pipe(
                        frame_prompt,
                        num_inference_steps=30,
                        guidance_scale=7.5,
                        height=height,
                        width=width
                    ).images[0]
                
                # Convert PIL to numpy
                frame_array = np.array(image)
                frames.append(frame_array)
                
                logger.info(f"Frame {frame_idx + 1}/{num_frames} generated")
            
            # Compose video
            task_cache.set_task(task_id, {
                "status": "composing_video",
                "progress": 80
            })
            
            video_path = self.output_dir / f"{task_id}.mp4"
            self._compose_video(frames, str(video_path), fps, width, height)
            
            # Create preview image (first frame)
            preview_path = self.output_dir / f"{task_id}_preview.png"
            Image.fromarray(frames[0]).save(preview_path)
            
            # Update task cache
            generation_time = time.time() - start_time
            task_cache.set_task(task_id, {
                "status": "completed",
                "progress": 100,
                "video": str(video_path),
                "preview": str(preview_path),
                "completed_at": datetime.now().isoformat(),
                "generation_time": generation_time
            })
            
            logger.info(f"Video generation completed for task {task_id} in {generation_time:.2f}s")
        
        except Exception as e:
            logger.error(f"Error in video generation: {str(e)}")
            from app.utils.cache import TaskCache
            task_cache = TaskCache()
            task_cache.set_task(task_id, {
                "status": "failed",
                "error": str(e)
            })
    
    def _compose_video(
        self,
        frames: list,
        output_path: str,
        fps: int,
        width: int,
        height: int
    ):
        """
        Kadrlardan video qo'shish
        """
        try:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            for frame in frames:
                # Convert RGB to BGR for OpenCV
                if len(frame.shape) == 3 and frame.shape[2] == 3:
                    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                else:
                    frame_bgr = frame
                
                out.write(frame_bgr)
            
            out.release()
            logger.info(f"Video saved: {output_path}")
        
        except Exception as e:
            logger.error(f"Error composing video: {str(e)}")
            raise
    
    async def add_background_music(
        self,
        video_path: str,
        audio_path: str
    ) -> str:
        """
        Videoga fon musiqa qo'shish
        """
        try:
            import subprocess
            
            output_path = Path(video_path).parent / f"with_audio_{Path(video_path).stem}.mp4"
            
            cmd = [
                "ffmpeg",
                "-i", video_path,
                "-i", audio_path,
                "-c:v", "copy",
                "-c:a", "aac",
                "-strict", "experimental",
                str(output_path)
            ]
            
            subprocess.run(cmd, check=True)
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Error adding audio: {str(e)}")
            raise
