import os
import json
import google.generativeai as genai
from typing import Dict, Any, List
from .functions import get_weather, set_reminder, create_todo, get_random_fact

class GeminiChatbot:
    def __init__(self):
        # Gemini API Key'i ortam değişkeninden al
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY ortam değişkeni ayarlanmamış!")
        
        genai.configure(api_key=api_key)
        
        # Model oluştur
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Sohbet geçmişi
        self.chat_history = []
        
    def _execute_function(self, function_name: str, arguments: Dict[str, Any]) -> str:
        """Fonksiyon çağrısını gerçekleştir"""
        
        if function_name == "get_weather":
            result = get_weather(arguments.get("city", ""))
            return f"🌤️ {result['city']} için hava durumu: {result['weather']}"
        
        elif function_name == "set_reminder":
            result = set_reminder(arguments.get("time", ""), arguments.get("text", ""))
            return f"⏰ {result['message']}"
        
        elif function_name == "create_todo":
            result = create_todo(arguments.get("item", ""))
            return f"✅ {result['message']} (Toplam: {result['total_items']})"
        
        elif function_name == "get_random_fact":
            result = get_random_fact()
            return f"💡 {result['fact']}"
        
        else:
            return f"❌ Bilinmeyen fonksiyon: {function_name}"
    
    def handle(self, user_message: str) -> str:
        """Kullanıcı mesajını işle ve yanıt döndür"""
        try:
            # Sistem promptu
            system_prompt = """Sen yardımcı bir asistansın. Kullanıcıya Türkçe yanıt veriyorsun.

Eğer kullanıcı şunları isterse, özel fonksiyonları kullan:
- Hava durumu soruyorsa: get_weather fonksiyonunu kullan
- Hatırlatma istiyorsa: set_reminder fonksiyonunu kullan  
- Yapılacak eklemek istiyorsa: create_todo fonksiyonunu kullan
- İlginç bilgi istiyorsa: get_random_fact fonksiyonunu kullan

Fonksiyon çağrısı için JSON formatı:
{"function": "fonksiyon_adı", "arguments": {"param": "değer"}}
"""
            
            # Hava durumu kontrolü
            if any(word in user_message.lower() for word in ["hava", "weather", "sıcaklık"]):
                # Şehir ismi çıkar
                cities = ["istanbul", "ankara", "izmir", "İstanbul", "İzmir"]
                city = None
                for c in cities:
                    if c.lower() in user_message.lower():
                        city = c.capitalize()
                        break
                
                if city:
                    result = get_weather(city)
                    return f"🌤️ {result['city']} için hava durumu: {result['weather']}"
            
            # Hatırlatma kontrolü
            if any(word in user_message.lower() for word in ["hatırlat", "reminder", "hatırlatma"]):
                # Basit zaman ve metin çıkarma
                import re
                time_match = re.search(r'\d{1,2}[:\.]\d{2}', user_message)
                if time_match:
                    time = time_match.group(0)
                    text = user_message.replace(time, "").strip()
                    result = set_reminder(time, text)
                    return f"⏰ {result['message']}"
            
            # Todo kontrolü
            if any(word in user_message.lower() for word in ["ekle", "yapılacak", "todo", "görev"]):
                result = create_todo(user_message)
                return f"✅ {result['message']} (Toplam: {result['total_items']})"
            
            # İlginç bilgi kontrolü
            if any(word in user_message.lower() for word in ["bilgi", "fact", "ilginç", "söyle"]):
                result = get_random_fact()
                return f"💡 {result['fact']}"
            
            # Normal sohbet
            full_prompt = f"{system_prompt}\n\nKullanıcı: {user_message}\n\nAsistan:"
            response = self.model.generate_content(full_prompt)
            bot_response = response.text.strip()
            
            return bot_response
            
        except Exception as e:
            return f"❌ Hata oluştu: {str(e)}"