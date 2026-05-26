@echo off
REM Setup script for AI Media Generator (Windows)

echo 🚀 AI Media Generator O'rnatishni boshlash...
echo.

REM Create virtual environment
echo 📦 Virtual environment yaratilmoqda...
python -m venv venv

REM Activate virtual environment
echo ⚙️ Virtual environment faollashtirilmoqda...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Dependencies o'rnatilmoqda...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create directories
echo 📁 Direktoriyalar yaratilmoqda...
if not exist outputs mkdir outputs
if not exist outputs\images mkdir outputs\images
if not exist outputs\videos mkdir outputs\videos
if not exist temp mkdir temp
if not exist static\uploads mkdir static\uploads

REM Download models (optional)
echo 🤖 AI modellar qayta yuklab olinmoqda...
python -c "
try:
    from diffusers import StableDiffusionPipeline
    import torch
    print('Modeli yuklab olinmoqda (birinchi marta, bu bir oz vaqt oladi)...')
    model_id = 'runwayml/stable-diffusion-v1-5'
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    print('✓ Model muvaffaqiyatli yuklab olindi!')
except Exception as e:
    print(f'⚠️ Model yuklanmadi: {e}')
    print('Model avtomatik tarzda kerak bo''lganda yuklab olinadi.')
"

echo.
echo ✅ O'rnatish tugadi!
echo.
echo 🚀 Serverini ishga tushirish uchun:
echo    python main.py
echo.
echo 🌐 Web interfacesi:
echo    http://localhost:8000
echo.
pause
