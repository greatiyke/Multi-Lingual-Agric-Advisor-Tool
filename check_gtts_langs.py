from gtts.lang import tts_langs
import json

langs = tts_langs()
print(json.dumps(langs, indent=4))

# Explicit check
print(f"Yoruba (yo) supported: {'yo' in langs}")
print(f"Igbo (ig) supported: {'ig' in langs}")
print(f"Hausa (ha) supported: {'ha' in langs}")
