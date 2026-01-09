import os
import uuid
import sys
import subprocess
import nest_asyncio

nest_asyncio.apply()

class TTSService:

    def __init__(self, output_dir="static/audio"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_audio(self, text, language="English"):
        # Map languages to Edge TTS voices
        lang_map = {
            "English": "en-NG-AbeoNeural",
            "Yoruba": "en-NG-EzinneNeural", # Fallback to Nigerian English (Native not available)
            "Hausa": "en-NG-EzinneNeural",
            "Igbo": "en-NG-AbeoNeural",
            "Pidgin": "en-NG-EzinneNeural"
        }
        
        voice = lang_map.get(language, "en-NG-AbeoNeural")
        
        try:
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(self.output_dir, filename)
            
            # Use subprocess to isolate asyncio loop
            worker_path = os.path.join(os.path.dirname(__file__), 'tts_worker.py')
            cmd = [sys.executable, worker_path, "--text", text, "--voice", voice, "--output", filepath]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                return filename
            else:
                print(f"[TTSService] Worker failed: {result.stderr}", file=sys.stderr)
                return None
                
        except Exception as e:
            print(f"[TTSService] Error generating audio: {e}", file=sys.stderr)
            return None
