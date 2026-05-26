"""
Quick start script - Tezkor boshlash
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    print("=" * 50)
    print("🚀 AI Media Generator - Tezkor Boshlash")
    print("=" * 50)
    
    # Create directories
    print("\n📁 Direktoriyalar yaratilmoqda...")
    dirs = ["outputs/images", "outputs/videos", "temp", "static/uploads"]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {dir_path}")
    
    # Check Python version
    print("\n🐍 Python versiyasi tekshirilmoqda...")
    if sys.version_info < (3, 8):
        print("  ✗ Python 3.8 yoki undan yuqori kerak!")
        sys.exit(1)
    print(f"  ✓ Python {sys.version.split()[0]}")
    
    # Check GPU
    print("\n🖥️ GPU tekshirilmoqda...")
    try:
        import torch
        if torch.cuda.is_available():
            print(f"  ✓ GPU mavjud: {torch.cuda.get_device_name(0)}")
            print(f"  ✓ CUDA versiyasi: {torch.version.cuda}")
        else:
            print("  ⚠️ GPU topilmadi, CPU-da ishlaydi")
    except ImportError:
        print("  ⚠️ PyTorch o'rnatilmagan")
    
    # Display instructions
    print("\n" + "=" * 50)
    print("📖 Keying Qadamlar")
    print("=" * 50)
    print("""
1️⃣  Dependencies o'rnatish:
    pip install -r requirements.txt

2️⃣  Serverni ishga tushirish:
    python main.py

3️⃣  Web interfaceni ochish:
    http://localhost:8000

4️⃣  API dokumentatsiyasi:
    http://localhost:8000/docs
    """)
    
    print("\n💡 Maslahlari:")
    print("  - Birinchi marta modellar yuklab olinadi (bir oz vaqt oladi)")
    print("  - GPU bo'lmasa, CPU-da ishlaydi (sekin)")
    print("  - Requirements.txt faylini o'qib chiqing")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
