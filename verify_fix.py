from services.tts_service import TTSService
import os

tts = TTSService()

print("--- Verification Test ---")

# 1. Test Hausa (Should work)
print("Testing Hausa...")
ha_file = tts.generate_audio("Sannu", "Hausa")
if ha_file:
    print(f"PASS: Hausa audio generated: {ha_file}")
else:
    print("FAIL: Hausa audio NOT generated")

# 2. Test Yoruba (Should be None)
print("\nTesting Yoruba...")
yo_file = tts.generate_audio("Bawo ni", "Yoruba")
if yo_file is None:
    print("PASS: Yoruba audio correctly skipped (None returned)")
else:
    print(f"FAIL: Yoruba audio generated unexpectedly: {yo_file}")

# 3. Test Igbo (Should be None)
print("\nTesting Igbo...")
ig_file = tts.generate_audio("Kedu", "Igbo")
if ig_file is None:
    print("PASS: Igbo audio correctly skipped (None returned)")
else:
    print(f"FAIL: Igbo audio generated unexpectedly: {ig_file}")

# 4. Test English (Should work)
print("\nTesting English...")
en_file = tts.generate_audio("Hello", "English")
if en_file:
    print(f"PASS: English audio generated: {en_file}")
else:
    print("FAIL: English audio NOT generated")
