import asyncio
import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    for v in voices:
        if "NG" in v["ShortName"] or "Hausa" in v["FriendlyName"] or "Yoruba" in v["FriendlyName"] or "Igbo" in v["FriendlyName"]:
            print(f"{v['ShortName']} - {v['FriendlyName']}")

asyncio.run(main())
