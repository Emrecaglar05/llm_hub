import streamlit as st
import os
from chatbot.core import GeminiChatbot
from dotenv import load_dotenv

load_dotenv()
# Sayfa yapılandırması
st.set_page_config(
    page_title="🤖 Gemini Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Başlık
st.title("🤖 Gemini AI Chatbot")
st.markdown("---")

# API Key kontrolü
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ GEMINI_API_KEY ortam değişkeni ayarlanmamış!")
    st.info("""
    Lütfen `.env` dosyası oluşturun ve şu satırı ekleyin:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```
    
    API Key almak için: https://makersuite.google.com/app/apikey
    """)
    st.stop()

# Session state başlatma
if "bot" not in st.session_state:
    try:
        st.session_state.bot = GeminiChatbot()
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"❌ Bot başlatılamadı: {str(e)}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Yan panel - Özellikler
with st.sidebar:
    st.header("🛠️ Özellikler")
    st.markdown("""
    Bu chatbot şunları yapabilir:
    
    - 🌤️ Hava durumu sorgulama
    - ⏰ Hatırlatma oluşturma
    - ✅ Yapılacaklar listesi
    - 💡 Rastgele bilgiler
    
    **Örnek komutlar:**
    - "İzmir hava durumu nedir?"
    - "Saat 14:30'da toplantı hatırlatması oluştur"
    - "Alışveriş yap görevini ekle"
    - "Bana ilginç bir bilgi ver"
    """)
    
    st.markdown("---")
    
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.messages = []
        st.rerun()

# Ana alan - Sohbet geçmişi
chat_container = st.container()

with chat_container:
    if len(st.session_state.messages) == 0:
        st.info("👋 Merhaba! Size nasıl yardımcı olabilirim?")
    
    for i, chat in enumerate(st.session_state.messages):
        # Kullanıcı mesajı
        with st.chat_message("user"):
            st.markdown(chat["user"])
        
        # Bot yanıtı
        with st.chat_message("assistant"):
            st.markdown(chat["bot"])

# Kullanıcı girişi
user_input = st.chat_input("Mesajınızı yazın...")

if user_input:
    # Kullanıcı mesajını göster
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Bot yanıtını al
    with st.chat_message("assistant"):
        with st.spinner("Düşünüyorum..."):
            bot_response = st.session_state.bot.handle(user_input)
            st.markdown(bot_response)
    
    # Mesajları kaydet
    st.session_state.messages.append({
        "user": user_input,
        "bot": bot_response
    })
    
    # Sayfayı güncelle
    st.rerun()