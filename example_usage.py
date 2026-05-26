"""
Example API usage script
Misol: API-dan foydalanish
"""

import requests
import json
import time
from typing import Optional

API_BASE_URL = "http://localhost:8000"

class AIMediaGenerator:
    """AI Media Generator API client"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
    
    def generate_image(
        self,
        prompt: str,
        style: str = "realistic",
        width: int = 768,
        height: int = 768,
        num_images: int = 1,
        wait: bool = True
    ) -> Optional[dict]:
        """
        Rasm yaratish
        
        Args:
            prompt: Rasm tavsifi
            style: Uslub (realistic, artistic, cartoon, etc.)
            width: Rasm eni
            height: Rasm balandligi
            num_images: Yaratilishi kerak bo'lgan rasmlar soni
            wait: Yaratish tugaguncha kutish
        
        Returns:
            Yaratilgan rasm ma'lumotlari
        """
        payload = {
            "prompt": prompt,
            "style": style,
            "width": width,
            "height": height,
            "num_images": num_images
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/api/image/generate",
                json=payload,
                timeout=600
            )
            response.raise_for_status()
            result = response.json()
            
            if result["status"] == "processing":
                print(f"✓ Task yaratildi: {result['task_id']}")
                
                if wait:
                    return self.wait_for_task(result["task_id"], "image")
                return result
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Xatolik: {e}")
            return None
    
    def generate_video(
        self,
        prompt: str,
        style: str = "realistic",
        duration: int = 5,
        fps: int = 24,
        width: int = 512,
        height: int = 512,
        wait: bool = True
    ) -> Optional[dict]:
        """
        Video yaratish
        
        Args:
            prompt: Video tavsifi
            style: Uslub
            duration: Davomiyligi (soniya)
            fps: Kadr soni
            wait: Yaratish tugaguncha kutish
        
        Returns:
            Yaratilgan video ma'lumotlari
        """
        payload = {
            "prompt": prompt,
            "style": style,
            "duration": duration,
            "fps": fps,
            "width": width,
            "height": height
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/api/video/generate",
                json=payload,
                timeout=1200
            )
            response.raise_for_status()
            result = response.json()
            
            if result["status"] == "processing":
                print(f"✓ Task yaratildi: {result['task_id']}")
                
                if wait:
                    return self.wait_for_task(result["task_id"], "video")
                return result
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Xatolik: {e}")
            return None
    
    def wait_for_task(
        self,
        task_id: str,
        task_type: str,
        check_interval: int = 5
    ) -> Optional[dict]:
        """
        Task-ning tugaguncha kutish
        
        Args:
            task_id: Task ID
            task_type: Task turi (image, video)
            check_interval: Status tekshirish oralig'i (soniya)
        
        Returns:
            Tugallangan task ma'lumotlari
        """
        endpoint = f"/api/{task_type}/status/{task_id}"
        
        while True:
            try:
                response = self.session.get(
                    f"{self.base_url}{endpoint}",
                    timeout=30
                )
                response.raise_for_status()
                result = response.json()
                
                status = result.get("status")
                progress = result.get("progress", 0)
                
                print(f"  Status: {status} ({progress}%)")
                
                if status == "completed":
                    print("✓ Task tugadi!")
                    return result
                elif status == "failed":
                    print(f"✗ Xatolik: {result.get('error')}")
                    return None
                
                time.sleep(check_interval)
                
            except requests.exceptions.RequestException as e:
                print(f"✗ Status tekshirishda xatolik: {e}")
                return None
    
    def get_models(self) -> Optional[dict]:
        """Mavjud modellarni olish"""
        try:
            response = self.session.get(f"{self.base_url}/api/models")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"✗ Xatolik: {e}")
            return None
    
    def health_check(self) -> bool:
        """Serverning holati tekshirish"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            response.raise_for_status()
            print("✓ Server faol")
            return True
        except requests.exceptions.RequestException:
            print("✗ Server faol emas")
            return False


def main():
    """Misol foydalanish"""
    print("=" * 50)
    print("AI Media Generator - API Client")
    print("=" * 50)
    
    # Initialize client
    client = AIMediaGenerator()
    
    # Check server health
    print("\n🔍 Server tekshirilmoqda...")
    if not client.health_check():
        print("Serverini ishga tushirib ko'ring: python main.py")
        return
    
    # Get available models
    print("\n📋 Mavjud modellar:")
    models = client.get_models()
    if models:
        print(json.dumps(models, indent=2))
    
    # Generate image example
    print("\n" + "=" * 50)
    print("🖼️ Rasm yaratil moqda...")
    print("=" * 50)
    
    image_result = client.generate_image(
        prompt="A serene landscape with mountains and a river during sunset, realistic style, high quality",
        style="photography",
        width=768,
        height=768,
        wait=True
    )
    
    if image_result:
        print(f"\n✓ Rasm tayyor!")
        if image_result.get("images"):
            print(f"Rasm: {image_result['images'][0]}")
    
    # Generate video example
    print("\n" + "=" * 50)
    print("🎥 Video yaratil moqda...")
    print("=" * 50)
    
    video_result = client.generate_video(
        prompt="A spacecraft flying through a field of asteroids, cinematic style",
        style="realistic",
        duration=3,
        fps=24,
        wait=True
    )
    
    if video_result:
        print(f"\n✓ Video tayyor!")
        if video_result.get("video"):
            print(f"Video: {video_result['video']}")


if __name__ == "__main__":
    main()
