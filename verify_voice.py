from services.tts_service import TTSService
import os

def test_voice_gen():
    service = TTSService()
    
    test_cases = [
        ("Yoruba", "E kaaro o. Bawo ni nkan?"),
        ("Igbo", "Ututu oma. Kedu ka i mere?"),
        ("Hausa", "Ina kwana. Yaya aiki?")
    ]

    print("Testing Edge TTS Integration...")
    for lang, text in test_cases:
        print(f"\nGenerating {lang}...")
        filename = service.generate_audio(text, lang)
        
        if filename:
            print(f"Success! File created: {filename}")
            full_path = os.path.join(service.output_dir, filename)
            if os.path.exists(full_path):
                print(f"File verified on disk: {full_path}")
                print(f"Size: {os.path.getsize(full_path)} bytes")
            else:
                print("Error: File not found on disk.")
        else:
            print("Error: Audio generation failed.")

if __name__ == "__main__":
    test_voice_gen()
