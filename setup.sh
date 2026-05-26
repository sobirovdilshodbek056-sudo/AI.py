#!/bin/bash
# Setup script for AI Media Generator

echo "🚀 AI Media Generator O'rnatishni boshlash..."

# Create virtual environment
echo "📦 Virtual environment yaratilmoqda..."
python -m venv venv

# Activate virtual environment
echo "⚙️ Virtual environment faollashtirilmoqda..."
source venv/bin/activate 2>/dev/null || venv\Scripts\activate

# Install dependencies
echo "📥 Dependencies o'rnatilmoqda..."
pip install --upgrade pip
pip install -r requirements.txt

# Create directories
echo "📁 Direktoriyalar yaratilmoqda..."
mkdir -p outputs/images outputs/videos temp static/uploads

# Download models (optional)
echo "🤖 AI modellar qayta yuklab olinmoqda..."
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
    print('Model avtomatik tarzda kerak bo\'lganda yuklab olinadi.')
"

echo ""
echo "✅ O'rnatish tugadi!"
echo ""
echo "🚀 Serverini ishga tushirish uchun:"
echo "   python main.py"
echo ""
echo "🌐 Web interfacesi:"
echo "   http://localhost:8000"
echo ""
