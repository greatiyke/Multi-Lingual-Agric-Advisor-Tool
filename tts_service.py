from gtts import gTTS
import os
import uuid

class TTSService:
    def __init__(self, output_dir="static/audio"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_audio(self, text, language="English"):
        # Map full language names to gTTS codes
        lang_map = {
            "English": "en",
            "Yoruba": "yo",
            "Hausa": "ha",
            "Igbo": "ig",
            "Pidgin": "en" # Fallback to English for Pidgin as it's not directly supported
        }
        
        lang_code = lang_map.get(language, "en")
        
        try:
            print(f"[TTSService] Generating audio in {language} ({lang_code})...")
            tts = gTTS(text=text, lang=lang_code, slow=False)
            
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(self.output_dir, filename)
            
            tts.save(filepath)
            return filename
        except Exception as e:
            print(f"[TTSService] Error generating audio: {e}")
            return None
