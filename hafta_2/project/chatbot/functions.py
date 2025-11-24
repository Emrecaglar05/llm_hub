import random
from typing import Dict, Any, List

# Global değişkenler
reminders: List[Dict[str, str]] = []
todo_list: List[str] = []

def get_weather(city: str) -> Dict[str, Any]:
    """Şehir için hava durumu bilgisi döndürür"""
    demo_weather = {
        "Istanbul": "22°C, güneşli ☀️",
        "Ankara": "18°C, parçalı bulutlu ⛅",
        "Izmir": "25°C, sıcak 🌡️",
        "İstanbul": "22°C, güneşli ☀️",
        "İzmir": "25°C, sıcak 🌡️"
    }
    weather = demo_weather.get(city, "Bilgi bulunamadı")
    return {"city": city, "weather": weather}

def set_reminder(time: str, text: str) -> Dict[str, Any]:
    """Hatırlatma oluşturur"""
    reminder = {"time": time, "text": text}
    reminders.append(reminder)
    return {
        "message": f"Hatırlatma kaydedildi: '{text}' - Saat: {time}",
        "total_reminders": len(reminders)
    }

def create_todo(item: str) -> Dict[str, Any]:
    """Yapılacaklar listesine öğe ekler"""
    todo_list.append(item)
    return {
        "message": f"'{item}' yapılacaklar listene eklendi",
        "total_items": len(todo_list)
    }

def get_random_fact() -> Dict[str, str]:
    """Rastgele ilginç bir bilgi döndürür"""
    facts = [
        "Dünya yüzeyinin %71'i sudur 🌊",
        "Bir karınca yaklaşık 50 kat kendi ağırlığını taşıyabilir 🐜",
        "Venüs, Güneş Sistemi'ndeki en sıcak gezegendir 🔥",
        "Işık hızı saniyede 299,792 km'dir ⚡",
        "İnsan vücudunda yaklaşık 37 trilyon hücre vardır 🧬",
        "Bal asla bozulmaz 🍯",
        "Okyanusların sadece %5'i keşfedilmiştir 🌊",
        "Kalpakburun köpekbalığı 400 yaşından fazla yaşayabilir 🦈"
    ]
    return {"fact": random.choice(facts)}

def get_all_reminders() -> List[Dict[str, str]]:
    """Tüm hatırlatmaları döndürür"""
    return reminders

def get_all_todos() -> List[str]:
    """Tüm yapılacakları döndürür"""
    return todo_list