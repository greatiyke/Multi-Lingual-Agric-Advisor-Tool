import os
import uuid
from gtts import gTTS

class TTSService:
    def __init__(self, output_dir="static/audio"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_audio(self, text, language="English"):
        # Map languages to gTTS language codes
        lang_map = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Portuguese": "pt",
            "Italian": "it",
            "Yoruba": "yo",
            "Hausa": "ha",
            "Igbo": "ig",
            "Pidgin": "en" # Fallback
        }
        
        lang_code = lang_map.get(language, "en")
        
        try:
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(self.output_dir, filename)
            
            # Use gTTS (Google Translate TTS) - Free and supports 100+ languages
            tts = gTTS(text=text, lang=lang_code)
            tts.save(filepath)
            
            return filename
                
        except Exception as e:
            print(f"[TTSService] Error generating audio: {e}")
            return None
