from gtts import gTTS
import os

try:
    print("Testing Yoruba...")
    tts_yo = gTTS(text="Bawo ni", lang='yo')
    tts_yo.save("test_yo.mp3")
    print("Yoruba worked!")
except Exception as e:
    print(f"Yoruba failed: {e}")

try:
    print("Testing Igbo...")
    tts_ig = gTTS(text="Kedu", lang='ig')
    tts_ig.save("test_ig.mp3")
    print("Igbo worked!")
except Exception as e:
    print(f"Igbo failed: {e}")
    
try:
    print("Testing Hausa...")
    tts_ha = gTTS(text="Sannu", lang='ha')
    tts_ha.save("test_ha.mp3")
    print("Hausa worked!")
except Exception as e:
    print(f"Hausa failed: {e}")
