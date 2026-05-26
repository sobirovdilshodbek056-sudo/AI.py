# USAGE GUIDE - Foydalanish Qo'llanmasi

## Tezkor Boshlash 🚀

### Windows:
```bash
setup.bat
python main.py
```

### Linux/Mac:
```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
python main.py
```

---

## Web Interfacesi 🌐

### 1. Rasm Yaratish
```
1. Parametrlar:
   - Prompt: Rasm tavsifi (inglizcha, o'zbekcha yoki ruscha)
   - Uslub: 8 ta turli uslub (Realistic, Artistic, Cartoon, va h.k.)
   - O'lcham: 256x256 dan 1024x1024 gacha
   - Sifat: Kovarak soniadagi bosqichlar

2. Bosing: "Rasm Yaratish"

3. Kutib turing (30-120 soniya)

4. Rasmni yuklab oling yoki ko'ring
```

### 2. Video Yaratish
```
1. Parametrlar:
   - Prompt: Video tavsifi
   - Uslub: Cinematic, Artistic, Cartoon, 3D Render
   - Davomiyligi: 1-60 soniya
   - Kadr soni (FPS): 12-60

2. Bosing: "Video Yaratish"

3. Kutib turing (1-10 minut - davomiyligi va parametrlariga bog'liq)

4. Videoni ko'ring yoki yuklab oling
```

---

## API Foydalanish 📡

### Python-da:
```python
from example_usage import AIMediaGenerator

client = AIMediaGenerator()

# Rasm yaratish
image = client.generate_image(
    prompt="A beautiful sunset over mountains",
    style="photography"
)

# Video yaratish
video = client.generate_video(
    prompt="A spaceship flying in space",
    duration=5,
    style="realistic"
)
```

### CURL-da:
```bash
# Rasm yaratish
curl -X POST http://localhost:8000/api/image/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A beautiful landscape",
    "style": "realistic",
    "width": 768,
    "height": 768
  }'

# Statusni tekshirish
curl http://localhost:8000/api/image/status/{task_id}
```

---

## Prompt Yozish Maslahlari 💡

### ✅ YAXSHI PROMPTS:

**Rasm uchun:**
```
"High quality, detailed oil painting of a castle on a mountain during sunset, 
cinematic lighting, masterpiece, artstation"

"Professional photography of a serene forest with morning mist and wildlife, 
4k, detailed, natural lighting"

"Concept art of a futuristic cyberpunk city with neon lights, 
extremely detailed, artstation quality"
```

**Video uchun:**
```
"Cinematic scene of a spacecraft entering a planet's atmosphere, 
dramatic lighting, 4k quality"

"A river flowing through a beautiful canyon landscape, 
smooth camera movement, cinematic"
```

### ❌ YOMON PROMPTS:
```
"Cool stuff" ❌
"Make something nice" ❌
"A place" ❌
"Video please" ❌
```

### 💡 MASLAHLARI:
1. **Bo'lsin aniq** - "sunset" emas, "beautiful golden sunset over mountains"
2. **Stili aniqla** - uslub parametrini foydalaning
3. **Sifat so'zlarini qo'shing** - "high quality", "detailed", "masterpiece"
4. **Referensi berish** - "in the style of [artist]", "artstation", "concept art"
5. **Mahdiyatni talqin qiling** - "photography", "oil painting", "3D render"

---

## Parametrlar Tushuntirilishi 📊

### Rasm Generatsiyasi:

