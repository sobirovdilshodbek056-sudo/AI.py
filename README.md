# AI Media Generator 🎬

Sun'iy intellekt asosida professional rasm va video yaratuvchi dastur.

## Xususiyatlari ✨

- 🖼️ **AI Rasm Generatsiyasi** - Lotin va o'zbek tilidagi prompts
- 🎥 **AI Video Yaratish** - Cinematic va professional videolar
- 🎨 **Ko'p Uslublar** - Realistic, Artistic, Cartoon, Oil Painting, va boshqalar
- ⚡ **Tezkor Yaratish** - Optimized GPU processing
- 💾 **Yuqori Sifat** - Hangamani sifat bilan yaratish

## Talablar 📋

```bash
Python 3.8+
CUDA 11.8+ (NVIDIA GPU uchun)
30GB bo'sh disk (modellar uchun)
```

## O'rnatish 🚀

### 1. Repository-ni klonlash
```bash
cd "AI video yaratish uchun dastur"
```

### 2. Virtual Environment yaratish
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Dependencies o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Server ishga tushirish
```bash
python main.py
```

Server `http://localhost:8000` da ishga tushuriladi.

### 5. Web interfaceni ochish
```
http://localhost:8000/static/index.html
```

Yoki `index.html` faylini brauzerda to'g'ridan-to'g'ri oching.

## API Endpoints 🔌

### Rasm Yaratish
```bash
POST /api/image/generate
Content-Type: application/json

{
    "prompt": "Rasmning tavsifi",
    "style": "realistic",
    "width": 768,
    "height": 768,
    "num_images": 1,
    "num_inference_steps": 50
}
```

### Video Yaratish
```bash
POST /api/video/generate
Content-Type: application/json

{
    "prompt": "Video-ning tavsifi",
    "style": "realistic",
    "duration": 5,
    "fps": 24,
    "width": 512,
    "height": 512
}
```

### Status Tekshirish
```bash
GET /api/image/status/{task_id}
GET /api/video/status/{task_id}
```

## Prompt Yozish Maslahlari 💡

YAXSHI PROMPTS:
- "High quality, detailed, masterpiece: A futuristic city with neon lights at night"
- "Professional photography of a serene forest with morning mist"
- "Cinematic 4K video of a space exploration scene"

YOMON PROMPTS:
- "Cool stuff"
- "Make something nice"
- "Video"

## Direktoriya Struktura 📁

```
AI video yaratish uchun dastur/
├── main.py                 # Asosiy aplikatsiya
├── requirements.txt        # Python dependencies
├── index.html             # Web interfacesi
├── .env                   # Environment social
├── app/
│   ├── core/
│   │   └── config.py      # Konfiguratsiyalar
│   ├── api/
│   │   ├── routes_image.py
│   │   └── routes_video.py
│   ├── services/
│   │   ├── image_generator.py
│   │   └── video_generator.py
│   ├── models/
│   │   └── schemas.py
│   └── utils/
│       ├── cache.py
│       └── file_manager.py
├── outputs/               # Yaratilgan fayllar
│   ├── images/
│   └── videos/
└── temp/                  # Vaqtinchalik fayllar
```

## Foydalanish 📖

### Web Interfaceda
1. "Rasm Yaratish" yoki "Video Yaratish" tabini tanlang
2. Rasmning yoki video-ning qisqacha tavsifini yozing
3. Uslub, o'lcha, va boshqa parametrlarni tanlang
4. "Yaratish" tugmasini bosing
5. Jarayon tugaguncha kutib turing
6. Yaratilgan faylni yuklab oling

### API orqali
```python
import requests

response = requests.post('http://localhost:8000/api/image/generate', json={
    'prompt': 'A beautiful sunset over mountains',
    'style': 'photography',
    'width': 768,
    'height': 768
})

task = response.json()
print(f"Task ID: {task['task_id']}")
```

## Teskari Olish ⚙️

```bash
# Status tekshirish
curl http://localhost:8000/health

# Mavjud modellar
curl http://localhost:8000/api/models

# Tarix
curl http://localhost:8000/api/image/models
```

## Muammolarni Hal Qilish 🔧

### CUDA xatosi
```bash
# CPU-da ishga tushirish
TORCH_DEVICE=cpu python main.py
```

### Xotira yetarli emas
- Model size-ni kichiklashtirishga urining
- GPU VRAM-ni oshmang
- CPU-da ishga tushirishni sinab ko'ring

### Model yuklanmayapti
```bash
# Modellarni qayta yuklab olish
rm -rf ~/.cache/huggingface
python main.py
```

## Litsenziya 📄

MIT License

## Muallif 👨‍💻

AI Media Generator - Sun'iy intellekt asosida rasm va video yaratuvchi.

## Qo'shimcha Resurslar 📚

- [Stable Diffusion Docs](https://huggingface.co/docs/diffusers)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PyTorch Documentation](https://pytorch.org/docs)

---

**Sug'utlar va xatolarni hisobot qiling** - Dasturni yaxshilab bering! 🚀
