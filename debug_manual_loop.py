import threading
import asyncio
import edge_tts
import os

async def _gen(text, voice, path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(path)

def run_manual():
    print(f"Thread {threading.current_thread().name}: Starting with Manual Loop...")
    
    text = "Yọ èpò kúrò lára àgbàdo."
    voice = "yo-NG-BunmiNeural"
    path = "test_manual.mp3"
    
    # helper logic
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        loop.run_until_complete(_gen(text, voice, path))
        
        print("Success! File created.")
        loop.close()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    run_manual()
