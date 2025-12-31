from gtts.lang import tts_langs
import json

langs = tts_langs()
print(json.dumps(langs, indent=2))
