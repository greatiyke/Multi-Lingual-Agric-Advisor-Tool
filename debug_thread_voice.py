import threading
import time
from services.tts_service import TTSService

def run_tts():
    print(f"Thread {threading.current_thread().name}: Starting TTS...")
    service = TTSService()
    try:
        filename = service.generate_audio("Yọ èpò kúrò lára àgbàdo.", "Yoruba")
        if filename:
            print(f"Thread {threading.current_thread().name}: Success! File: {filename}")
        else:
            print(f"Thread {threading.current_thread().name}: Failed (None returned)")
    except Exception as e:
        print(f"Thread {threading.current_thread().name}: Exception: {e}")

if __name__ == "__main__":
    t = threading.Thread(target=run_tts)
    t.start()
    t.join()
    print("Main: Thread finished.")
