# 🤖 LLM Öğrenme Yolculuğum

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Transformers](https://img.shields.io/badge/🤗_Transformers-FFD21E?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![GPU](https://img.shields.io/badge/GPU_Supported-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

### *Bu hafta LLM yolculuğuma başladım! 🚀*

</div>

---

## 📚 Bu Hafta Neler Öğrendim?

### 🎯 **1. Transformers Pipeline ile Metin Üretimi**

Hugging Face'in güçlü `pipeline` API'sini kullanarak modelleri nasıl çalıştıracağımı öğrendim:

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    device_map="auto",  # 🔥 GPU otomatik kullanımı
)
```

**💡 Öğrendiklerim:**
- ✅ `device_map="auto"` ile GPU otomatiği
- ✅ `max_new_tokens` ile cevap uzunluğu kontrolü
- ✅ `temperature` ile yaratıcılık ayarları

---

### 🇹🇷 **2. Türkçe Destekli Modeller**

**Qwen 2.5** modelini Türkçe sorulara cevap vermesi için yapılandırdım:

| Model | Boyut | Türkçe Desteği | Kullanım |
|-------|-------|----------------|----------|
| **Qwen2.5-1.5B-Instruct** | 1.5B parametre | ⭐⭐⭐⭐⭐ | Sohbet ve Q&A |
| **DialoGPT-medium** | 355M parametre | ⭐⭐⭐ | Dialog sistemleri |

```python
questions = [
    "Merhaba",
    "2+2 kaç eder?",
    "Python nedir?", 
    "Yapay zeka nasıl çalışır?"
]
```

---

### 💬 **3. Chat Template'leri ve Prompt Engineering**

Qwen modelinin özel sohbet formatını öğrendim:

```python
prompt = f"<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n"
```

**🎓 Önemli Detaylar:**
- `<|im_start|>` ve `<|im_end|>` etiketleri rolleri ayırır
- Kullanıcı ve asistan rolleri net şekilde tanımlanır
- Model böylece "kim konuşuyor" sorusuna cevap verir

---

### 🔐 **4. Environment Variables ve Güvenlik**

`.env` dosyası ile API token'larını güvenli şekilde yönetmeyi öğrendim:

```python
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")  # 🔒 Token güvende!
```

**⚠️ Güvenlik Notu:** Token'ları asla kodun içine yazmıyorum!

---

### ⚙️ **5. Tokenization Süreci**

Metinlerin nasıl sayısallaştırıldığını anladım:

```python
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
```

**📊 Tokenizer Ne Yapar?**
1. Metni küçük parçalara böler (tokenize)
2. Her parçayı sayıya çevirir
3. Model bu sayıları işler
4. Çıktıyı tekrar metne çevirir

---

## 🛠️ Kullandığım Teknolojiler

<div align="center">

| Kütüphane | Sürüm | Amaç |
|-----------|-------|------|
| `transformers` | 4.x | Model yükleme ve çalıştırma |
| `torch` | 2.x | GPU hızlandırma |
| `accelerate` | Latest | Multi-GPU desteği |
| `python-dotenv` | 1.x | Environment yönetimi |

</div>

---

## 🚀 Projelerdeki Öne Çıkan Özellikler

### ✨ **1. Otomatik GPU Kullanımı**
```python
device_map="auto"  # CPU'dan GPU'ya otomatik geçiş
```

### 🎨 **2. Yaratıcılık Kontrolü**
```python
temperature=0.7  # 0.1 (robotik) → 1.0 (yaratıcı)
```

### 📏 **3. Token Limiti Yönetimi**
```python
max_new_tokens=100  # Her cevapta maksimum 100 yeni kelime
```

### 🔄 **4. Hata Yönetimi**
```python
try:
    response = generator(prompt)
except Exception as e:
    print(f"❌ Hata: {e}")
```

---

## 📈 Gelecek Adımlarım

- [ ] Fine-tuning ile özel veri setleri
- [ ] RAG (Retrieval Augmented Generation) implementasyonu
- [ ] Streamlit ile web arayüzü
- [ ] Türkçe sentiment analysis
- [ ] Multi-turn conversation sistemi

---

## 🎓 Temel Kavramlar Özeti

| Kavram | Açıklama |
|--------|----------|
| **Pipeline** | Modeli kullanıma hazır hale getiren API |
| **Tokenizer** | Metin ↔ Sayı dönüşümü yapan araç |
| **Temperature** | Cevapların çeşitliliğini kontrol eder |
| **max_new_tokens** | Üretilecek maksimum kelime sayısı |
| **device_map** | CPU/GPU seçimi için parametre |

---

<div align="center">

### 💪 **İlk Hafta Başarıyla Tamamlandı!**

*"Her büyük yolculuk küçük bir adımla başlar."*

---

⭐ **Bu repo faydalı olduysa yıldız atmayı unutma!**

📫 **Sorularınız için:** [İletişime geç](linkedin.com/in/emre-çağlar-9bb493294/)

</div>

---

<div align="center">
<sub>Made with ❤️ and Python | 2025</sub>
