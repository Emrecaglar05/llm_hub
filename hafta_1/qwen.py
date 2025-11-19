from transformers import AutoTokenizer, pipeline
import torch
import accelerate
MODEL_ID ="Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
genarator = pipeline(
    "text-generation", 
    model=MODEL_ID, 
    device_map="auto", # Cihazın otomatik olarak gpu kullanmasını sağlar
    tokenizer=tokenizer, # Değişken olarak tanımladığım tokenizeri kullanıyorum
    max_new_tokens=100, # Cevap verirken en fazla 100 yeni token üretmesini sağlar
    temperature=0.7 # Yaratıcılığı ayarlar (daha yüksek değerler daha yaratıcı cevaplar sağlar
)

prompt = "LLM nedir? Kısa ve anlaşılır bir şekilde cevap ver."

response = genarator(prompt) # Cevap üretme işlemi
print(response[0]['generated_text'])