| Parametr | Qiymat | Tushuntirish |
|----------|--------|-------------|
| width | 256-1024 | Rasm kengligini pikselda |
| height | 256-1024 | Rasm balanligini pikselda |
| num_images | 1-4 | Bir marta nechtata rasm yaratish |
| guidance_scale | 1-20 | Prompt ta'sirining kuchi (7.5 optimal) |
| steps | 20-100 | Generatsiya bosqichlari (ko'p = sifatli lekin sekin) |

### Video Generatsiyasi:

| Parametr | Qiymat | Tushuntirish |
|----------|--------|-------------|
| duration | 1-60 | Video davomiyligi (soniya) |
| fps | 12-60 | Kadr soni (24 = standart kino) |
| width | 256-1024 | Video kengligini pikselda |
| height | 256-1024 | Video balannigini pikselda |

---

## Tipik Vaqtlar ⏱️

Optimal kompyuter uchun:

| Operatsiya | Vaqt | Shunosi |
|-----------|------|---------|
| Rasm (768x768) | 30-60s | Birinchi marta modelni yuklab oladi |
| Rasm (1024x1024) | 60-120s | Batafsil rasm |
| Video (5s, 512x512) | 3-5 min | GPU talab qiladi |
| Video (10s, 512x512) | 5-10 min | Sekinroq |

**GPU bo'lmasa:** Vaqtlar 5-10x ko'payadi!

---

## Tekstlash 🔍

### Muammoni Hal Qilash:

**Xatolik: "CUDA out of memory"**
```
Yechim:
- Rasm o'lchamini kichiklashtirib ko'ring (512x512)
- Bosqichlar sonini kamaytiring (30-40)
- GPU-ning boshqa dasturini yoping
- CPU-da ishlang: PYTORCH_DEVICE=cpu python main.py
```

**Xatolik: "Model topilmadi"**
```
Yechim:
- Internet ulanishini tekshiring
- ~/.cache/huggingface ni o'chirib tashlang
- Modelni qayta yuklab olishga ijozat bering
```

**Rasm yoki video sifasi past**
```
Yechim:
- num_inference_steps ni oshiring (80-100)
- guidance_scale ni o'zgartirib ko'ring (6-10)
- Prompt-ni tekshirib ko'ring
- Uslubni o'zgartirib ko'ring
```

**Server qayta ishga tushishi**
```bash
ps aux | grep python
kill -9 [process_id]  # Kill old process
python main.py        # Start again
```

---

## Monitoring 📈

### Logs tekshirish:
```bash
tail -f logs/app.log
```

### API Health Check:
```bash
curl http://localhost:8000/health
```

### Mavjud Modellar:
```bash
curl http://localhost:8000/api/models
```

---

## Advanced Foydalanish 🎓

### Custom Config:
```python
# app/core/config.py-ni o'zgartiring:
DEFAULT_IMAGE_SIZE = (512, 512)  # Kichik
MAX_VIDEO_DURATION = 30          # Qisqaroq
```

### Background Processing optimizatsiya:
```python
# app/services/image_generator.py-ni redaktir qiling
MAX_WORKERS = 2  # Parallel tasks
```

### Custom API Endpoints qo'shish:
```python
# app/api/routes_custom.py yarating
# main.py-da include qiling
```

---

## Maslahlari va Fokuslar 💡

### GPU Optimizatsiya:
1. `torch.backends.cudnn.benchmark = True` - fastroq
2. fp16 foydalaning - xotirasi kamroq
3. Batch processing - ko'p taskni bir vaqtda ishla

### Memory Management:
1. Yaratilgan fayllarni muntazam o'chirib turung
2. `temp/` folderni tozalang
3. Cache-ni reset qiling

### Production:
1. Gunicorn/Uvicorn orqali ishga tushiring
2. Nginx reverse proxy qo'ying
3. Docker containerda ishga tushiring

---

## Ko'proq Qo'llanma 📚

- [Stable Diffusion Documentation](https://huggingface.co/docs/diffusers)
- [FastAPI Docs](http://localhost:8000/docs) - Swagger UI
- [PyTorch Guide](https://pytorch.org/docs/)

---

## Qo'shimcha Savollar? 💬

Muammoni hal qilishda qiynalayotgan bo'lsagiz:
1. logs/ folderni tekshiring
2. README.md ni o'qib chiqing
3. example_usage.py-ni o'rganing
4. API documentation: http://localhost:8000/docs

---

**Taklif va bug xabarlari uchun pull request yuboring!** 🙏

Dasturni xursand bilan foydalaning! 🎉
