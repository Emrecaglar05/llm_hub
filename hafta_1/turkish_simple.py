"""
Basit Türkçe LLM Örneği (GPU destekli)
"""

from transformers import pipeline

# Türkçe destekli model
MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"

print("🇹🇷 Türkçe LLM yükleniyor...")

# Pipeline oluştur
generator = pipeline(
    "text-generation",
    model=MODEL_ID,
    device_map="auto",   # GPU varsa kullanır
    max_new_tokens=50,  # maksimum 50 token üretir
    temperature=0.3      # yaratıcı cevaplar için düşük sıcaklık
)

# Türkçe sorular
questions = [
    "Merhaba",
    "2+2 kaç eder?",
    "Python nedir?", 
    "Yapay zeka nasıl çalışır?"
]

print("✅ Model hazır! Türkçe sorular test ediliyor...\n")

for i, question in enumerate(questions, 1): # Soruları sırayla işlemeye yarar enumerate
    print(f"🔤 Soru {i}: {question}")
    
    # Qwen chat formatı
    prompt = f"<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n"
    #Qwen, tek seferlik metin üretiminden ziyade sohbet için tasarlanmış. 
    # Kullanıcı/assistant etiketleri ile kim ne söylediğini ayırt ediyor. 
    # Bu sayede model “asistan” rolünü bilir ve cevapları kullanıcı rolüne karışmaz.
    
    try:
        response = generator(prompt)
        full_text = response[0]["generated_text"]
        
        # Sadece assistant cevabını al
        if "<|im_start|>assistant\n" in full_text:
            answer = full_text.split("<|im_start|>assistant\n")[-1]
            answer = answer.split("<|im_end|>")[0].strip()
            print(f"🤖 Cevap: {answer}")
        else:
            print(f"🤖 Cevap: {full_text}")
            
    except Exception as e:
        print(f"❌ Hata: {e}")
    
    print("-" * 60)

print("\n🎉 Test tamamlandı!")
